#!/use/bin/env python3
# -*- coding: utf-8 -*-
from numpy import *


def airlight(src, L, ratio):
    """
    airlight: used to calculate values of airlight

    --------
    :param src: original input image with 3 channels
    :param L: lumination of the src, with only 1 channel
    :param ratio: the final window radius < ratio * min(height, width)
    :return: al(1,1,3)
    """
    (hei, wid) = src.shape[0:2]
    min_r = ratio * min((hei, wid))
    al = quadtree(src, L, min_r)
    return al


def quadtree(src, L, min_r):
    (hei, wid) = src.shape[0:2]
    if hei < min_r or wid < min_r:
        al = zeros((1,1,3))
        al[0, 0, 0] = mean(src[:, :, 0])
        al[0, 0, 1] = mean(src[:, :, 1])
        al[0, 0, 2] = mean(src[:, :, 2])
        return al
    mid_hei = floor(hei / 2).astype(int)
    mid_wid = floor(wid / 2).astype(int)
    quad1 = mean(L[0:mid_hei, 0:mid_wid])
    quad2 = mean(L[mid_hei:hei, 0:mid_wid])
    quad3 = mean(L[0:mid_hei, mid_wid:wid])
    quad4 = mean(L[mid_hei:hei, mid_wid:wid])
    if quad1 >= max(quad2, quad3, quad4):
        al = quadtree(src[0:mid_hei, 0:mid_wid, :], L[0:mid_hei, 0:mid_wid], min_r)
    elif quad2 >= max(quad3, quad4):
        al = quadtree(src[mid_hei:hei, 0:mid_wid, :], L[mid_hei:hei, 0:mid_wid], min_r)
    elif quad3 >= quad4:
        al = quadtree(src[0:mid_hei, mid_wid:wid, :], L[0:mid_hei, mid_wid:wid], min_r)
    else:
        al = quadtree(src[mid_hei:hei, mid_wid:wid, :], L[mid_hei:hei, mid_wid:wid], min_r)
    return al

