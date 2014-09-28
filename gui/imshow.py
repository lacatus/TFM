#!/usr/bin/env python

from gui import cv2
from gui import np
from gui import variables


def showallimg(camera_frames):

    s = len(camera_frames)

    height, width, depth = camera_frames[0].shape

    if s >= 2:
        num_rows = ((s - 1) / 2) + 1

        window_width = width * 2
        window_height = height * num_rows

    else:
        window_width = width
        window_height = height

    all_img = np.zeros((window_height, window_width, 3), np.uint8)

    rows = 1
    cols = 1
    aux = 0

    for frame in camera_frames:

        all_img[height * (rows - 1):height * rows,
                width * (cols - 1):width * cols] = frame

        aux += 1

        if aux % 2 is 0:
            rows += 1
            cols = 1
        else:
            cols += 1

    cv2.imshow(variables.app_window_name, all_img)
    cv2.waitKey(1)
