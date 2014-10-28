#!/usr/bin/env python

from detection import cv2
from detection import np


class Blob(object):

    def __init__(self):

        self.blob_img = None
        self.bound_rect = None
        self.contour = None
        self.projection = None

    def setdefault(self, blob_img, bound_rect, contour):

        self.blob_img = blob_img
        self.bound_rect = bound_rect
        self.contour = contour

        # self.projection
        self.contoursprojection()

    def contoursprojection(self):

        # Normalize blob_img
        # Binary images in OpenCV come with (0, 255) values instead
        # of (0, 1)

        blob_norm = self.blob_img / 255

        x_projection = np.add.reduce(blob_norm, 0, dtype=np.uint32)
        y_projection = np.add.reduce(blob_norm, 1, dtype=np.uint32)

        # Can be normalized
        self.projection = [y_projection, x_projection]

    def drawprojection(self, frame):

        x, y, w, h = self.bound_rect

        y_pro = self.projection[0]
        for i in range(len(y_pro)):
            cv2.line(
                frame, (x + w, y + i), (x + w + y_pro[i], y + i), (0, 0, 0), 1)

        x_pro = self.projection[1]
        for i in range(len(x_pro)):
            cv2.line(
                frame, (x + i, y + h), (x + i, y + h + x_pro[i]), (0, 0, 0), 1)

    def drawboundingrect(self, frame):

        x, y, w, h = self.bound_rect

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
