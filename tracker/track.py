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
        self.setstate(0)
        self.state_info = {
            0: 'Init',
            1: 'Locking',
            2: 'Locked',
            3: 'Missing',
            4: 'Lost'
        }
        self.count = 0
        self.count_max = 5

    def setsubject(self, subject):

        self.subject = subject

    def setstate(self, state):

        self.state = state

    def updatelockcount(self):

        self.count += 1

        if self.count > self.count_max:
            self.setstate(2)

    def updatemisscount(self):

        self.count -= 1

        if self.miss_count <= 0:
            self.setstate(4)

    def update(self, subject=None):  # TODO

        if not subject:
            pass
        else:
            self.setsubject(subject)
