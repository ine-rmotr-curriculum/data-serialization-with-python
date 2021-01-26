1. Run `./create-fractal.py --help`
1. Run `./create-fractal.py --kind mandelbrot -x-1.0 -y0.28 -s0.15`
1. Run `./create-fractal.py -t julia`
1. View the generated files
1. Edit `create-fractal.py` to add `import pdb; pdb.set_trace()` just before the end.
1. Edit create-fractal.py to add `breakpoint()`` at line 33 (after data=...)
1. Run the program again `./create-fractal.py -t julia`
1. Get help with "h"
1. Show local context with "l"
1. Show function with breakpoint with "ll"
1. `(Pdb) data`
1. `(Pdb) min, max`
1. `(Pdb) data.mean()`
1. Continue with "c"
1. Show program with "ll"
1. `(Pdb) fname`
1. `(Pdb) im`
1. `(Pdb) im.size`
1. Continue/exit with "n"
1. Edit file to only use `breakpoint()`
1. `PYTHONBREAKPOINT=ipdb.set_trace ./create-fractal.py --kind=julia`
1. Move up the stack with "u"
1. Show local context with "l"
1. `ipdb> p args`
1. `ipdb> dir()
1. `ipbd> down`
1. `ipdb> data.<tab>` (pick e.g. dtype)
1. `ipbd> def hello(): print("Hello")`
1. `hello()`
1. `ipdb> q`
1. `PYTHONBREAKPOINT=pudb.set_trace ./create-fractal.py --kind=julia`
1. Show help with "?"
1. Quit with "q"
1. Edit `create-fractal.py` to remove `breakpoint()` lines
1. `python -m pudb ./create-fractal.py --kind mandelbrot -x-1.0 -y0.28 -s0.15`
1. Step through with "n" until we reach `im = generate(...)`
1. Step INTO the function `generate()` with "s"
1. Step INTO the fucntion `make_canvas()` with "s"
1. Step through with "n" until we reach `escape = fn(...)`
1. Step INTO function with "s"
1. Step through with "n" for a while
1. Add breakpoint at line 28 (`z = z*z + z0`)
1. Continue a few times with "c"
1. "V" focus variables
1. "S" focus stack
1. Up twice: "u", "u"
1. Add breakpoint at line 37 (`return im`)
1. "B" focus breakpoints
1. "C" focus code
1. Down stack twice: "d", "d"
1. Add watch expression (focus Variables) with "n": `abs(z)`
1. Continue a few times with "c" (focus Code)
1. Remove breakpoint `mandlebrot.py:28`
1. Continue with "c" (wait a bit)
1. Notice suspicious variables `data` versus `rescaled`
1. At command line (Ctrl-X):
   * `>>> np.bincount(data.flatten())`
   * `>>> np.bincount(rescaled.flatten())`
1. Quit with "Ctrl-X" (leave shell pane) and "q"
1. Fix bug on line 34: `min, max = data.min().astype(float), data.max()`
1. `./create-fractal.py --kind mandelbrot -x-1.0 -y0.28 -s0.15`
1. `./create-fractal.py --kind julia`
1. View the generated fractal











