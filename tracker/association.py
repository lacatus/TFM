#!/usr/bin/env python

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

    # Initialize tracks
    if not tr:

        for s in sub:

            tr = assignsubjecttonewtrack(sub)
            new_track.append(tr)

    # If tracks already initialized
    # BIG TODO FOR TOMORROW
    """
    else:
        for t in tr:
            for s in sub:
                loss = lossfunction(t, s)
                print loss
        tr = sub
    """

    return new_track
