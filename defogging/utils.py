import numpy as np


def padding(src, r):
    """
    padding: used to padding the edges of the src with width of r

    --------
    :param src: input(one channel only)
    :param r: the width of padding
    :return: dst
    """
    (hei, wid) = src.shape[0:2]
    dst = np.zeros((hei+2*r, wid+2*r))
    dst[r:r+hei, r:r+wid] = src[:,:]
    dst[0:r, r:r + wid] = np.tile(src[0:1, 0:wid], [r,1])
    dst[r+hei:, r:r+wid] = np.tile(src[hei-1:hei, 0:wid], [r,1])
    dst[:, 0:r] = np.tile(dst[:, r:r+1], [1,r])
    dst[:, r+wid:] = np.tile(dst[:, r+wid-1:r+wid], [1,r])
    return dst
