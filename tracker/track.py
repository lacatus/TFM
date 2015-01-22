#!/usr/bin/env python


class Track(object):

    """
    Track class that contains the information regarding
    the existent track paths that are currently in the
    scene. State Machine
    """

    def __init__(self):

        self.subject = None
        self.points = None  # TODO
        self.color = None  # TODO
        self.state = None
        self.state_info = None
        self.count = None
        self.count_max = None

    def delete(self):

        del self

    def setdefault(self, subject):

        self.setsubject(subject)
        self.setstate(1)
        self.state_info = {
            1: 'Locking',
            2: 'Locked',
            3: 'Missing',
            4: 'Lost'
        }
        self.count = 1
        self.count_max = 5

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

        if self.count <= -5:
            self.setstate(4)
        else:
            self.count -= 1
            self.setstate(3)

    def update(self, subject=None):  # TODO

        # TODO
        # Register track points in order to paint them

        if not subject:  # keep updating with same subject ?? <-- BIG TODO
            self.updatemisscount()
        else:
            self.setsubject(subject)
            self.updatelockcount()
