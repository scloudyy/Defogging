import pytest
import numpy as np
from defogging.utils.reshape import reshape

def test_reshape():
    a = np.array([[1,2,3,4],[4,5,6,6],[7,8,9,9]])
    a_re = reshape(a, (6,6))
    (hei, wid) = a_re.shape[0:2]
    assert hei == 6 and wid == 6
    a_re = reshape(a, (2, 2))
    (hei, wid) = a_re.shape[0:2]
    assert hei == 2 and wid == 2
