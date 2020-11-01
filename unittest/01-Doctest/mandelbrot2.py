def mandelbrot(z0:complex, orbits:int=255) -> int:
    """Find the escape orbit of points under Mandelbrot iteration
    
    >>> mandelbrot(0.0965-0.638j)
    17
    
    # Might need to increase orbits to resolve some points
    >>> mandelbrot(0.106225-0.6376125j, orbits=1000)
    291
    """
    z = z0
    for n in range(orbits):
        if abs(z) > 2.0:
            return n
        z = z * z + z0
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()