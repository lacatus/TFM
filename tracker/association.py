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

    return loss


def assignsubjecttonewtrack(sub):

    tr = track.Track()
    tr.setdefault(sub)
    return tr


def assignsubjecttoexistingtrack(tr, sub):
    pass


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

    # Detection && Tracks present
    else:
        loss = np.zeros((len(tr), len(sub)))
        # Calculate loss function
        for jj in range(len(tr)):
            for ii in range(len(sub)):
                loss[jj, ii] = lossfunction(tr[jj], sub[ii])

        # Hungarian association
        res = _hungarian(loss)
        print 'loss'
        print loss
        print 'res'
        print res

    return new_track
