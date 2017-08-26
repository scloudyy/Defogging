#!/use/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *
import scipy.ndimage

from .core.recover import recover
from .core.airlight import airlight
from .core.transmission import transmission
from .utils.reshape import reshape


def defogging(src, img):
    L = array(img.convert("L")).astype(float) / 255
    src_d = scipy.ndimage.zoom(src, (0.5,0.5,1))
    L_d = scipy.ndimage.zoom(L, 0.5)
    (hei, wid) = src_d.shape[0:2]
    A = airlight(src_d, L_d, 0.2)
    trans_d = transmission(src_d, A, round(0.02 * min(hei, wid)), 0.95, L_d)
    trans = reshape(scipy.ndimage.zoom(trans_d, 2), src.shape[0:2])
    dst = recover(src, A, trans)
    return dst
