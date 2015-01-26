#!/usr/bin/env python

from tracker import np
from tracker import track


def gettrackcircles(tracks):

    circles = []

    for t in tracks:
        circles.append(t.subject.circle)

    return circles


def checkoverlap(x1, y1, r1, x2, y2, r2):

    dxy = np.sqrt(np.power(y2 - y1, 2) + np.power(x2 - x1, 2))
    dr = np.power(r2 + r1, 2)

    if dxy <= dr:
        return True

    else:
        return False


def checkbelonging(index, jj):

    for ii in range(len(index)):
        a, b = index[ii]

        if b == jj:
            return a

    return False


def getcircleintersections(circles, tr):  # Might be Cython meat 

    groups = []
    groups_index = []

    for jj in range(len(circles)):
        (x1, y1), r1 = circles[jj]

        res = checkbelonging(groups_index, jj)

        if res:
            gtr = groups[res]

        else:
            gtr = track.TrackGroup()
            gtr.setdefault(tr[jj])

            groups.append(gtr)
            groups_index.append([len(groups) - 1, jj])

        for ii in range(len(circles)):
            (x2, y2), r2 = circles[ii]

            if jj >= ii:
                continue

            if checkoverlap(x1, y1, r1, x2, y2, r2):
                gtr.appendnewtrack(tr[ii])
                groups_index.append([len(groups) - 1, ii])

    print len(groups)
    return groups


def findoverlappingcircles(tracks):

    """
    TODO
    ----
    Grouping must be done uppon the loss function
    Next big todo
        - Maybe different loss functions (grouping, group exit, ...)
    """

    circles = gettrackcircles(tracks)
    groups = getcircleintersections(circles, tracks)


def checkforgroup(tracks):

    findoverlappingcircles(tracks)

    return tracks
