#!/usr/bin/env python

from tracker import association


def inittracks(len):

    tracks = []

    for cam in range(len):
        tracks.append([])

    return tracks


def associatetrackssubjects(tracks, subjects):

    new_tracks = []

    for ii in range(len(tracks)):

        track = association.associatetracksubject(tracks[ii], subjects[ii])
        new_tracks.append(track)

    return new_tracks


def trackerprocess(tracks, subjects):

    tracks = associatetrackssubjects(tracks, subjects)

    return tracks
