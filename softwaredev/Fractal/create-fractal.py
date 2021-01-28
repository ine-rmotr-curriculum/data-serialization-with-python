#!/usr/bin/env python
"Command line generation of fractals"

from argparse import ArgumentParser
import sys
from PIL import Image
import numpy as np
from fractal.mandelbrot import mandelbrot, fast_mandelbrot
from fractal.julia import julia, fast_julia
from fractal.sierpiński import gasket, carpet
from fractal.koch import snowflake
from fractal.visualize import make_canvas
import code
from textwrap import dedent

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
    parser.add_argument('--trace', action="store_true", default=False,
                        help="Trace the fractal generation")
    parser.add_argument('--custom', action="store_true", default=False,
                        help="Define a custom fractal function")
    return parser.parse_args(argv)


def generate(args):
    data = make_canvas(args.fn, args.xcenter, args.ycenter,
                           args.size, args.pixels)
    # Rescale to 0-255 as uint8
    min, max = data.min().astype(float), data.max()
    rescaled = (255 * (data-min)/max).astype(np.uint8)
    im = Image.fromarray(rescaled)
    return im


def main(args):
    fname = f"{args.kind}_{args.xcenter}_{args.ycenter}_{args.size}.png"
    im = generate(args)
    im.save(fname)
    print(f"Saved fractal image {fname}", file=sys.stderr)

def trace(args):
    import trace

    # create a Trace object, telling it what to ignore, and whether to
    # do tracing or line-counting or both.
    tracer = trace.Trace(
            ignoredirs=[sys.prefix, sys.exec_prefix],
            trace=False, count=True)

    # run the new command using the given tracer
    tracer.run('main(args)')

    # make a report, placing output in the current directory
    r = tracer.results()
    r.write_results(show_missing=True, coverdir="coverage")


if __name__ == '__main__':
    args = config()

    if args.custom:
        sys.ps1 = "fractal> "
        sys.ps2 = "     ... "
        banner = dedent("""
        ┌────────────────────────────────────────────────────────────────────┐
        │ *** Define a custom ℂ🠖ℕ function named 'fractal()' ***             │
        │ You may inspect or modify the command-line parameters 'args'       │
        │ ... when complete, press Ctrl-D to save function and exit          │
        └────────────────────────────────────────────────────────────────────┘
        """)
        exitmsg = "--- Using function 'fractal()' to generate image ---"
        args.kind = "fractal"
        code.interact(banner=banner, local=globals(), exitmsg=exitmsg)

    args.fn = eval(args.kind)
    if args.trace:
        trace(args)
    else:
        main(args)

