#!/use/bin/env python3
# -*- coding: utf-8 -*-
from numpy import *
from PIL import Image
import sys
from airlight import airlight
from transmission import transmission
from guidedfilter import guidedfilter
from recover import recover


def defogging(img):
    src = array(img).astype(float) / 255
    L = array(img.convert("L")).astype(float) / 255
    (hei, wid) = src.shape[0:2]
    A = airlight(src, L, 0.2)
    trans = transmission(src, A, round(0.02 * min(hei, wid)), 0.95)
    trans_refined = guidedfilter(trans, L, 30, 1e-6)
    dst = recover(src, A, trans_refined)

    dst_img = Image.fromarray(uint8(dst * 255))
    outname = args[1] + "_defogging.bmp"
    dst_img.save(outname)
    return dst_img


if __name__ == '__main__':
    args = sys.argv
    img = Image.open(args[1])
    defogging(img)
