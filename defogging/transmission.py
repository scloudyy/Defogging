from numpy import *
from .minfilter import cal_minfilter

def cal_transmission(src, A, r, w):
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
    min_tmp = cal_minfilter(tmp, r)
    dst = ones((hei, wid)) - min_tmp[:, :]

    dst  = vectorize(lambda x: x if x > 0.1 else 0.1)(dst)
    return dst
