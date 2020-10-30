import sys
import os
import unittest
import doctest
from random import random

@unittest.skipIf(os.environ.get('SKIP_RANDOM'), "Skipping on ENV setting")
class TestRandom(unittest.TestCase):
    def test_random(self):
        for i in range(10):
            r = random()
            with self.subTest(r=r):
                self.assertTrue(r < 0.9, msg="Value exceeds bounds")


from fractal import mandelbrot
from fractal import julia
from fractal import koch
from fractal import sierpiński

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(mandelbrot))
    tests.addTests(doctest.DocTestSuite(julia))
    tests.addTests(doctest.DocTestSuite(koch))
    tests.addTests(doctest.DocTestSuite(sierpiński))
    return tests