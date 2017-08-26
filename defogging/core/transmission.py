from numpy import *

from defogging.utils.minormaxfilter import min_or_max
from .patchshift import patchshift
from .guidedfilter import guidedfilter


def transmission(src, A, r, w, L):
    """

    :param src: original input image(three channels)
    :param A: airlight(1,1,3)
    :param r: radius of darkchannel
    :param w: t = 1 - w*(I/A)
    :return: dst
    """
    (hei, wid) = src.shape[0:2]
    tmp = zeros((hei, wid))
    for i in range(hei):
        for j in range(wid):
            tmp[i, j] = min(src[i, j, :] / A[0, 0, :])
    min_tmp = min_or_max(tmp, r, "min")
    dst = ones((hei, wid)) - min_tmp[:, :]

    dst  = vectorize(lambda x: x if x > 0.1 else 0.1)(dst)

    dst_refined = guidedfilter(dst, L, 30, 1e-6)
    return dst_refined
