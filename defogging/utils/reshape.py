import scipy.ndimage
import numpy as np
from numpy.matlib import repmat

def reshape(src, shape):
    (hei_dst, wid_dst) = shape
    (hei, wid) = src.shape[0:2]
    dst = src
    if hei > hei_dst:
        dst = dst[0:hei_dst, :]
    elif hei < hei_dst:
        tmp = repmat(dst[hei - 1:hei, :], hei_dst - hei, 1)
        dst = np.insert(dst, hei, values=tmp, axis=0)

    if wid > wid_dst:
        dst = dst[:, 0:wid_dst]
    elif wid < wid_dst:
        tmp = repmat(dst[:, wid - 1:wid].T, wid_dst - wid, 1)
        dst = np.insert(dst, wid, values=tmp, axis=1)

    return dst
