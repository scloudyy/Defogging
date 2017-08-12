import pytest
import sys
from defogging import Defog

def main():
    args = sys.argv
    df = Defog()
    df.read_img(args[1])
    df.defog()
    out_name = args[1] + "_defogged.bmp"
    df.save_img(out_name)

if __name__ == '__main__':
    main()
