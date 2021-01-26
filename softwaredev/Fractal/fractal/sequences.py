import numpy as np


def scatter(seq1, seq2, pixels=800, ncolor=16):
    canvas = np.zeros(shape=(pixels, pixels), dtype=np.uint8)
    color = 1   
    while True:
        x, y = seq1.get_one(), seq2.get_one()
        if max(x, y) >= pixels:
            break
        canvas[x, y] = color
        color += 1  # Cycle through 15 non-zero colors
        color = 1 if color >= ncolor else color

    return canvas


def scatter_step(seq1, seq2, pixels=800, ncolor=16):
    canvas = np.zeros(shape=(pixels, pixels), dtype=np.uint8)
    color = 1   
    while True:
        x, y = seq1.get_one(), seq2.get_one()
        if max(x, y) >= pixels:
            break
        canvas[x, :y+1] = color
        canvas[:x+1, y] = color
        color += 1  # Cycle through non-zero colors
        color = 1 if color >= ncolor else color

    return canvas