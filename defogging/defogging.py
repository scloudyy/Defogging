#!/use/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *

from .core.recover import recover
from .core.airlight import airlight
from .core.transmission import transmission


def defogging(src, img):
    L = array(img.convert("L")).astype(float) / 255
    (hei, wid) = src.shape[0:2]
    A = airlight(src, L, 0.2)
    trans = transmission(src, A, round(0.02 * min(hei, wid)), 0.95, L)
    dst = recover(src, A, trans)
    return dst
