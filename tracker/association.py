#!/usr/bin/env python

# TODO --> import from init
from sklearn.utils.linear_assignment_ import _hungarian
from tracker import cv2
from tracker import np
from tracker import stats
from tracker import track
from tracker import variables
from scipy.stats import norm    #<--@cia

def normpdf(x, m, v):
    
    return (1 / (np.sqrt(2 * np.pi) * v)) * np.exp(-(1./2) * np.power((x - m) / v, 2))


def lossfunction(tr, sub):
    #@CIA june-25-2015

    loss=0
    distance=0
    #----prepare variables
    (x, y), (h, b), a = sub.rot_box
    p = tr.pf.p
    p_star = tr.pf.p_star
    p_mean = tr.pf.p_mean

    #----obtain loss(tr,sub)
    #--distance(tr,sub)
    sqDistance = np.power(x - p_mean[0], 2) + np.power(y - p_mean[1], 2)
    distance = np.sqrt(sqDistance)
    #--mix of gaussians
    w_star = 0.20
    w_mean = 0.80
    #sigma_mean = 1
    #sigma_star = 1

    """
    TODO
    ----
    cov --> anchura de las particulas en vez de 1
    """

    """
    COLOR_CUBES
    ---
    1 vector de 8 cubos por canal de color BGR
    ---
    SUBJECT (Deteccion)
    b, g, r = sub.rgb_cubes
    TRACKER
    b, g, r = tr.rgb_cubes
    """

    #.for X
    mu_starX = p_star[0] # x_star
    mu_meanX = p_mean[0] # x_mean
    sigma_starX = p_star[3]#/2
    sigma_meanX = p_mean[3]#/2
    lossX = w_star*norm.pdf(x,mu_starX,sigma_starX) + w_mean*norm.pdf(x,mu_meanX,sigma_meanX)
    #.for Y
    mu_starY = p_star[1] # x_star
    mu_meanY = p_mean[1] # x_mean
    sigma_starY = p_star[2]#/2
    sigma_meanY = p_mean[2]#/2
    lossY = w_star*norm.pdf(y,mu_starY,sigma_starY) + w_mean*norm.pdf(y,mu_meanY,sigma_meanY)    #.neglog of joint(X,Y) assuming independence

    # For appareance

    lossApp = cv2.compareHist(tr.rgb_cubes.ravel().astype('float32'),
                          sub.rgb_cubes.ravel().astype('float32'),
                          cv2.cv.CV_COMP_BHATTACHARYYA)
    #print cv2.normalize(sub.rgb_cubes.ravel().astype('float32'))
    #print cv2.normalize(tr.rgb_cubes.ravel().astype('float32'))
    
    loss = - np.log(lossX) - np.log(lossY) + np.log(lossApp)

    if loss == float('Inf') or loss == -float('Inf'):
        loss = 100
    return loss, distance

def lossfunction__old1(tr, sub):
    #@Borja(orginal)1

    # Where to create the loss using data from the subject class

    # First simple loss function---------------------------------------
    # Based in simple distance to subject base
    (xt, yt), radius = tr.pf.circle
    (xs, ys), radius = sub.circle

    distance = int(np.sqrt(np.power(xt - xs, 2) + np.power(yt - ys, 2)))

    # Second loss function---------------------------------------------
    # Based in normal probability density function of particles for
    # position and detection size

    (x, y), (h, w), a = sub.rot_box

    p = tr.pf.p
    p_star = tr.pf.p_star
    p_mean = tr.pf.p_mean

    # optimizacion --> no calcular constantemente mean y std, sino hacerlo antes de entrar aqui
    # loss = -x -y -vx -vy
    loss  = - np.log(normpdf(x, np.mean(p[:, 0]), np.std(p[:, 0]))) \
        - np.log(normpdf(y, np.mean(p[:, 1]), np.std(p[:, 1]))) \
        - np.log(normpdf(x - p_star[0], np.mean(p[:, 4]), np.std(p[:, 4]))) \
        - np.log(normpdf(y - p_star[1], np.mean(p[:, 5]), np.std(p[:, 5]))) 
        #- np.log(normpdf(sub.h, np.mean(p[:, 4]), np.std(p[:, 4])))

    debug_flag=0
    if debug_flag:
        """
        print '###'
        print normpdf(p_star[1] - y, np.mean(p[:, 5]), np.std(p[:, 5]))
        print x
        print y
        """

        """
        print '----'
        print 'x, y, h: %s, %s, %s' % (x, y, sub.h)
        #print 'x: %s' % - np.log(normpdf(x, np.mean(p[:, 0]), np.std(p[:, 0])))
        print 'vx: %s' % - np.log(normpdf(p_star[0] - x, np.mean(p[:, 4]), np.std(p[:, 4])))
        print 'vy: %s' % - np.log(normpdf(p_star[1] - y, np.mean(p[:, 5]), np.std(p[:, 5])))
        print '----'
        """

    return loss, distance


def globallossfunction(tr, sub):

    threshold = 10
    loss = np.zeros((len(tr), len(sub)))
    distance = np.zeros((len(tr), len(sub)))

    for jj in range(len(tr)):
        for ii in range(len(sub)):
            loss[jj, ii], distance[jj, ii] = lossfunction(tr[jj], sub[ii])
            #loss[jj, ii], distance[jj, ii] = lossfunction__old1(tr[jj], sub[ii])

    print loss

    return loss, distance, threshold


def assignsubjecttonewtrack(sub):

    variables.num_tracks += 1
    tr = track.Track()
    tr.setdefault(sub, variables.num_tracks)
    return tr

def assignsubjecttoexistingtrack(tr, sub):

    score = lossfunction(tr, sub)
    tr.updatetrack(sub, score[0])
    return tr

def postproc(loss, threshold):

    #print np.isinf(loss)
    #print loss
    #x = np.isinf(loss)
    #print x
    #mask_a = np.all(np.isinf(loss), axis = 1)
    #mask_b = np.all(np.isinf(loss), axis = 0)
    #print mask_a
    #print mask_b

    loss[loss > threshold] = threshold * 2

    return loss

def hungarianassociation(loss, distance, threshold):

    loss = postproc(loss, threshold)

    debug_flag = 0
    if debug_flag: print loss

    # SKLEARN association method
    res = _hungarian(loss)

    del_index = []

    for ii in range(len(res)): 
        y, x = res[ii]

        if(loss [y, x] > threshold):
            del_index.append(ii)

    new_res = np.delete(res, del_index, 0)
    #print new_res
    return new_res

def getnotassociatedindex(len_sub, len_tr, del_tr, del_sub):

    non_tr = []
    non_sub = []

    non_sub = np.array(range(len_sub))
    non_tr = np.array(range(len_tr))

    non_sub = np.delete(non_sub, del_sub)
    non_tr = np.delete(non_tr, del_tr)

    non_sub = non_sub.tolist()
    non_tr = non_tr.tolist()

    return non_sub, non_tr


def trackmerge(tr, new_tr_copy, non_tr, loss, threshold, res):

    threshold_ = threshold + (2 * threshold / 3)  # margin

    new_tr = new_tr_copy

    for ii in range(len(non_tr)):

        a = loss[non_tr[ii], :]
        b = a[a < threshold_]

        if len(b) > 0:
            if len(b) > 1:
                b = [b.min()]

            # Get merging track overlapped subject's index
            idx_b = np.argwhere(a == b)

            # Get parent track's index
            idx_new_tr = np.argwhere(res[:, 1] == idx_b[0, 0])

            # Merge tracks
            try:  # Maybe wrong hungarian as we expected

                # Only associate locked tracks
                if tr[ii].state is 2 and new_tr[idx_new_tr[0, 0]].state is 2:
                    new_tr[idx_new_tr[0, 0]].associatetrack(tr[ii])
                    tr = np.delete(tr, ii)
                    tr = tr.tolist()

            except:
                pass

    return new_tr, tr


def tracksplit(new_tr, sub, threshold):
    # usage of appareance model might be a good option
    # for distance calculation in this section

    threshold_ = threshold + (2 * threshold / 3)  # margin

    del_idx = []

    for ii in range(len(sub)):
        for tr in new_tr:
            if tr.group and tr.calculatesubjectdistance(sub[ii], threshold_):
                n_tr = tr.deassociatetrack()
                score = lossfunction(tr, sub[ii])
                n_tr.updatetrack(sub[ii], score[0])
                new_tr.append(n_tr)
                del_idx.append(ii)
                break

    if del_idx:
        sub = np.delete(sub, del_idx)
        sub = sub.tolist()

    return new_tr, sub


def printtracks(tr):

    """
    for t in tr:
        t.printtrack()
    """
    pass


def trackupdate(tr, sub, res, loss, threshold):

    new_track = []
    del_index_sub = []
    del_index_tr = []
    init_tr = tr
    init_sub = sub
    threshold_distance = 100

    aux_res = res

    # Update successful associations
    for ii in range(len(res)):
        y, x = res[ii]
        aux_res = np.delete(aux_res, 0, axis=0)
        new_tr = assignsubjecttoexistingtrack(tr[y], sub[x])
        new_track.append(new_tr)
        del_index_sub.append(x)
        del_index_tr.append(y)

    sub = np.delete(sub, del_index_sub)
    tr = np.delete(tr, del_index_tr)
    sub = sub.tolist()
    tr = tr.tolist()

    # Update missed associations --> where merge should act
    non_index_sub, non_index_tr = getnotassociatedindex(
        len(init_sub), len(init_tr), del_index_tr, del_index_sub)

    new_track, tr = trackmerge(
        tr, new_track, non_index_tr, loss, threshold_distance, res)

    del_index = []

    for ii in range(len(tr)):
        tr[ii].updatetrack()

        # In case track got lost
        if tr[ii].state == 4:
            del_index.append(ii)

    if del_index:
        tr = np.delete(tr, del_index)
        tr = tr.tolist()

    for n in new_track:
        tr.append(n)

    # Update new subjects --> where split should act

    tr, sub = tracksplit(new_track, sub, threshold_distance)

    """
    TODO
    ----
    - Only assign new tracks in outer positions of the image
    """

    for s in sub:
        t = assignsubjecttonewtrack(s)
        tr.append(t)

    return tr


def pfdiffussion(tr):

    new_tr = []

    for t in tr:

        t.pf.pdiffussion()
        new_tr.append(t)

    return new_tr


def pfupdate(tr):

    new_tr = []

    for t in tr:

        t.pf.plikelihood()
        new_tr.append(t)

    return new_tr

def alternativeAssociation(loss, distance, threshold, tr, res):

    print '-----'
    print 'Alfre2 association'
    print '-----'

    debug_flag=0

    if debug_flag: print loss

    # get best detection for each tracker
    y, x = loss.shape

    new_res = np.array([[]])

    for jj in range(y):
        best_detection = loss[jj, :].argmin(axis = 0)
        s = loss[jj, best_detection]
        # -- TOMA DE DECISIONES --
        # 1) anomalia del score
        mx = tr[jj].score_mu + 3*tr[jj].score_sigma
        mn = tr[jj].score_mu - 3*tr[jj].score_sigma
        if tr[jj].mature:
            if s > mn and s < mx:
                if not new_res.any():
                    new_res = np.array([[jj, best_detection]])
                else:
                    new_res = np.vstack((new_res,np.array([jj, best_detection])))
        else:
            if not new_res.any():
                new_res = np.array([[jj, best_detection]])
            else:
                new_res = np.vstack((new_res, np.array([jj, best_detection])))

        if debug_flag:
            #print 'loss: %s' \
            #      %  loss[jj, best_detection]
            print '[%s , %s] <-- %s' \
                  % (mn, mx, loss)
            #print 'mu: %s, sigma: %s' \
            #      % (tr[jj].score_mu, tr[jj].score_sigma)
            print tr[jj].score
            print
            print 'res'
            print res
            print 'new_res'
            print new_res

    return new_res


def associatetracksubject(tr, sub):

    new_track = []

    # CASES
    # NO tracks
    if not tr:

        for s in sub:

            tr = assignsubjecttonewtrack(s)
            new_track.append(tr)

    # NO detectiondetections4tracker
    elif not sub:

        for t in tr:
            t.updatemisscount()

        new_track = tr

    # Detection && Tracks present
    else:

        # Particle diffussion
        tr = pfdiffussion(tr)

        # Calculate loss function
        loss, distance, threshold = globallossfunction(tr, sub)

        # Hungarian association
        res = hungarianassociation(loss, distance, threshold)

        # Alternative association
        #res = alternativeAssociation(loss, distance, threshold, tr, res)

        # Update tracks with new association
        new_track = trackupdate(tr, sub, res, loss, threshold)

    # Update prob particle filter
    new_track_2 = pfupdate(new_track)

    return new_track_2
