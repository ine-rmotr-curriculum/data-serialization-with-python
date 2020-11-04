try:
    from numba import njit
except ImportError:
    njit = lambda f: f

@njit
def julia(z:complex, c:complex=-0.1+0.65j, orbits:int=255) -> int:
    for n in range(orbits):
        if abs(z) > 2.0:
            return n
        z = z * z + c
    return orbits
