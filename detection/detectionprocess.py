#!/usr/bin/env python

from detection import blob
from detection import cv2
from detection import np
from detection import subject
#from threedgeometry import retroprojection


def contourstoblobs(bg_models):

    total_blobs = []

    for bg in bg_models:

        bin_img = bg.diff_img_copy
        bg_blobs = []

        for ii in range(len(bg.contours)):

            x, y, w, h = bg.rectangles[ii]

            b = blob.Blob()
            b.setdefault(
                bin_img[y:y + h, x:x + w],
                bg.rectangles[ii],
                bg.contours[ii])

            bg_blobs.append(b)

        total_blobs.append(bg_blobs)

    return total_blobs


def createglobalmask(total_blobs, bg_models):

    size = bg_models[0].bg_img.shape
    height = size[0]
    width = size[1]

    total_masks = []

    for bg_blobs in total_blobs:

        global_mask = np.zeros((height, width), dtype=np.uint8)

        for blob in bg_blobs:

            blob.drawglobalmask(global_mask)

        total_masks.append(
            cv2.morphologyEx(
                global_mask, 
                cv2.MORPH_CLOSE, 
                cv2.getStructuringElement(
                    cv2.MORPH_CROSS, 
                    (5, 10))))

    """
    cv2.imshow(
        "demo", 
        cv2.morphologyEx(
            global_mask, 
            cv2.MORPH_CLOSE, 
            cv2.getStructuringElement(
                cv2.MORPH_CROSS, 
                (5, 10))))
    """

    return total_masks


def globalmasktosubjects(total_masks, bg_models, cameras, frames):

    total_subjs = []

    win_width = bg_models[0].win_width
    win_height = bg_models[0].win_height

    for ii in range(len(total_masks)):

        subjs = []

        """
        # OpenCV 2.4.8
        contours, hierarchy = cv2.findContours(
            total_masks[ii], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        """
        # OpenCV 3.0.0
        _, contours, hierarchy = cv2.findContours(
            total_masks[ii], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            
        res =  cv2.bitwise_and(frames[ii], frames[ii], mask = total_masks[ii]) 

        for cont in contours:

            x, y, w, h = cv2.boundingRect(cont)
            box = [x, y, w, h]

            if w >= (win_width / 2) and h >= (win_height / 2):

                ellipse = cv2.fitEllipse(cont)
                rot_box = cv2.minAreaRect(cont)
                circle = cv2.minEnclosingCircle(cont)
                subj = subject.Subject()
                subj.setdefault(
                    total_masks[ii][y:y + h, x:x + w],
                    box, rot_box, ellipse, circle, cameras[ii], cont,
                    res[y:y + h, x:x + w])
                subjs.append(subj)

        total_subjs.append(subjs)

    return total_subjs

# TODO
"""
def retroprojectsubjects(total_cameras, total_subjects):

    for ii in range(len(total_cameras)):

        subjects = total_subjects[ii]

        for subj in subjects:

            retroprojection.retroprojectsubject(total_cameras[ii], subj)

    return total_subjects
"""


def detectionprocess(bg_models, cameras, frames):

    total_blobs = contourstoblobs(bg_models)
    total_masks = createglobalmask(total_blobs, bg_models)
    total_subjs = globalmasktosubjects(total_masks, bg_models, cameras, frames)
    #total_subjs = retroprojectsubjects(cameras, total_subjs) # TODO

    return total_blobs, total_subjs
