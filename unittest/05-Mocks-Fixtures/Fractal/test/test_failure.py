import numpy as np

def test_np_failA():
    a = np.ones(5, dtype=int)
    b = np.array([1, 1, 3, 0, 1], dtype=int)
    assert (a == b).all()
    
    
def test_np_failB():
    a = np.ones(5, dtype=int)
    b = np.array([1, 1, 3, 0, 1], dtype=int)
    np.testing.assert_array_equal(a, b)