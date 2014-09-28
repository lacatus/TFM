#!/usr/bin/env python


def getframes(cameras):

    frames = []

    for cam in cameras:

        ret, frame = cam.video.getframe()
        frames.append(frame)

        if not ret:
            frames = False
            break

    return frames
