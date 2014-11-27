#!/usr/bin/emv python

from detection import cv2
from detection import np


class Subject(object):

    def __init__(self):

        self.bin = None
        self.box = None
        self.rot_box = None
        self.ellipse = None
        self.e = None
        self.base = None
        self.top = None
        self.group = None
        self.retro_base = None
        self.retro_top = None

    def setdefault(self, src, box, rot_box, ellipse):

        self.bin = src
        self.box = box
        self.rot_box = rot_box
        self.formatellipse(ellipse)

    def formatellipse(self, ellipse):

        (x, y), (w, h), a = ellipse
        self.ellipse = (int(x), int(y)), (int(w), int(h)), a
        self.e = {
            'x': int(x),
            'y': int(y),
            'w': int(w),
            'h': int(h),
            'a': a
        }
        self.getbase()
        self.gettop()

    def getbase(self):

        x = self.e['x']
        y = self.e['y'] + int(self.e['h'] / 2)
        self.base = (x, y)

    def gettop(self):

        x = self.e['x']
        y = self.e['y'] - int(self.e['h'] / 2)
        self.top = (x, y)

    def setretroprojection(self, db, dt):

        self.retro_base = db
        self.retro_top = dt

    def paintrotbox(self, frame):

        box = cv2.cv.BoxPoints(self.rot_box)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)

    def paintellipse(self, frame):

        cv2.ellipse(frame, self.ellipse, (0, 255, 0), 2)

    def paintbase(self, frame):

        cv2.circle(
            frame,
            self.base,
            2,
            (255, 0, 0),
            thickness=2,
            lineType=8
        )

    def painttop(self, frame):

        cv2.circle(
            frame,
            self.top,
            2,
            (255, 0, 0),
            thickness=2,
            lineType=8
        )
