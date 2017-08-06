import sys
from PIL import Image
from defogging.defogging import defogging

def main():
    args = sys.argv
    name = args[1]
    img = Image.open(name)
    dst = defogging(img)
    dst_name = name + "_defogging.bmp"
    dst.save(dst_name)

if __name__ == '__main__':
    main()
