#!/usr/bin/env python

from detection import cv2
from detection import np


class Blob(object):

    def __init__(self):

        self.blob_img = None
        self.bound_rect = None
        self.contour = None
        self.projection = None
        self.smooth_projection = None
        self.mean = None

    def setdefault(self, blob_img, bound_rect, contour):

        self.blob_img = blob_img
        self.bound_rect = bound_rect
        self.contour = contour

        # self.projection
        self.__contoursprojection()
        # self.smooth_projection
        self.__smoothprojection()
        # self.median
        self.__meanprojection()

    def __contoursprojection(self):

        # Normalize blob_img
        # Binary images in OpenCV come with (0, 255) values instead
        # of (0, 1)

        blob_norm = self.blob_img / 255

        x_proj = np.add.reduce(blob_norm, 0, dtype=np.uint8)
        y_proj = np.add.reduce(blob_norm, 1, dtype=np.uint8)

        x_norm_proj = cv2.normalize(
            x_proj, alpha=1, beta=255, norm_type=cv2.NORM_MINMAX)
        y_norm_proj = cv2.normalize(
            y_proj, alpha=1, beta=255, norm_type=cv2.NORM_MINMAX)

        self.projection = [
            np.add.reduce(blob_norm, 1, dtype=np.uint8),
            np.add.reduce(blob_norm, 0, dtype=np.uint8)]

    def __smoothprojection(self):

        # (1,15) --> but could be anything
        self.smooth_projection = [
            cv2.GaussianBlur(self.projection[0], (1, 15), 0),
            cv2.GaussianBlur(self.projection[1], (1, 15), 0)]

    def __meanprojection(self):

        self.mean = [
            np.mean(self.smooth_projection[0]).astype(np.uint8),
            np.mean(self.smooth_projection[1]).astype(np.uint8)]

    def drawprojection(self, frame):

        x, y, w, h = self.bound_rect

        y_pro = self.projection[0]
        for i in range(len(y_pro)):
            cv2.line(
                frame, (x + w, y + i), (x + w + y_pro[i], y + i), (0, 0, 0), 1)

        x_pro = self.projection[1]
        for j in range(len(x_pro)):
            cv2.line(
                frame, (x + j, y + h), (x + j, y + h + x_pro[j]), (0, 0, 0), 1)

    def drawsmoothprojection(self, frame):

        x, y, w, h = self.bound_rect

        y_pro = self.smooth_projection[0]
        for i in range(len(y_pro)):
            cv2.circle(frame, (x + w + y_pro[i], y + i), 1, (0, 255, 0))

        x_pro = self.smooth_projection[1]
        for j in range(len(x_pro)):
            cv2.circle(frame, (x + j, y + h + x_pro[j]), 1, (0, 255, 0))

    def drawmeanprojection(self, frame):

        x, y, w, h = self.bound_rect

        y_mean = self.mean[0]
        for i in range(h):
            cv2.circle(frame, (x + w + y_mean, y + i), 1, (255, 255, 255))

        x_mean = self.mean[1]
        for j in range(w):
            cv2.circle(frame, (x + j, y + h + x_mean), 1, (255, 255, 255))

    def drawboundingrect(self, frame):

        x, y, w, h = self.bound_rect

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
