import numpy as np
from itertools import product
import matplotlib.pyplot as plt


def make_canvas(fn, x, y, size, pixels, kws={}):
    """Create a 'canvas' based on an arbitrary function fn:ℂ🠖ℕ

    fn:     function visualized
    x:      real coordinate of center
    y:      imaginary coordinate of center
    size:   numeric range of value to plot in each coord
    pixels: size of generated graph in pixels (square)

    Canvas is NumPy array of dtype uint8 (0 <= n <= 255)
    """
    xspan, yspan = pixels, pixels
    canvas = np.empty(shape=(xspan, yspan), dtype=np.uint8)
    for row, col in product(range(xspan), range(yspan)):
        real = x - (size/2) + (size * col/xspan)
        imag = y - (size/2) + (size * row/yspan)
        z0 = complex(real, imag)
        escape = fn(z0, **kws) or 0
        canvas[row, col] = escape
    return canvas


def visualize(canvas):
    "Visualize an arbitrary canvas of 8-bit unsigned ints"
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.imshow(canvas)
