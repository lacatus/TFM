#!/usr/bin/env python

from threedgeometry import np


def retroprojectsubject(camera, subject):

    ih = camera.inverse_homography
    sb = subject.h_base
    st = subject.h_top

    uvb = np.array([[sb[0]], [sb[1]], [1]])
    uvt = np.array([[st[0]], [st[1]], [1]])

    db = ih.dot(uvb)
    dt = ih.dot(uvt)

    db = db / db[2]
    dt = dt / dt[2]

    subject.setretroprojection(db, dt)
