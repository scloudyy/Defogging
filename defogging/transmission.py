from numpy import *
from minfilter import minfilter

def transmission(src, A, r, w):
    """

    :param src: original input image(three channels)
    :param A: airlight(1,1,3)
    :param r: radius of darkchannel
    :param w: t = 1 - w*(I/A)
    :return: dst
    """
    (hei, wid) = src.shape[0:2]
    dst = zeros((hei, wid))
    tmp = zeros((hei, wid, 3))
    min_tmp = zeros((hei, wid))
    for c in range(3):
        tmp[:, :, c] = src[:, :, c] / A[0, 0, c]
    tmp[:, :, :] = ones((hei, wid, 3)) - tmp[:, :, :]
    for i in range(hei):
        for j in range(wid):
            min_tmp[i, j] = min(tmp[i, j])
    dst = minfilter(min_tmp, r)
    return dst
