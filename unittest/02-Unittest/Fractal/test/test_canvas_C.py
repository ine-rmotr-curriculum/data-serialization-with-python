import unittest
from random import randrange
import numpy as np
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
 
    def test_canvas_type(self):
        self.assertIsInstance(self.base_canvas, np.ndarray)
        
    def test_min_max(self):
        self.assertTrue(self.base_canvas.max() <= self.max_pix_val)
        self.assertIn(self.base_canvas.min(), [0, 1, 2])  # actually 0

    def test_val_distribution(self):
        # simple_fn has approx equal value distribution along diagonal
        diag = np.diag(self.base_canvas)
        vals, counts = np.unique(diag, return_counts=True)
        self.assertFalse(counts.max() > counts.min() + 1)
        
    def tearDown(self):
        # clean up resources here...
        pass


class TestCanvasDocs(unittest.TestCase):
    def setUp(self):
        self.fn = lambda c: max(int(c.real), int(c.imag)) % 256
        self.canvas = make_canvas(self.fn, 0, 0, 800, 800)
        
    def test_position_values(self):
        "Verify values in correct place on canvas"
        for x in range(0, 100, 10):
            for y in range(50, 150, 10):
                self.assertEqual(self.canvas[x, y], self.fn(x+y*1j),
                                 msg=f"Error for simple_fn({x}+{y}j)")
        
    
if __name__ == '__main__':
    unittest.main()