#!/use/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PIL import Image
from numpy import *

from .core.recover import recover
from .core.airlight import airlight
from .core.guidedfilter import guidedfilter
from .core.transmission import transmission


def defogging(src):
    L = array(Image.fromarray(uint8(src *255)).convert("L")).astype(float) / 255
    (hei, wid) = src.shape[0:2]
    A = airlight(src, L, 0.2)
    trans = transmission(src, A, round(0.02 * min(hei, wid)), 0.95)
    trans_refined = guidedfilter(trans, L, 30, 1e-6)
    dst = recover(src, A, trans_refined)
    return dst
