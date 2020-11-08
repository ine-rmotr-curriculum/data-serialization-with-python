The function, `mandelbrot()` is a calculation of how many "orbits" the 
iterative function $z_{n+1}=z_{n}^{2}+c$ takes until a given point on 
the complex plane "escapes."  The *Mandelbrot Set* is the collection of 
only those points, $z_0$, that never diverge under this function.
Famously, the boundary of this set is a *fractal*, showing increasingly 
more details over every finite number of iterations.

    # Do we calculate escape for every point?
    >>> from random import random
    >>> from fractal.mandelbrot import mandelbrot
    
    # We wish to try a large number of points
    >>> escapes = []
    >>> for _ in range(100_000):
    ...     real = random() * 4 - 2
    ...     imag = random() * 4 - 2
    ...     z0 = complex(real, imag)
    ...     escapes.append(mandelbrot(z0, orbits=255))
    
    # Do we always get good values?
    >>> all(0 <= esc <= 255 for esc in escapes)
    True