#!/usr/bin/env python

from tracker import cv2
from tracker import rnd


class Track(object):

    """
    Track class that contains the information regarding
    the existent track paths that are currently in the
    scene. State Machine
    """

    """
    TODO
    ----
    - Associate tracks to track
        - Associate 1:N
        - Deassociate 1:N
        - Associate with children N:N
        - Deassociate with children N:N
    - Create appareance model for Deassociating
        - Start with color model
        - Continue with parts
    """

    def __init__(self):

        self.subject = None
        self.path = None
        self.path_max = None
        self.color = None
        self.state = None
        self.state_info = None
        self.state_color = None
        self.count = None
        self.count_max = None
        self.count_min = None
        self.num = None
        self.update = None
        self.group = None
        self.associated = None

    def delete(self):

        del self

    def setdefault(self, subject, num):

        self.setsubject(subject)
        self.path = []
        self.path_max = 30
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
        self.state_color = {
            1: (0, 128, 255),
            2: (0, 255, 0),
            3: (0, 255, 255),
            4: (0, 0, 255)
        }
        self.count = 1
        self.count_max = 5
        self.count_min = -5
        self.num = num
        self.update = assFalse
        self.group = False
        self.associated = []

    def associatetrack(self, track):

        self.group = True
        self.associated.append(track)

    def deassociatetrack(self):
        pass  # TODO

    def setsubject(self, subject):

        self.subject = subject

    def setstate(self, state):

        self.state = state

    def updatelockcount(self, associated=True):

        if self.count >= self.count_max:
            self.setstate(2)
        else:
            self.count += 1
            self.setstate(1)

        if self.group and associated:
            self.updateassociatedlockcount()

    def updateassociatedlockcount(self):

        for a in self.associated:
            a.updatelockcount(False)

    def updatemisscount(self, associated=True):

        if self.count <= self.count_min:
            self.setstate(4)
        else:
            self.count -= 1

            if self.count <= 0:
                self.setstate(3)

        if self.group and associated:
            self.updateassociatedmisscount()

    def updateassociatedmisscount(self):

        for a in self.associated:
            a.updatemisscount(False)

    def updatepath(self, subject, associated=True):

        if len(self.path) > self.path_max:
            self.path.pop(0)

        self.path.append(subject.circle)

        if self.group and associated:
            self.updateassociatedpath(subject)

    def updateassociatedpath(self, subject):

        for a in self.associated:
            a.updatepath(subject, False)

    def updatetrack(self, subject=None):  # TODO

        self.update = False

        if not subject:  # keep updating with same subject ?? <-- propagation
            self.updatemisscount()
        else:
            self.update = True
            self.setsubject(subject)
            self.updatelockcount()
            self.updatepath(subject)

    def paintpath(self, frame):  # <-- Paint subject with state color

        path = self.path
        color = self.color

        for p in path:
            (x, y), radius = p
            center = (int(x), int(y))
            cv2.circle(frame, center, 2, color, 2)

    def paintsubject(self, frame):

        self.subject.paintrotboxcolor(frame, self.state_color[self.state])

    def paintnum(self, frame):

        cv2.putText(frame, str(self.num), self.subject.top,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    def painttrack(self, frame):

        self.paintpath(frame)
        self.paintnum(frame)
        #self.printtrack()

        if self.update:
            self.paintsubject(frame)

    def printtrack(self):

        print 'Track attributes NUM: %s' % self.num
        # print 'Path: %s' % self.path
        # print 'State: %s' % self.state_info[self.state]
        # print 'Count: %s' % self.count
