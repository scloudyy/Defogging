#!/use/bin/env python3
# -*- coding: utf-8 -*-
from numpy import *
from PIL import Image
import sys
from airlight import airlight


def defogging():
    args = sys.argv
    img = Image.open(args[1])
    src = array(img).astype(float) / 255
    L = array(img.convert("L")).astype(float) / 255
    al = airlight(src, L, 0.2)

if __name__ == '__main__':
    defogging()
