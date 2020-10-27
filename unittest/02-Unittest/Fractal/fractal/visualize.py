import numpy as np
from itertools import product
import matplotlib.pyplot as plt


def make_canvas(fn, x, y, size, pixels, kws={}):
    xspan, yspan = pixels, pixels
    canvas = np.empty(shape=(xspan, yspan), dtype=np.uint8)
    for row, col in product(range(xspan), range(yspan)):
        real = x - (size/2) + (size * col/xspan)
        imag = y - (size/2) + (size * row/yspan)
        z0 = complex(real, imag)
        escape = fn(z0, **kws) or 0
        canvas[row, col] = escape
    return canvas


def visualize(fn, x, y, size, pixels, kws={}):
    """Visualize an arbitrary function fn:ℂ🠖ℕ
    
    fn:     function visualized
    x:      real coordinate of center
    y:      imaginary coordinate or center
    size:   numeric range of value to plot in each coord
    pixels: size of generated graph in pixels (square)
    """
    canvas = make_canvas(fn, x, y, size, pixels, kws)
    display(canvas)
    
    
def display(canvas):
    "Display a 2-D array"
    assert isinstance(canvas, np.ndarray) and canvas.ndim == 2
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.imshow(canvas)
