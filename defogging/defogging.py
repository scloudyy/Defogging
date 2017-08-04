#!/use/bin/env python3
# -*- coding: utf-8 -*-
from numpy import *
from PIL import Image
import sys

from .airlight import cal_airlight
from .transmission import cal_transmission
from .guidedfilter import cal_guidedfilter
from .recover import cal_recover


def defogging(img, name):
    src = array(img).astype(float) / 255
    L = array(img.convert("L")).astype(float) / 255
    (hei, wid) = src.shape[0:2]
    A = cal_airlight(src, L, 0.2)
    trans = cal_transmission(src, A, round(0.02 * min(hei, wid)), 0.95)
    trans_refined = cal_guidedfilter(trans, L, 30, 1e-6)
    dst = cal_recover(src, A, trans_refined)

    dst_img = Image.fromarray(uint8(dst * 255))
    outname = name + "_defogging.bmp"
    dst_img.save(outname)
    return dst_img

def main():
    args = sys.argv
    img = Image.open(args[1])
    defogging(img, args[1])

if __name__ == '__main__':
    main()