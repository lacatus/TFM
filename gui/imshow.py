#!/usr/bin/env python

from gui import cv2
from gui import np
from gui import variables


def paintcontours(frames, bg_models):

    contour_frames = []

    for ii in range(len(frames)):

        image = frames[ii].copy()

        cv2.drawContours(image, bg_models[ii].contours, -1, (0, 255, 0), 5)

        contour_frames.append(image)

    return contour_frames


def paintblobs(frames, total_blobs):

    for ii in range(len(total_blobs)):

        for blob in total_blobs[ii]:

            blob.drawboundingrect(frames[ii])
            blob.drawprojection(frames[ii])
            blob.drawsmoothprojection(frames[ii])
            blob.drawmeanprojection(frames[ii])

    return frames


def paintmasks(frames, total_blobs):

    for ii in range(len(total_blobs)):

        for blob in total_blobs[ii]:

            blob.drawmask(frames[ii])

    return frames


def paintellipses(frames, total_ellipses):

    for ii in range(len(total_ellipses)):

        for ellipse in total_ellipses[ii]:

            cv2.ellipse(
                frames[ii], ellipse, (0, 255, 0), 2)

    return frames


def showallimg(camera_frames):

    s = len(camera_frames)

    size = camera_frames[0].shape

    height = size[0]
    width = size[1]

    if s >= 2:
        num_rows = ((s - 1) / 2) + 1

        window_width = width * 2
        window_height = height * num_rows

    else:
        window_width = width
        window_height = height

    # In case we want to show img different than rgb
    if len(size) < 3:
        all_img = np.zeros((window_height, window_width), np.uint8)

    else:
        all_img = np.zeros((window_height, window_width, 3), np.uint8)

    rows = 1
    cols = 1
    aux = 0

    for frame in camera_frames:

        all_img[height * (rows - 1):height * rows,
                width * (cols - 1):width * cols] = frame.astype(np.uint8)

        aux += 1

        if aux % 2 is 0:
            rows += 1
            cols = 1
        else:
            cols += 1

    cv2.imshow(variables.app_window_name, all_img)
    cv2.waitKey(1)
