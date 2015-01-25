#!/usr/bin/env python

from tracker import np
from tracker import track


def gettrackcircles(tracks):

    circles = []

    for t in tracks:

        circles.append(t.subject.circle)

    return circles


def checkoverlap(x1, y1, r1, x2, y2, r2):

    dxy = np.sqrt(np.pow(y2 - y1, 2) + np.pow(x2 - x1, 2))
    dr = np.pow(r2 + r1, 2)

    if dxy <= dr:
        return True
    else:
        return False


def checkbelonging(index, jj):

    for ii in range(len(index)):
        a, b = index[ii]
        if b == jj:
            return a


def getcircleintersections(circles, tracks):

    groups = []
    groups_index = []

    for jj in range(len(circles)):
        (x1, y1), r1 = circles[jj]

        res = checkbelonging(groups_index, jj)

        if res:
            gtr = groups[res]
        else:
            gtr = track.TrackGroup()
            groups.append(gtr)
            gtr.appendnewtrack(track[jj])
            groups_index.append([len(groups_index), jj])

        for ii in range(len(circles)):
            (x2, y2), r2 = circles[ii]

            if jj >= ii:
                continue

            if checkoverlap(x1, y1, r1, x2, y2, r2):
                gtr.appendnewtrack(track[ii])
                groups_index.append([len(groups_index), ii])

    return groups


def findoverlappingcircles(tracks):

    """
    TODO
    ----
    Encontrar superposiciones de los circulos de los sujetos
        - Posible optimizacion cython n2
        - Basado en intersecciones de circulos (posible solucion)
        - Dependiendo del area que se superponen, consideraremos grupo o no
    Nueva clase grupo contenedora de tracks
        - Pensar estrategia a seguir para combinar tracks y grupo de tracks
            - Groups --> clase padre de --> tracks
            - Aunque groups solo tenga un track, este hereda y se define que
              group no es un group
    """

    circles = gettrackcircles(tracks)
    intersections = getcircleintersections(circles, tracks)

    pass


def checkforgroup(tracks):

    findoverlappingcircles(tracks)

    return tracks
