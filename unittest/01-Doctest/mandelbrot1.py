def mandelbrot(z0:complex, orbits:int=255) -> int:
    z = z0
    for n in range(orbits):
        if abs(z) > 2.0:
            return n
        z = z * z + z0
        
if __name__ == '__main__':
    print(mandelbrot(0.0965-0.638j))  # Should print 17