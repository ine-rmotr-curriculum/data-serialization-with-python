import numpy as np
import pytest
from fractal.visualize import visualize


def test_stretch_null():
    "If most values are used, canvas not modified"
    canvas = np.random.randint(256, size=(800, 800), dtype=np.uint8)
    original = canvas.copy()
    visualize(canvas, stretch_palette=True)
    assert (canvas == original).all()
    assert canvas.min() == 0
    
    
def test_stretch_small():
    "If only a few values are used, convert zeros to 2*max"
    canvas = np.random.randint(33, size=(800, 800), dtype=np.uint8)
    original = canvas.copy()
    visualize(canvas, stretch_palette=True)
    # should change some (many) pixels
    assert (canvas != original).any()
    assert canvas.min() > 0
    # the new max should be 64 (prior max was 32)
    assert canvas.max() == 64
    # next largest is 32
    assert canvas[canvas < 64].max() == 32
    
    
def test_stretch_medium():
    "If moderately more than half values used, convert zeros to 255"
    canvas = np.random.randint(151, size=(800, 800), dtype=np.uint8)    
    original = canvas.copy()
    visualize(canvas, stretch_palette=True)
    # should change some (many) pixels
    assert (canvas != original).any()
    assert canvas.min() > 0
    # the new max should be 255 (prior max was 150)
    assert canvas.max() == 255
    # next largest is 150
    assert canvas[canvas < 255].max() == 150
    

@pytest.mark.xfail
def test_nostretch():
    "If stretch_palette=False, should not change values"
    canvas = np.random.randint(33, size=(800, 800), dtype=np.uint8)
    visualize(canvas, stretch_palette=False)
    # should NOT change any pixels
    assert canvas.min() > 0