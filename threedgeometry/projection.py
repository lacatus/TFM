#!/usr/bin/env python

from threedgeometry import cv2
from threedgeometry import np


def draw(img, c, p1, p2, p3):

    """
    img = cv2.line(img, p1, p2, (255, 0, 0), thickness=1)
    img = cv2.line(img, p2, p3, (0, 255, 0), thickness=1)
    img = cv2.line(img, p3, p1, (0, 0, 255), thickness=1)
    """

    cv2.circle(img, c, 2, (255, 255, 255), thickness=10, lineType=8)
    cv2.circle(img, p1, 2, (255, 0, 0), thickness=10, lineType=8)
    cv2.circle(img, p2, 2, (0, 255, 0), thickness=10, lineType=8)
    cv2.circle(img, p3, 2, (0, 0, 255), thickness=10, lineType=8)
    cv2.line(img, c, p1, (255, 0, 0), thickness=10)
    cv2.line(img, c, p2, (0, 255, 0), thickness=10)
    cv2.line(img, c, p3, (0, 0, 255), thickness=10)
    return img


def projectaxes(frame, camera):

    a1 = np.float32([[3, 0, 0]])
    a2 = np.float32([[0, 3, 0]])
    a3 = np.float32([[0, 0, 3]])
    c0 = np.float32([[0, 0, 0]])

    ap1, j = cv2.projectPoints(
        a1,
        camera.rotation,
        camera.translation,
        camera.intrinsics,
        np.float64([0, 0, 0, 0])
    )

    ap2, j = cv2.projectPoints(
        a2,
        camera.rotation,
        camera.translation,
        camera.intrinsics,
        np.float64([0, 0, 0, 0])
    )

    ap3, j = cv2.projectPoints(
        a3,
        camera.rotation,
        camera.translation,
        camera.intrinsics,
        np.float64([0, 0, 0, 0])
    )

    cp0, j = cv2.projectPoints(
        c0,
        camera.rotation,
        camera.translation,
        camera.intrinsics,
        np.float64([0, 0, 0, 0])
    )

    draw(
        frame,
        tuple(cp0.ravel().astype(int)),
        tuple(ap1.ravel().astype(int)),
        tuple(ap2.ravel().astype(int)),
        tuple(ap3.ravel().astype(int))
    )
