import pytest
import requests
from utilities import *

class JSONAnswer:
    def __init__(self, data):
        self.data = data
        
    def json(self):
        return self.data

def mock_get(url):
    parts = url.split('/')
    start, stop = map(int, parts[-2:])
    primes = get_primes_upto(stop)
    result = [n for n in primes if n >= start]
    return JSONAnswer(result)
        
                          
def test_exact_moderate_range(monkeypatch):
    # Check for correct results for moderate result size
    correct = [1_000_003, 1_000_033, 1_000_037,
               1_000_039, 1_000_081, 1_000_099]
    monkeypatch.setattr(requests, 'get', mock_get)
    assert get_primes_between(1_000_000, 1_000_100) == correct


class JSONLen:
    def __init__(self, len_):
        self.len = len_
        
    def json(self):
        class Len:
            def __init__(self, len_):
                self.len = len_
            def __len__(self):
                return self.len
            
        return Len(self.len)

def mock_get_approx(url):
    parts = url.split('/')
    start, stop = map(int, parts[-2:])
    return JSONLen(prime_count(stop) - prime_count(start))
    
    
def test_approx_large_range(monkeypatch):
    # Check for approximate results for large result size
    monkeypatch.setattr(requests, 'get', mock_get_approx)
    primes = get_primes_between(100_000_000, 105_000_000)
    at_least, at_most = 279_682, 338_416
    assert at_least < len(primes) < at_most

