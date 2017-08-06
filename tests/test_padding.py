import pytest
from defogging.utils.padding import padding
from numpy import *

def test_padding():
    a = array([[1,1,1], [1,1,1], [1,1,1]])
    b = padding(a, 2)
    (hei_a, wid_a) = a.shape[0:2]
    (hei_b, wid_b) = b.shape[0:2]
    assert hei_b == hei_a + 4 and wid_b == wid_a + 4
