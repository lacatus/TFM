from tracker import cv2
from tracker import np


class ParticleFilter(object):

    """
    Class that implements the necessary methods
    to obtain a particle filter running
    """

    def __init__(self):

        self.p = None
        self.cov = None
        self.num_p = None
        self.prob = None
        self.det = None

    def setdefault(self, det):

        self.p = np.array([])
        self.cov = np.eye(4) * 1
        self.num_p = 30
        self.prob = np.array([])
        self.det = det

        # Init particles
        self.init_p()

    def init_p(self):

        (x, y), (h, w), a = self.det
        self.p = np.floor(
            np.random.multivariate_normal(
                [x, y, h, w],
                self.cov,
                self.num_p
            )
        )

    def updatedet(self, det):

        self.det = det

    def plikelihood(self):

        (x, y), (h, w), a = self.det
        det = np.floor(np.array([[x, y, h, w]]))
        yrep = np.ones((self.num_p, 4)) * det

        R2 = np.sum(np.power(self.p - yrep, 2), 1)
        width = 2 * (np.amax(np.sqrt(R2)) - np.amin(np.sqrt(R2)))
        prob = np.exp(-R2 / width)

        prob = prob / np.sum(prob)
        self.prob = prob

        self.sortprob()

    def sortprob(self):

        idx = self.prob.argsort()[::-1]
        self.prob = self.prob[idx]
        self.p = self.p[idx]

    def pdiffussion(self):

        self.resample()
        self.motionmodel()

    def resample(self):

        if np.sum(self.prob) > 0:

            p = self.p
            y, x = p.shape
            new_p = np.zeros((y, x))

            for ii in range(len(self.p)):
                idx = self.pmfrnd()
                new_p[ii, :] = p[idx, :]

            self.p = new_p

    def pmfrnd(self):

        x = np.arange(self.num_p)

        dist = np.cumsum(self.prob)
        rndnum = np.random.rand()
        k = np.sum(rndnum > dist)

        return x[k]

    def motionmodel(self):

        p = self.p
        y, x = p.shape

        a0 = np.floor(np.random.uniform(-15, 15, [y, 1]))
        a1 = np.floor(np.random.uniform(-15, 15, [y, 1]))
        a2 = np.floor(np.random.uniform(-3, 3, [y, 1]))
        a3 = np.floor(np.random.uniform(-3, 3, [y, 1]))

        p[:, 0] = p[:, 0] + a0[:, 0]
        p[:, 1] = p[:, 1] + a1[:, 0]
        p[:, 2] = p[:, 2] + a2[:, 0]
        p[:, 3] = p[:, 3] + a3[:, 0]

        self.p = p

    def paintp(self, frame):

        pt = self.p

        for p in pt:
            x, y, h, w = p
            rot_box = (x, y), (h, w), 0
            box = cv2.cv.BoxPoints(rot_box)
            box = np.int0(box)
            cv2.drawContours(frame, [box], 0, (255, 255, 255), 2)
