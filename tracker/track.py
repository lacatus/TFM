#!/usr/bin/env python

from tracker import cv2
from tracker import np
from tracker import particlefilter as pfil
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
    - Create appareance model for Deassociating
        - Start with color model
        - Continue with parts
    - Propagation on trackmissupdate
    """

    def __init__(self):

        self.subject = None
        self.path = None
        self.path_max = None

        # new --> historico score
        self.score = None
        self.score_max = None
        self.score_mu = None
        self.score_sigma = None
        #

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
        self.pf = None

        # RGB CUBES
        self.rgb_cubes = None
        self.rgb_a = 0.05
        # ===

    def delete(self):

        del self

    def setdefault(self, subject, num):

        self.setsubject(subject)
        self.path = []
        self.path_max = 30

        # new --> historico score
        self.score = []
        self.score_max = 30

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
        self.count_min = -3
        self.num = num
        self.update = False
        self.group = False
        self.associated = []
        self.setparticles(subject)
        self.score = []
        self.score_sigma = 0
        self.score_mu = 0
        self.mature = False
        self.rgb_cubes = subject.rgb_cubes


    def setparticles(self, subject):

        self.pf = pfil.ParticleFilter()
        self.pf.setdefault(subject)

    def setgroupstate(self, state):

        self.group = state

    def associatetrack(self, track):

        self.group = True

        if track.group:
            self.associateassociatedtracks(track)
        else:
            self.associated.append(track)

    def associateassociatedtracks(self, track):  # TODO

        for ii in range(len(track.associated)):
            self.associated.append(track.associated.pop(0))

        track.setgroupstate(False)
        self.associated.append(track)

    def deassociatetrack(self):
        # better --> TODO --> BASED ON COLOR MODEL

        self.printtrack()
        print self.associated
        res = self.associated.pop(0)

        if len(self.associated) < 1:
            self.group = False

        return res

    def setsubject(self, subject):

        self.subject = subject

    def setstate(self, state):

        self.state = state

    def updatelockcount(self, associated=True):

        if self.count >= self.count_max:
            self.count = self.count_max  # + 2 # little extra margin
            self.setstate(2)
            self.mature = True
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

    def updatescore(self, score):
        if len(self.score) > self.score_max:
            self.score.pop(0)

        self.score.append(score)
        self.score_sigma = np.std(self.score)
        self.score_mu = np.mean(self.score)

    def updateassociatedpath(self, subject):

        for a in self.associated:
            a.updatepath(subject, False)

    def updatergbcubes(self, subject):
        a = self.rgb_a
        for ii in range(3):
            self.rgb_cubes[ii] = a*subject.rgb_cubes[ii] + (1-a)*self.rgb_cubes[ii]

    def updatetrack(self, subject=None, score=None):

        self.update = False

        if not subject:  # keep updating with same subject ?? <-- propagation
            self.updatemisscount()
        else:
            self.update = True
            self.setsubject(subject)
            self.updatelockcount()
            self.updatepath(subject)
            self.pf.updatedet(subject)
            self.updatescore(score)
            self.updatergbcubes(subject)

    def calculatesubjectdistance(self, subject, threshold):  # Future change

        (xt, yt), radius = self.subject.circle
        (xs, ys), radius = subject.circle

        loss = int(np.sqrt(np.power(xt - xs, 2) + np.power(yt - ys, 2)))
        print 'Deassociate loss'
        print loss
        if loss <= threshold:
            return True
        else:
            return False

    def paintpath(self, frame):  # <-- Paint subject with state color

        path = self.path
        color = self.color

        for p in path:
            (x, y), radius = p
            center = (int(x), int(y))
            cv2.circle(frame, center, 2, color, 2)

    def paintsubject(self, frame):

        if self.group:
            self.subject.paintrotboxcolor(frame, (255, 255, 255))
        else:
            self.subject.paintrotboxcolor(frame, self.state_color[self.state])

    def paintnum(self, frame):

        cv2.putText(frame, str(self.num), self.subject.top,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    def printtrack(self):

        (x, y), (h, w), a = self.subject.rot_box

        print 'Track attributes NUM: %s' % self.num
        # print 'Path: %s' % self.path
        print 'State: %s' % self.state_info[self.state]
        print 'Count: %s' % self.count
        print 'Subject: %s,%s,%s,%s' % (x, y, h, w)

    def printassociatedtrack(self):

        if self.group:
            print 'Associated tracks:'

            for a in self.associated:
                a.printtrack()

            print '##'

    def painttrack(self, frame):

        #self.pf.paintp(frame, self.color)
        self.pf.paintbestp(frame, self.num, self.color)
        self.paintpath(frame)
        #self.paintnum(frame)
        #self.printtrack()
        #self.printassociatedtrack()
        #self.paintsubject(frame)
        """
        if self.update:  # <-- take a look, 2 subjects do not associate at all
            self.paintsubject(frame)
        """
