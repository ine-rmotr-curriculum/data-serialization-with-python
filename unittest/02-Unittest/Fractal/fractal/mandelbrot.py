def mandelbrot(z0:complex, orbits:int=255) -> int:
    """Find the escape orbit of points under Mandelbrot iteration
    
    >>> mandelbrot(0.0965-0.638j)
    17
    
    # Might need to increase orbits to resolve some points
    >>> mandelbrot(0.106225-0.6376125j, orbits=1000)
    291

    # If z0 isn't coercible to complex, TypeError
    >>> mandelbrot('X')  
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/home/davidmertz/git/INE/unittest/01-Doctest/mandelbrot1.py", line 4, in mandelbrot
        if abs(z) > 2.0:
    TypeError: bad operand type for abs(): 'str'
    
    # Orbits must be integer.  Traceback abbreviated below
    >>> mandelbrot(0.0965-0.638j, orbits=3.1) 
    Traceback (most recent call last):
    TypeError: 'float' object cannot be interpreted as an integer
    """
    z = z0
    for n in range(orbits):
        if abs(z) > 2.0:
            return n
        z = z * z + z0