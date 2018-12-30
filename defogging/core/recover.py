from numpy import *


def recover(src, A, trans):
    """
    J = (I(x) - A) / t(x) +A

    --------
    :param src: original input(three channels)
    :param A: airlight(1,1,3)
    :param trans: transmission(one channel only)
    :return: dst
    """
    (hei, wid) = src.shape[0:2]
    dst = zeros((hei, wid, 3))
    dst[:, :, 0] = divide((src[:, :, 0] - A[0, 0, 0]), trans[:, :]) + A[0, 0, 0]
    dst[:, :, 1] = divide((src[:, :, 1] - A[0, 0, 1]), trans[:, :]) + A[0, 0, 1]
    dst[:, :, 2] = divide((src[:, :, 2] - A[0, 0, 2]), trans[:, :]) + A[0, 0, 2]
    dst = vectorize(lambda x: x if x < 1 else 1)(dst)
    dst = vectorize(lambda x: x if x > 0 else 0)(dst)
    return dst
