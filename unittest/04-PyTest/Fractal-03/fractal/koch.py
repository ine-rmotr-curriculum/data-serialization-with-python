"""Draw a Koch Snowflake

Unlike some other fractals, evaluating a single point for membership 
is dramatically inefficient.  Creating an entire canvas is more direct
"""
import numpy as np

def snowflake(pixels=800, N=5):
    """Draw a Koch snowflake of `N` iterations on canvas of size `pixels`
    
    More than 255 iterations are not be legible, and are not allowed.
    For this implementation, the interior of the snowflake is rendered, 
    not only the boundary outline.
    
    Encode points outside the snowflake as 0.  
    Encode points added to snowflake at iteration n as value n.
    
    >>> canvas = snowflake(500, N=6)
    >>> canvas.shape
    (500, 500)
    """
    assert N < 256
    canvas = np.zeros(shape=(pixels, pixels), dtype=np.uint8)
    # Implementation here...
    return canvas
    