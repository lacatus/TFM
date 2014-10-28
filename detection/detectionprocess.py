#!/usr/bin/env python

from detection import blob


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


def detectionprocess(bg_models):

    blobs = contourstoblobs(bg_models)

    return blobs
