from numpy import *

from .padding import padding


def min_or_max(src, r, op):
    """

    :param src: input(one channel only)
    :param r: window radius
    :param op: "min" or "max"
    :return: dst
    """
    if op == "min":
        operation = amin
    else:
        operation = amax
    (hei, wid) = src.shape[0:2]
    dst = zeros((hei, wid))
    src_pad = padding(src, r)
    for i in range(hei):
        for j in range(wid):
            dst[i, j] = operation(src_pad[i:i+2*r+1, j:j+2*r+1])
    return dst
