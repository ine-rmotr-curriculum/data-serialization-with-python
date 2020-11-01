import unittest
from random import randrange
from fractal.visualize import *

class TestCanvas(unittest.TestCase):
    "Test that a canvas has expected properties"
    def setUp(self):
        self.min_pix_val = 0
        self.max_pix_val = 255
        self.base_canvas = make_canvas(self.simple_fn, 0, 0, 800, 800)

    def simple_fn(self, c):
        return max(int(c.real), int(c.imag)) % 256

    def test_canvas_size(self):
        for n in range(8):
            pixels = 2**n
            size = randrange(0, pixels)
            canvas = make_canvas(self.simple_fn, 0, 0, size, pixels)
            self.assertEqual(canvas.shape, (pixels, pixels), 
                             msg=f"Unexpected canvas size {canvas.shape}")
    
    def tearDown(self):
        pass   # clean up resources here...
        
