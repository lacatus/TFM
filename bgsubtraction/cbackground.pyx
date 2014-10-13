import numpy as np
cimport numpy as np


def scanningwindow(np.ndarray[int, ndim = 2] src, int win_height, int win_width, int win_min_pix):

	cdef unsigned int height = src.shape[0]
	cdef unsigned int width = src.shape[1]

	cdef unsigned int ii
	cdef unsigned int jj

	cdef unsigned int aux

	cdef np.ndarray dst = np.zeros([height - 1, width - 1], dtype = np.uint8)

	for jj in xrange(0, height - win_height, win_height / 2):

		for ii in xrange(0, width - win_width, win_width / 2):

			aux = src[jj, ii] + src[jj + win_height, ii + win_width] - src[jj + win_height, ii] - src[jj, ii + win_width]

			if aux > (win_min_pix * 255):

				dst[jj:jj + win_height, ii:ii + win_width] = 255

	return dst