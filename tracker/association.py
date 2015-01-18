#!/usr/bin/env python

# TODO --> import from init
from sklearn.utils.linear_assignment_ import _hungarian
from tracker import np
from tracker import track


def lossfunction(tr, sub):

    # Where to create the loss using data from the subject class

    # First simple loss function
    # Based in simple distance to subject base
    (xt, yt), radius = tr.subject.circle
    (xs, ys), radius = sub.circle

    loss = np.sqrt(np.power(xt - xs, 2) + np.power(yt - ys, 2))

    threshold = 1000

    return loss, threshold


def globallossfunction(tr, sub):

    threshold = 0
    loss = np.zeros((len(tr), len(sub)))

    for jj in range(len(tr)):
        for ii in range(len(sub)):
            loss[jj, ii], treshold = lossfunction(tr[jj], sub[ii])

    return loss, threshold


def assignsubjecttonewtrack(sub):

    tr = track.Track()
    tr.setdefault(sub)
    return tr


def assignsubjecttoexistingtrack(tr, sub):

    tr.update(sub)
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

    return new_res


def trackupdate(tr, sub, res):

    new_track = []
    del_index = []

    # Update succesful associations
    for ii in range(len(res)):
        y, x = res[ii]

        new_tr = assignsubjecttoexistingtrack(tr[y], sub[x])

        new_track.append(new_tr)
        del_index.append(ii)

    tr = np.delete(tr, del_index)
    tr = tr.tolist()

    # Update missed associations
    del_index = []

    for ii in range(len(tr)):
        tr[ii].update()

        # In case track got lost
        if tr[ii].state == 4:
            del_index.append(ii)

    if del_index:
        tr = np.delete(tr, del_index)
        tr = tr.tolist()

    for n in new_track:
        tr.append(n)

    # Update new subjects
    del_index = []
    del_index = np.delete(res, 0, 1)

    sub = np.delete(sub, del_index)
    sub = sub.tolist()

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
        new_track = trackupdate(tr, sub, res)

    return new_track
