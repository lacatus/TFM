#!/usr/bin/env python

from tracking import cv2


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
        self.projection = []

    def contoursprojection(self):

        # Normalize blob_img
        # Binary images in OpenCV come with (0, 255) values instead
        # of (0, 1)
        blob_norm = blob_img / 255

        x_projection = cv2.reduce(blob_norm, 0, cv2.CV_REDUCE_SUM)
        y_projection = cv2.reduce(blob_norm, 1, cv2.CV_REDUCE_SUM)

        self.projection = [y_projection, x_projection]

    def drawprojection(self, frame):

        x, y, w, h = self.bound_rect

        y_pro = self.projection[0]

        for i in range(len(y_pro)):

            cv2.line(
                img, (x + w, y + i), (x + w + y_pro[i], y + i), (0, 0, 0), 1)

        x_pro = self.projection[1]

        for i in range(len(x_pro)):

            cv2.line(
                img, (x + i, y + h), (x + i, y + h + x_pro[i]), (0, 0, 0), 1)
