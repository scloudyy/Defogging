#!/use/bin/env python3
# -*- coding: utf-8 -*-
from numpy import *
from numpy.matlib import repmat


def guidedfilter(src, I, r, eps):
    """
    guidedfilter: O(1) time implementation of guided filter.

    ----------
    :param src: filtering input image (should be a gray-scale/single channel image)
    :param I: guidance image (should be a gray-scale/single channel image)
    :param r: local window radius
    :param eps: regularization parameter
    :return: dst
    """
    (hei, wid) = I.shape[0:2]
    N = boxfilter(ones((hei,wid)), r)
    mean_I = divide(boxfilter(I, r), N)
    mean_p = divide(boxfilter(src, r), N)
    mean_Ip = divide(boxfilter(multiply(I, src), r), N)
    cov_Ip = mean_Ip - multiply(mean_I, mean_p)

    mean_II = divide(boxfilter(multiply(I, I), r), N)
    var_I = mean_II - multiply(mean_I, mean_I)

    a = divide(cov_Ip, (var_I + eps))
    b = mean_p - multiply(a, mean_I)

    mean_a = divide(boxfilter(a, r), N)
    mean_b = divide(boxfilter(b, r), N)

    dst = multiply(mean_a, I) + mean_b
    return dst


def boxfilter(src, r):
    """
    boxfilter: O(1) time box filtering using cumulative sum.

    ----------
    :param src: input (should be a gray-scale/single channel image)
    :param r: local window radius
    :return: dst(x, y)=sum(sum(src(x-r:x+r,y-r:y+r)))
    """
    (hei, wid) = src.shape[0:2]
    dst = zeros((hei, wid))
    
    cum = cumsum(src, axis=0)
    dst[0:r+1, :] = cum[r:2*r+1, :]
    dst[r+1:hei-r, :] = cum[2*r+1:hei, :] - cum[0:hei-2*r-1, :]
    dst[hei-r:hei, :] = repmat(cum[hei-1:hei, :], r, 1) - cum[hei-2*r-1:hei-r-1, :]

    cum = cumsum(dst, axis=1)
    dst[:, 0:r+1] = cum[:, r:2*r+1]
    dst[:, r+1:wid-r] = cum[:, 2*r+1:wid] - cum[:, 0:wid-2*r-1]
    dst[:, wid-r:wid] = repmat(cum[:, wid-1:wid], 1, r) - cum[:, wid-2*r-1:wid-r-1]
    return dst
