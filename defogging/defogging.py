#!/use/bin/env python3
# -*- coding: utf-8 -*-
from numpy import *
from PIL import Image
import sys
import airlight

def defogging():
    args = sys.argv
    img = Image.open(args[1])
    src = array(img).astype(float32) / 255
    L = array(img.convert("L")).astype(float32) / 255
    al = airlight.airlight(src, L, 0.2)

if __name__ == '__main__':
    defogging()
