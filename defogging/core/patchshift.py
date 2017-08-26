from numpy import *

from defogging.utils.minormaxfilter import min_or_max
from defogging.utils.padding import padding


def patchshift(trans, r, base):
    """

    :param trans: original transmission
    :param r: radius
    :param base: the shift base
    :return: dst
    """

    min_base = min_or_max(base, r, "min")
    max_base = min_or_max(base, r, "max")
    dif = max_base - min_base
    (hei, wid) = trans.shape[0:2]

    pad_dif = padding(dif, r)
    for i in range(hei):
        for j in range(wid):
            b = pad_dif[i:i+2*r+1, j:j+2*r+1]
            a = where(b == amax(b))
    return
