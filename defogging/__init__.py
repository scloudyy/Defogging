from PIL import Image
import numpy as np
import sys

from .defogging import defogging


class Defog():
    def __init__(self):
        self.__foggy_name = None
        self.__foggy_img = None
        self.__foggy_src = None
        self.__defogged = None

    def read_img(self, name):
        """
        read a foggy image from hard disk

        :param name: the name of the foggy image
        """
        self.__foggy_name = name
        self.__foggy_img = Image.open(name)
        self.__foggy_src = np.array(self.__foggy_img).astype(float) / 255

    def read_array(self, array, range):
        """
        read a foggy object from numpy.array

        :param array: a foggy object in numpy.array
        :param range: the range of the input array, only in two value: 1 and 255
                      1 means array's range in [0,1], 255 means array's range in [0,255]
        """
        if range == 1:
            self.__foggy_src = array.astype(float)
            self.__foggy_img = Image.fromarray(np.uint8(array * 255))
        elif range == 255:
            self.__foggy_src = array.astype(float) / 255
            self.__foggy_img = Image.fromarray(np.uint8(array))

    def defog(self):
        self.__defogged = defogging(self.__foggy_src, self.__foggy_img)

    def get_array(self, range):
        """
        return the defogged array

        :param range: the range of the defogged array, only in two value: 1 and 255
                      1 means array's range in [0,1], 255 means array's range in [0,255]
        """
        if self.__defogged == None:
            return 0
        if range == 1:
            return self.__defogged
        elif range == 255:
            return np.uint8(self.__defogged * 255)

    def save_img(self, name):
        """
        save defogged image to the hard disk

        :param name: name of image
        """
        defogged_img = Image.fromarray(np.uint8(self.__defogged * 255))
        defogged_img.save(name)

def main():
    args = sys.argv
    name = args[1]
    df = Defog()
    df.read_img(name)
    df.defog()
    df.save_img(name + "_defogged.bmp")

if __name__ == '__main__':
    main()
