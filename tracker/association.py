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

    threshold = 50

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


def assignsubjecttoexistingtrack(tr, sub):
    



def trackupdate(tr, sub, res):

    """
    TODO
    - [ ] update de tracks
        - [ ] tracks existentes asociadas
        - [ ] tracks existentes no asociadas
        - [ ] creacion de nuevas tracks
    - [ ] realizar metodo de pintar tracks
    """

    new_track = []

    # Update succesful assoiations
    for r in res:
        y, x = r
        assignsubjecttoexistingtrack(tr[y], sub[x])

    #return new_track
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
