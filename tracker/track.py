#!/usr/bin/env python


class Track(object):

    """
    Track class that contains the information regarding
    the existent track paths that are currently in the
    scene. State Machine
    """

    def __init__(self):

        self.subject = None
        self.state = None
        self.state_info = None
        self.lock_count = None
        sefl.lock_count_max = None
        self.miss_count = None
        self.miss_count_max = Nonw

    def delete(self):

        del self

    def setdefault(self, subject):

        self.setsubject(subject)
        self.setstate(0)
        self.state_info = [
            0: 'Init',
            1: 'Locking',
            2: 'Locked',
            3: 'Missing',
            4: 'Lost'
        ]
        self.lock_count = 0
        self.lock_count_max = 5
        self.miss_count = 0
        self.miss_count_max = 10

    def setsubject(self, subject):

        self.subject = subject

    def setstate(self, state):

        self.state = state

    def updatelockcount(self, update):

        if update is 0:
            self.lock_count = 0
        else:
            self.setstate(1)
            self.lock_count += 1

        if self.lock_count > self.lock_count_max:
            self.updatelockcount(0)
            self.setstate(2)

    def updatemisscount(self, update):

        if update is 0:
            self.miss_count = 0
        else:
            self.setstate(3)
            self.miss_count += 1

        if self.miss_count > self.miss_count_max:
            self.updatemisscount(0)
            self.setstate(4)
