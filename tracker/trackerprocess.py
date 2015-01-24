#!/usr/bin/env python

from tracker import association
from tracker import group
from tracker import variables


def inittracks(len):

    tracks = []
    variables.num_tracks = 0

    for cam in range(len):
        tracks.append([])

    return tracks


def associatetrackssubjects(tracks, subjects):

    new_tracks = []

    for ii in range(len(tracks)):

        track = association.associatetracksubject(tracks[ii], subjects[ii])
        new_tracks.append(track)

    return new_tracks


def checkforgroups(tracks):

    new_tracks = []

    for ii in range(len(tracks)):

        track = group.checkforgroup(tracks[ii])
        new_tracks.append(track)

    return new_tracks


def trackerprocess(tracks, subjects):

    tracks = associatetrackssubjects(tracks, subjects)
    groups = checkforgroups(tracks)

    return tracks
