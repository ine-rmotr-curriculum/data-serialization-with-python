from fractions import Fraction
import pytest
from fractal.sierpiński import gasket

@pytest.mark.parametrize("pixels,N", [
        pytest.param(3**3, 2, id="9x9 canvas; 2 iterations"), 
        pytest.param(3**5, 2), pytest.param(3**5, 3),
        pytest.param(3**7, 2), pytest.param(3**7, 3), pytest.param(3**7, 5)])
def test_outside_set(pixels, N):
    canvas = gasket(pixels, N)
    pix_count = pixels ** 2
    remaining_zeros = Fraction(8, 9)**N * pix_count
    assert len(canvas[canvas==0]) == remaining_zeros
    

@pytest.mark.parametrize("pixels,N", [
        pytest.param(3**3+1, 2), pytest.param(3**5+1, 2), pytest.param(3**5-1, 3),
        pytest.param(3**7-1, 2), pytest.param(3**7+1, 3), pytest.param(3**7-2, 5)])
@pytest.mark.xfail
def test_rounding_errors(pixels, N):
    canvas = gasket(pixels, N)
    pix_count = pixels ** 2
    remaining_zeros = Fraction(8, 9)**N * pix_count
    assert len(canvas[canvas==0]) == remaining_zeros

@pytest.mark.parametrize("pixels,N", [
        pytest.param(3**3+1, 2), pytest.param(3**5+1, 2), pytest.param(3**5-1, 3),
        pytest.param(3**7-1, 2), pytest.param(3**7+1, 3), pytest.param(3**7-2, 5)])
def test_approx_outside_set(pixels, N):
    canvas = gasket(pixels, N)
    pix_count = pixels ** 2
    remaining_zeros = Fraction(8, 9)**N * pix_count
    assert 0.9 < len(canvas[canvas==0])/remaining_zeros < 1.1
