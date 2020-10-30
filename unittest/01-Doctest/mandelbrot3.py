def mandelbrot(z0:complex, orbits:int=255) -> int:
    """Find the escape orbit of points under Mandelbrot iteration
    
    >>> mandelbrot(0.0965-0.638j)
    17
    """
    z = z0
    for n in range(orbits):
        if abs(z) > 2.0:
            return n
        z = z * z + z0
    return orbits  # <-- fixed non-escape return