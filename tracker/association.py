#!/usr/bin/env python

# TODO --> import from init
from sklearn.utils.linear_assignment_ import _hungarian
from tracker import np
from tracker import track


def lossfunction(tr, sub):

    # First simple loss function
    # Based in simple distance to subject base
    xt, yt = tr.subject.base
    xs, ys = sub.base

    loss = np.sqrt(np.power(xt - xs, 2) + np.power(yt - ys, 2))

    threshold = 50

    return loss, threshold


def assignsubjecttonewtrack(sub):

    tr = track.Track()
    tr.setdefault(sub)
    return tr


def assignsubjecttoexistingtrack(tr, sub):
    pass


def trackupdate(tr, sub, loss, res):

    """
    TODO
    - [ ] cambiar distancia basada en posicion central, no de la base
    - [x] checkear si la asociacion supera un threshold
    - [ ] sino update de tracks
    - [ ] realizar metodo de pintar tracks
    """

    new_track = []
    #return new_track
    return tr


def hungarianassociation(loss, threshold):

    # SKLEARN association method
    res = _hungarian(loss)

    del_index = []

    # Threshold results
    for ii in range(len(res)):
        y, x = res[ii]

        if(loss[y, x] > threshold):
            del_index.append(ii)

    new_res = np.delete(res, del_index, 0)

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

    # NO detection
    elif not sub:

        for t in tr:
            t.updatemisscount()

        new_track = tr

    # Detection && Tracks present
    else:

        threshold = 0

        loss = np.zeros((len(tr), len(sub)))
        # Calculate loss function
        for jj in range(len(tr)):
            for ii in range(len(sub)):
                loss[jj, ii], treshold = lossfunction(tr[jj], sub[ii])

        # Hungarian association
        res = hungarianassociation(loss, threshold)

        #new_track = trackupdate(tr, sub, loss, res)

    return new_track
