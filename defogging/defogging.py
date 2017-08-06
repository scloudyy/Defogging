#!/use/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PIL import Image
from numpy import *

from core.recover import recover
from core.airlight import airlight
from core.guidedfilter import guidedfilter
from core.transmission import transmission


def defogging(name):
    img = Image.open(name)
    src = array(img).astype(float) / 255
    L = array(img.convert("L")).astype(float) / 255
    (hei, wid) = src.shape[0:2]
    A = airlight(src, L, 0.2)
    trans = transmission(src, A, round(0.02 * min(hei, wid)), 0.95)
    trans_refined = guidedfilter(trans, L, 30, 1e-6)
    dst = recover(src, A, trans_refined)

    dst_img = Image.fromarray(uint8(dst * 255))
    dst_name = name + "_defogging.bmp"
    dst_img.save(dst_name)
    return dst

def main():
    args = sys.argv
    defogging(args[1])

if __name__ == '__main__':
    main()
