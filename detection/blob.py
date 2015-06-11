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
        self.mask = None

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
        # self.mask
        self.__applymeanthreshold(blob_img)
        # peta con grandes grupos
        # self.__applymaskmorphologicaloperation()

    def __contoursprojection(self):

        # Normalize blob_img
        # Binary images in OpenCV come with (0, 255) values instead
        # of (0, 1)

        blob_norm = self.blob_img / 255

        x_proj = np.add.reduce(blob_norm, 0, dtype=np.uint8)
        y_proj = np.add.reduce(blob_norm, 1, dtype=np.uint8)

        """
        # OpenCV 2.4.8
        x_norm_proj = cv2.normalize(
            x_proj, alpha=1, beta=255, norm_type=cv2.NORM_MINMAX)
        y_norm_proj = cv2.normalize(
            y_proj, alpha=1, beta=255, norm_type=cv2.NORM_MINMAX)
        """
        # OpenCV 3.0.0
        x_norm_proj = None
        y_norm_proj = None
        cv2.normalize(x_proj, x_norm_proj,
            alpha=1, beta=255, norm_type=cv2.NORM_MINMAX)
        cv2.normalize(y_proj, y_norm_proj,
            alpha=1, beta=255, norm_type=cv2.NORM_MINMAX)

        self.projection = [
            np.add.reduce(blob_norm, 1, dtype=np.uint8),
            np.add.reduce(blob_norm, 0, dtype=np.uint8)]

    def __smoothprojection(self):

        # (1,15) --> but could be anything
        self.smooth_projection = [
            cv2.GaussianBlur(self.projection[0], (1, 15), 0),
            cv2.GaussianBlur(self.projection[1], (1, 15), 0)]

    def __meanprojection(self):

        """
        self.mean = [
            np.mean(self.smooth_projection[0]).astype(np.uint8),
            np.mean(self.smooth_projection[1]).astype(np.uint8)]
        """
        self.mean = [
            0,
            np.mean(self.smooth_projection[1]).astype(np.uint8)]

    def __applymeanthreshold(self, blob_img):

        size = blob_img.shape
        height = size[0]
        width = size[1]

        mask = np.zeros((height, width), dtype=np.uint8)

        smooth_projection_x = self.smooth_projection[0]
        mean_x = int(self.mean[0] / 4)
        smooth_projection_y = self.smooth_projection[1]
        mean_y = int(self.mean[1] / 3)

        # Mask in X
        for ii in xrange(0, height - 1, 1):

            if(smooth_projection_x[ii] >= mean_x):
                mask[ii, :] = 255

        # Mask in Y
        for jj in xrange(0, width - 1, 1):

            if(smooth_projection_y[jj] >= mean_y):
                mask[:, jj] = 255

        # By now only mask in y projection
        self.mask = cv2.bitwise_and(blob_img, blob_img, mask=mask)

    def __applymaskmorphologicaloperation(self):

        x, y, w, h = self.bound_rect

        # TODO --> print self.mean mean_x mean_y kernel
        col = int(h/10)
        row = int(w/10)

        # in case that kernel is 0
        if col is 0:
            col = 1
        if row is 0:
            row = 1

        mask = self.mask
        kernel = np.ones((col, row), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
        self.mask = cv2.erode(mask, kernel, iterations=1)

    def drawglobalmask(self, global_mask):

        x, y, w, h = self.bound_rect

        global_mask[y:y + h, x:x + w] = cv2.add(
            global_mask[y:y + h, x:x + w], self.mask)

        return global_mask

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

        x_mean = int((self.mean[0] * 2) / 3)
        y_mean = int(self.mean[1] / 2)

        for i in range(h):
            cv2.circle(frame, (x + w + x_mean, y + i), 1, (255, 255, 255))

        for j in range(w):
            cv2.circle(frame, (x + j, y + h + y_mean), 1, (255, 255, 255))

    def drawboundingrect(self, frame):

        x, y, w, h = self.bound_rect

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    def drawmask(self, frame):

        # Create colored mask for visualization
        x, y, w, h = self.bound_rect

        mask_color = np.zeros((h, w, 3), dtype=np.uint8)
        mask_color[:, :, 1] = 255  # Assign blue color to created colored mask
        mask_color = cv2.bitwise_and(mask_color, mask_color, mask=self.mask)

        frame[y:y + h, x:x + w] = cv2.add(frame[y:y + h, x:x + w], mask_color)
