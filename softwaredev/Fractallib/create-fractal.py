#!/usr/bin/env python
"Command line generation of fractals"

from argparse import ArgumentParser
import sys
from PIL import Image
import numpy as np
from fractal.julia import julia
from fractal.sierpiński import gasket, carpet
from fractal.mandelbrot import mandelbrot
from fractal.koch import snowflake
from fractal.visualize import make_canvas


def config(argv=sys.argv[1:]):
    parser = ArgumentParser(description='Create a PNG of a fractal')
    parser.add_argument('-t', '--kind', type=str, default='mandelbrot',
                        help="Type of fractal to create")
    parser.add_argument('-x', '--xcenter', type=float, default=0,
                        help="Real coordinate of center of canvas")
    parser.add_argument('-y', '--ycenter', type=float, default=0,
                        help="Imaginary coordinate of center of canvas")
    parser.add_argument('-s', '--size', type=float, default=2,
                        help="Numeric range of values to plot")
    parser.add_argument('-p', '--pixels', type=int, default=800,
                        help="Size of generated graph")
    return parser.parse_args(argv)


def generate(args):
    data = make_canvas(args.fn, args.xcenter, args.ycenter,
                           args.size, args.pixels)
    # Rescale to 0-255 as uint8
    min, max = data.min(), data.max()
    rescaled = (255 * (data-min)/max).astype(np.uint8)
    im = Image.fromarray(rescaled)
    return im


if __name__ == '__main__':
    args = config()
    args.fn = eval(args.kind)
    fname = f"{args.kind}_{args.xcenter}_{args.ycenter}_{args.size}.png"
    im = generate(args)
    im.save(fname)
    print(f"Saved fractal image {fname}")

