#!/usr/bin/env python

from tracker import cv2
from tracker import rnd


class Track(object):

    """
    Track class that contains the information regarding
    the existent track paths that are currently in the
    scene. State Machine
    """

    def __init__(self):

        self.subject = None
        self.path = None
        self.color = None
        self.state = None
        self.state_info = None
        self.count = None
        self.count_max = None
        self.count_min = None

    def delete(self):

        del self

    def setdefault(self, subject):

        self.setsubject(subject)
        self.path = []
        self.updatepath(subject)
        self.color = (
            rnd.randrange(0, 255),
            rnd.randrange(0, 255),
            rnd.randrange(0, 255)
        )
        self.setstate(1)
        self.state_info = {
            1: 'Locking',
            2: 'Locked',
            3: 'Missing',
            4: 'Lost'
        }
        self.count = 1
        self.count_max = 5
        self.count_min = -5

    def setsubject(self, subject):

        self.subject = subject

    def setstate(self, state):

        self.state = state

    def updatelockcount(self):

        if self.count > self.count_max:
            self.setstate(2)
        else:
            self.count += 1
            self.setstate(1)

    def updatemisscount(self):

        if self.count <= self.count_min:
            self.setstate(4)
        else:
            self.count -= 1
            self.setstate(3)

    def updatepath(self, subject):

        self.path.append(subject.circle)

    def paintpath(self, frame): 

        path = self.path
        color = self.color

        for p in path:
            (x, y), radius = p
            center = (int(x), int(y))
            cv2.circle(frame, center, 2, color, 2)

    def printtrack(self):

        print 'Track attributes'
        print 'Path: %s' % self.path
        print 'Color: %s' % str(self.color)
        print 'State: %s' % self.state_info[self.state]
        print 'Count: %s' % self.count

    def update(self, subject=None):  # TODO 

        if not subject:  # keep updating with same subject ?? <-- propagation
            self.updatemisscount()
        else:
            self.setsubject(subject)
            self.updatelockcount()
            self.updatepath(subject)
