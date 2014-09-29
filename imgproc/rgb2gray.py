#!/usr/bin/env python

from imgproc import cv2


def rgb2graytransform(frames):

    gray_frames = []

    for img in frames:
        aux_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        gray_frames.append(aux_img)

    return gray_frames