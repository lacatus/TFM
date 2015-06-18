from tracker import cv2
from tracker import np


class ParticleFilter(object):

    """
    Class that implements the necessary methods
    to obtain a particle filter running
    """

    """
    - filtro de particulas
        - si no hago un update --> plikelihood con resultado igual num de pesos
        - si no, sacar pesos basandose en la deteccion
    """

    def __init__(self):

        self.p = None
        self.cov = None
        self.num_p = None
        self.prob = None
        self.det = None
        self.circle = None
        self.p_star = None
        self.p_mean = None
        self.update = 0

    def setdefault(self, subject):

        self.p = np.array([])
        #self.cov = np.eye(5) * 1
        self.cov = np.eye(6) * 1
        self.num_p = 30
        self.prob = np.array([])
        self.det = subject
        self.circle = subject.circle
        self.rb = subject.rot_box
        # Init particles
        self.init_p()

    def init_p(self):

        (x, y), (h, w), a = self.rb
        self.p = np.floor(
            np.random.multivariate_normal(
                [x, y, h, w, 0, 0],
                self.cov,
                self.num_p
            )
        )
        
        self.p_star = [x, y, h, w, 0, 0]

        """
        (x, y), (h, w), a = self.rb
        self.p = np.floor(
            np.random.multivariate_normal(
                [x, y, h, w, self.det.h],
                self.cov,
                self.num_p
            )
        )
        """

    def updatedet(self, subject):

        self.det = subject
        self.rb = subject.rot_box
        self.circle = subject.circle
        self.update = 1

    def plikelihood(self):

        if self.update:
            (x, y), (h, w), a = self.rb

            det = np.floor(np.array([[x, y, h, w, x - self.p_star[0], y - self.p_star[1]]]))
            yrep = np.ones((self.num_p, 6)) * det

            R2 = np.sum(np.power(self.p[:, 0:6] - yrep, 2), 1)
            width = 2 * (np.amax(np.sqrt(R2)) - np.amin(np.sqrt(R2)))
            prob = np.exp(- R2 / width)

            a = np.sum(prob)
            if a != 0.0:
                prob = prob / np.sum(prob)
            self.prob = prob

            self.sortprob()
        self.calculatepstar()

    def sortprob(self):

        idx = self.prob.argsort()[::-1]
        self.prob = self.prob[idx]
        self.p = self.p[idx]

    def calculatepstar(self):

        if np.sum(self.prob) != 0:
            self.p_star = np.average(self.p, axis = 0, weights = self.prob)
        else:
            self.p_star = np.average(self.p, axis = 0)
        
    def calculatepmean(self):

        self.p_mean = np.average(self.p, axis = 0)

    def pdiffussion(self):

        self.resample()
        self.motionmodel()
        self.calculatepmean()

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

        a0 = np.floor(np.random.uniform(-15, 15, [y, 1])) # x
        a1 = np.floor(np.random.uniform(-15, 15, [y, 1])) # y
        a2 = np.floor(np.random.uniform(-3, 3, [y, 1])) # h
        a3 = np.floor(np.random.uniform(-3, 3, [y, 1])) # w
        a4 = np.floor(np.random.uniform(-7, 7, [y, 1])) # vx
        a5 = np.floor(np.random.uniform(-7, 7, [y, 1])) # vy

        """
        p[:, 0] = p[:, 0] + a0[:, 0]
        p[:, 1] = p[:, 1] + a1[:, 0]
        p[:, 2] = p[:, 2] + a2[:, 0]
        p[:, 3] = p[:, 3] + a3[:, 0]

        """

        p[:, 0] = p[:, 0] + p[:, 4] + a0[:, 0] 
        #p[:, 0] = p[:, 0] + a0[:, 0] 
        p[:, 1] = p[:, 1] + p[:, 5] + a1[:, 0]
        #p[:, 1] = p[:, 1] + a1[:, 0]
        p[:, 2] = p[:, 2] + a2[:, 0]
        p[:, 3] = p[:, 3] + a3[:, 0]
        p[:, 4] = p[:, 4] + a4[:, 0]
        p[:, 5] = p[:, 5] + a5[:, 0]

        self.p = p
        self.update = 0

    def paintp(self, frame, color):

        pt = self.p

        for p in pt:
            x, y, h, w, _, _ = p
            #x, y, h, w, _ = p
            rot_box = (x, y), (h, w), 0
            """
            # OpenCV 2.4.8
            box = cv2.cv.BoxPoints(rot_box)
            """
            # OpenCV 3.0.0
            box = cv2.boxPoints(rot_box)
            box = np.int0(box)
            cv2.drawContours(frame, [box], 0, color, 2)

    def paintbestp(self, frame, num, color):

        x, y, h, w, _, _ = self.p_star
        #x, y, h, w, _ = p
        rot_box = (x, y), (h, w), 0
        """
        # OpenCV 2.4.8
        box = cv2.cv.BoxPoints(rot_box)
        """
        # OpenCV 3.0.0
        box = cv2.boxPoints(rot_box)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, color, 2)
        cv2.putText(frame, str(num), (int(x), int(y)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
