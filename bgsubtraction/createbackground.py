#!/usr/bin/env python

"""
This script contains the necessary code in order to
generate the background reference images for each video of
the datasets.

This script does not participates in the main routine
of the project, but it is necesarry in order to achieve
better results on the process of background subtraction
"""

import cv2
import numpy as np
import sys


def createbackgroundimg(src_vid, dst_img, frame_count):

    # Background parameters
    counter = 1
    alpha = 0.9
    beta = 0.1

    # Read video
    data_vid = cv2.VideoCapture(src_vid)

    # Create background image
    ret, frame = data_vid.read()

    size = frame.shape
    height = size[0]
    width = size[1]
    channels = size[2]

    bg = np.zeros((height, width, channels), dtype=np.uint8)

    # Loop though video
    while True:

        # Get each frame
        ret, frame = data_vid.read()

        # If not retrieved frame, break
        if not ret:
            break

        if frame_count is counter:

            bg = cv2.addWeighted(bg, alpha, frame, beta, 0)
            counter = 1

        else:
            counter += 1

    # Save image
    cv2.imwrite(dst_img, bg)


def alldatasetsbackgroundimg():

    project_dir = '/home/blg/TFM'

    # oxtown
    print 'Creating background imgs for oxtown ...'

    print 'Camera 1 ...'

    src_vid = \
        '%s/data/oxtown/video/camera001.avi' % project_dir
    dst_img = \
        '%s/data/oxtown/background/camera001.jpg' % project_dir

    createbackgroundimg(src_vid, dst_img, 25)

    """
    # pets09 - crop01
    print 'Creating background img for ewap - 1.avi ...' 
    src_vid = '%s/data/ewap/videos/1.avi' % project_dir
    dst_img = '%s/data/ewap/background/background.jpg' % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    
    # pets09 - crop01
    print 'Creating background img for pets09 - crop01 ...' 
    src_vid = '%s/data/pets09/icae/videos/crop_1.avi' % project_dir
    dst_img = '%s/data/pets09/icae/background/background.jpg' % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    # caviar 
    print 'Creating background img for caviar ...' 
    src_vid = '%s/data/caviar/videos/Meet_WalkSplit.avi' % project_dir
    dst_img = '%s/data/caviar/background/background.jpg' % project_dir

    createbackgroundimg(src_vid, dst_img, 30)

    # grazptz1
    print 'Creating background imgs for grazptz1 ...'

    print 'Camera 1 ...'

    src_vid = '%s/data/grazptz/set1/videos/cam-131.avi' % project_dir
    dst_img = '%s/data/grazptz/set1/background/cam-131.jpg' % project_dir

    createbackgroundimg(src_vid, dst_img, 30)

    print 'Camera 2 ...'

    src_vid = '%s/data/grazptz/set1/videos/cam-132.avi' % project_dir
    dst_img = '%s/data/grazptz/set1/background/cam-132.jpg' % project_dir

    createbackgroundimg(src_vid, dst_img, 30)

    print 'Camera 3 ...'

    src_vid = '%s/data/grazptz/set1/videos/cam-133.avi' % project_dir
    dst_img = '%s/data/grazptz/set1/background/cam-133.jpg' % project_dir

    createbackgroundimg(src_vid, dst_img, 30)

    # graztpz2
    print 'Creating background imgs for grazptz2 ...'

    print 'Camera 1 ...'

    src_vid = '%s/data/grazptz/set2/videos/cam-131.avi' % project_dir
    dst_img = '%s/data/grazptz/set2/background/cam-131.jpg' % project_dir

    createbackgroundimg(src_vid, dst_img, 30)

    print 'Camera 2 ...'

    src_vid = '%s/data/grazptz/set2/videos/cam-132.avi' % project_dir
    dst_img = '%s/data/grazptz/set2/background/cam-132.jpg' % project_dir

    createbackgroundimg(src_vid, dst_img, 30)

    print 'Camera 3 ...'

    src_vid = '%s/data/grazptz/set2/videos/cam-133.avi' % project_dir
    dst_img = '%s/data/grazptz/set2/background/cam-133.jpg' % project_dir

    createbackgroundimg(src_vid, dst_img, 30)

    print 'Camera 4 ...'

    src_vid = '%s/data/grazptz/set2/videos/cam-134.avi' % project_dir
    dst_img = '%s/data/grazptz/set2/background/cam-134.jpg' % project_dir

    createbackgroundimg(src_vid, dst_img, 30)

    # pets091
    print 'Creating background imgs for pets091 ...'

    print 'Camera 1 ...'

    src_vid = \
        '%s/data/pets09/s0/citycenter/time_12_34/camera001.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/citycenter/time_12_34/background/camera001.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 2 ...'

    src_vid = \
        '%s/data/pets09/s0/citycenter/time_12_34/camera002.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/citycenter/time_12_34/background/camera002.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 3 ...'

    src_vid = \
        '%s/data/pets09/s0/citycenter/time_12_34/camera003.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/citycenter/time_12_34/background/camera003.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 4 ...'

    src_vid = \
        '%s/data/pets09/s0/citycenter/time_12_34/camera004.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/citycenter/time_12_34/background/camera004.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    # pets092
    print 'Creating background imgs for pets092 ...'

    print 'Camera 1 ...'

    src_vid = \
        '%s/data/pets09/s0/citycenter/time_14_55/camera001.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/citycenter/time_14_55/background/camera001.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 2 ...'

    src_vid = \
        '%s/data/pets09/s0/citycenter/time_14_55/camera002.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/citycenter/time_14_55/background/camera002.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 3 ...'

    src_vid = \
        '%s/data/pets09/s0/citycenter/time_14_55/camera003.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/citycenter/time_14_55/background/camera003.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    # pets093
    print 'Creating background imgs for pets093 ...'

    print 'Camera 1 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_13_57/camera001.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_13_57/background/camera001.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 2 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_13_57/camera002.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_13_57/background/camera002.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 3 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_13_57/camera003.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_13_57/background/camera003.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 4 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_13_57/camera004.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_13_57/background/camera004.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    # pets094
    print 'Creating background imgs for pets094 ...'

    print 'Camera 1 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_13_59/camera001.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_13_59/background/camera001.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 2 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_13_59/camera002.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_13_59/background/camera002.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 3 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_13_59/camera003.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_13_59/background/camera003.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 4 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_13_59/camera004.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_13_59/background/camera004.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    # pets095
    print 'Creating background imgs for pets095 ...'

    print 'Camera 1 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_14_03/camera001.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_14_03/background/camera001.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 2 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_14_03/camera002.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_14_03/background/camera002.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 3 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_14_03/camera003.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_14_03/background/camera003.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 4 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_14_03/camera004.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_14_03/background/camera004.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    # pets096
    print 'Creating background imgs for pets096 ...'

    print 'Camera 1 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_14_06/camera001.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_14_06/background/camera001.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 2 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_14_06/camera002.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_14_06/background/camera002.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 3 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_14_06/camera003.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_14_06/background/camera003.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 4 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_14_06/camera004.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_14_06/background/camera004.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    # pets097
    print 'Creating background imgs for pets097 ...'

    print 'Camera 1 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_14_29/camera001.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_14_29/background/camera001.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 2 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_14_29/camera002.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_14_29/background/camera002.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 3 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_14_29/camera003.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_14_29/background/camera003.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 4 ...'

    src_vid = \
        '%s/data/pets09/s0/regularflow/time_14_29/camera004.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s0/regularflow/time_14_29/background/camera004.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    # pets098
    print 'Creating background imgs for pets098 ...'

    print 'Camera 1 ...'

    src_vid = \
        '%s/data/pets09/s1/l1/time_13_57/camera001.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s1/l1/time_13_57/background/camera001.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 2 ...'

    src_vid = \
        '%s/data/pets09/s1/l1/time_13_57/camera002.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s1/l1/time_13_57/background/camera002.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 3 ...'

    src_vid = \
        '%s/data/pets09/s1/l1/time_13_57/camera003.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s1/l1/time_13_57/background/camera003.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 4 ...'

    src_vid = \
        '%s/data/pets09/s1/l1/time_13_57/camera004.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s1/l1/time_13_57/background/camera004.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    # pets099
    print 'Creating background imgs for pets099 ...'

    print 'Camera 1 ...'

    src_vid = \
        '%s/data/pets09/s1/l1/time_13_59/camera001.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s1/l1/time_13_59/background/camera001.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 2 ...'

    src_vid = \
        '%s/data/pets09/s1/l1/time_13_59/camera002.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s1/l1/time_13_59/background/camera002.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 3 ...'

    src_vid = \
        '%s/data/pets09/s1/l1/time_13_59/camera003.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s1/l1/time_13_59/background/camera003.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    print 'Camera 4 ...'

    src_vid = \
        '%s/data/pets09/s1/l1/time_13_59/camera004.avi' % project_dir
    dst_img = \
        '%s/data/pets09/s1/l1/time_13_59/background/camera004.jpg' \
        % project_dir

    createbackgroundimg(src_vid, dst_img, 10)

    # oxtown
    print 'Creating background imgs for oxtown ...'

    print 'Camera 1 ...'

    src_vid = \
        '%s/data/oxtown/video/camera001.avi' % project_dir
    dst_img = \
        '%s/data/oxtown/background/camera001.jpg' % project_dir

    createbackgroundimg(src_vid, dst_img, 25)
    """

alldatasetsbackgroundimg()
