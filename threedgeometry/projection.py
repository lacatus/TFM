#!/usr/bin/env python

from threedgeometry import cv2
from threedgeometry import np


def drawgroundplane(frame, p):

    cv2.circle(frame, p, 2, (255, 255, 255), thickness=2, lineType=8)


def projectgroundplane(frame, camera):

    for p in camera.plane:

        p1, j = cv2.projectPoints(
            p,
            camera.rotation,
            camera.translation,
            camera.intrinsics,
            np.float64([0, 0, 0, 0])
        )

        drawgroundplane(frame, tuple(p1.ravel().astype(int)))


def drawaxis(frame, c, p1, p2, p3):

    cv2.line(frame, c, p1, (255, 0, 0), thickness=10)
    cv2.line(frame, c, p2, (0, 255, 0), thickness=10)
    cv2.line(frame, c, p3, (0, 0, 255), thickness=10)

    return frame


def projectaxes(frame, camera):

    #axis_factor = camera.axis_factor

    c0 = np.float32([[0, 0, 0]])

    a1 = np.float32([[3, 0, 0]])  #* axis_factor  # x
    a2 = np.float32([[0, 3, 0]])  #* axis_factor  # y
    a3 = np.float32([[0, 0, 3]])  #* axis_factor  # z

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

    drawaxis(
        frame,
        tuple(cp0.ravel().astype(int)),
        tuple(ap1.ravel().astype(int)),
        tuple(ap2.ravel().astype(int)),
        tuple(ap3.ravel().astype(int))
    )
