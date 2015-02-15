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

    def plikelihood(self):

        (x, y), (h, w), a = self.det
        det = np.floor(np.array([[x, y, h, w]]))

        yrep = np.ones((self.num_p, 4)) * det

        R2 = np.sum(np.power(self.p - yrep, 2), 1)
        width = 2 * (np.amax(np.sqrt(R2)) - np.amin(np.sqrt(R2)))
        self.prob = np.exp(-R2 / width)

        print R2
        print width
        print self.prob

        self.sortprob()

    def sortprob(self):

        idx = self.prob.argsort()[::-1]
        self.prob = self.prob[idx]
        self.p = self.p[idx]

    def pdiffussion(self):

        self.resample()
        pass

    def resample(self):

        if np.sum(self.prob) > 0:

            p = self.p
            new_p = np.array([])

            for ii in range(len(self.p)):

                idx = self.pmfrnd()
                np.append(new_p, p[idx])
                print p[idx]

    def pmfrnd(self):

        x = np.arange(self.num_p)

        dist = np.cumsum(self.prob)
        rndnum = np.random.rand()
        k = np.sum(rndnum > dist) + 1

        print x[k]
        return x[k]
