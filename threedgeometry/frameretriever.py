#!/usr/bin/env python


def getnumcameras(cameras):

    while 1:

        print '\nCamera options:'

        for i in range(1, len(cameras) + 2):

            if i is len(cameras) + 1:
                print ' %s. All cameras\n' % i

            else:
                print ' %s. Camera %s' % (i, i)

        n = raw_input('Please select one option: ')
        n = int(n)

        for j in range(1, len(cameras) + 2):

            if j is n and j <= len(cameras):
                return [cameras[j - 1]]

            elif j is n and j > len(cameras):
                return cameras


def getframes(cameras):

    frames = []

    for cam in cameras:

        ret, frame = cam.video.getframe()
        frames.append(frame)

        if not ret:
            frames = False
            break

    return frames
