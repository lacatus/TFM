#!/usr/bin/env python

from detection import blob
from detection import cv2
from detection import np


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

        total_masks.append(global_mask)

    return total_masks


def detectionprocess(bg_models):

    blobs = contourstoblobs(bg_models)
    masks = createglobalmask(blobs, bg_models)

    return blobs, masks
