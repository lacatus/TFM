#!/usr/bin/emv python

from detection import cv2
from detection import np


class Subject(object):

    def __init__(self):

        self.bin = None
        self.box = None
        self.rot_box = None
        self.ellipse = None
        self.circle = None
        self.e = None
        self.base = None
        self.h_base = None
        self.top = None
        self.h_top = None
        self.group = None
        self.retro_base = None
        self.retro_top = None

    def setdefault(self, src, box, rot_box, ellipse, circle, camera):

        self.bin = src
        self.box = box
        self.rot_box = rot_box
        self.formatellipse(ellipse)
        self.formatcircle(circle, camera)

    def formatellipse(self, ellipse):

        (x, y), (w, h), a = ellipse
        self.ellipse = (int(x), int(y)), (int(w), int(h)), a

    def formatcircle(self, circle, camera):

        self.circle = circle
        (x, y), radius = circle

        self.e = {'x': int(x), 'y': int(y), 'r': int(radius)}

        self.getbase(camera)
        self.gettop(camera)

    def getbase(self, camera):

        x = self.e['x']
        y = self.e['y'] + self.e['r']
        self.base = (x, y)

        h = camera.video.height
        w = camera.video.width

        hx = int(h / 2 - x)
        hy = int(y - w / 2)

        self.h_base = (hx, hy)

    def gettop(self, camera):

        x = self.e['x']
        y = self.e['y'] - self.e['r']
        self.top = (x, y)

        h = camera.video.height
        w = camera.video.width

        hx = int(h / 2 - x)
        hy = int(y - w / 2)

        self.h_top = (hx, hy)

    def setretroprojection(self, db, dt):

        self.retro_base = db
        self.retro_top = dt

    def paintrotbox(self, frame):

        box = cv2.cv.BoxPoints(self.rot_box)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)

    def paintellipse(self, frame):

        cv2.ellipse(frame, self.ellipse, (255, 0, 0), 2)

    def paintcircle(self, frame):

        (x, y), radius = self.circle
        center = (int(x), int(y))
        radius = int(radius)
        cv2.circle(frame, center, radius, (0, 255, 0), 2)

    def paintbase(self, frame):

        cv2.circle(
            frame,
            self.base,
            2,
            (255, 255, 0),
            thickness=2,
            lineType=8
        )

    def painttop(self, frame):

        cv2.circle(
            frame,
            self.top,
            2,
            (255, 255, 0),
            thickness=2,
            lineType=8
        )
