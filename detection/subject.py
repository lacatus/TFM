#!/usr/bin/emv python

from detection import cv2
from detection import np


class Subject(object):

    def __init__(self):

        self.bin = None
        self.box = None
        self.rot_box = None
        self.group = None

        # RELATIONATE WITH RETROPROJECTION

    def setdefault(self, src, box, rot_box):

        self.box = box
        self.rot_box = rot_box
        # self.bin
        self.setbin(src)

    def setbin(self, src):

        x, y, w, h = self.box
        self.bin = src[y:y + h, x:x + w]

    def paintrotbox(self, frame):

        cv2.ellipse(frame, self.rot_box, (0, 255, 0), 2)
