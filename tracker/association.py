#!/usr/bin/env python

# TODO --> import from init
from sklearn.utils.linear_assignment_ import _hungarian
from tracker import np
from tracker import track
from tracker import variables


def lossfunction(tr, sub):

    # Where to create the loss using data from the subject class

    # First simple loss function
    # Based in simple distance to subject base
    (xt, yt), radius = tr.subject.circle
    (xs, ys), radius = sub.circle

    loss = int(np.sqrt(np.power(xt - xs, 2) + np.power(yt - ys, 2)))

    return loss


def globallossfunction(tr, sub):

    threshold = 50
    loss = np.zeros((len(tr), len(sub)))

    for jj in range(len(tr)):
        for ii in range(len(sub)):
            loss[jj, ii] = lossfunction(tr[jj], sub[ii])

    return loss, threshold


def assignsubjecttonewtrack(sub):

    variables.num_tracks += 1
    tr = track.Track()
    tr.setdefault(sub, variables.num_tracks)
    return tr


def assignsubjecttoexistingtrack(tr, sub):

    tr.updatetrack(sub)
    return tr


def hungarianassociation(loss, threshold):

    # SKLEARN association method
    res = _hungarian(loss)

    del_index = []

    for ii in range(len(res)):
        y, x = res[ii]

        if(loss[y, x] > threshold):
            del_index.append(ii)

    new_res = np.delete(res, del_index, 0)

    return new_res


def printtracks(tr):

    for t in tr:
        t.printtrack()


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

    new_tr = new_tr_copy

    for ii in range(len(non_tr)):

        a = loss[non_tr[ii], :]
        b = a[a < threshold]

        if len(b) > 0:
            if len(b) > 1:
                b = [b.min()]

            # Get merging track overlapped subject's index
            idx_b = np.argwhere(a == b)

            # Get parent track's index
            idx_new_tr = np.argwhere(res == idx_b[0, 0])

            # Merge tracks
            try:  # Maybe wrong hungarian as we expected
                new_tr[idx_new_tr[0, 0]].associatetrack(tr[ii])
                tr = np.delete(tr, ii)
                tr = tr.tolist()

            except:
                pass

    return new_tr, tr


def tracksplit(init_sub, new_sub, loss, threshold, res):

    for ii in range(len(non_sub)):

        a = loss[:, non_sub[ii]]
        b = a[a < threshold]

        if len(b) > 0:
            print 'Split'  # TODO

    """
    TODO
    ----
    only split track when a track with associated
    childs can be assigned to two subjects
    """


def trackupdate(tr, sub, res, loss, threshold):

    new_track = []
    del_index_sub = []
    del_index_tr = []
    init_tr = tr
    init_sub = sub

    # Update successful associations
    for ii in range(len(res)):
        y, x = res[ii]

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
        tr, new_track, non_index_tr, loss, threshold, res)

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
    del_index = []
    del_index = np.delete(res, 0, 1)

    sub = np.delete(sub, del_index)
    sub = sub.tolist()

    print sub

    for s in sub:
        t = assignsubjecttonewtrack(s)
        tr.append(t)

    return tr


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

        # Calculate loss function
        loss, threshold = globallossfunction(tr, sub)

        # Hungarian association
        res = hungarianassociation(loss, threshold)

        # Update tracks with new association
        new_track = trackupdate(tr, sub, res, loss, threshold)

    return new_track
