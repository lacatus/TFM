#!/usr/bin/env python

from gui import cv2
from gui import np
from gui import variables


def init_imshow():
    while 1:
        options = {
            1: 'RGB frames',
            2: 'Grayscale frames',
            3: 'Background models',
            4: 'Binary subtraction',
            5: 'Window scan',
            6: 'Background difference'
        }

        options_str = \
            '\nImshow options:\n' \
            '   1. %s\n' \
            '   2. %s\n' \
            '   3. %s\n' \
            '   4. %s\n' \
            '   5. %s\n' \
            '   6. %s\n' % \
            (options[1], options[2],
            options[3], options[4],
            options[5], options[6])

        print options_str

        ans = raw_input('Please select one option: ')

        if 0 < int(ans) <= len(options):
            return int(ans)

        else:
            print '\nPlease select a valid option'


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