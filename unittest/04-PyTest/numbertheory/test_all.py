
import pytest
from utilities import *

def test_pair_sum_string():
    pairs = pair_sums('abcd')
    assert isinstance(pairs, set)
    assert len(pairs) == 12
    for s in {'ab', 'ac', 'bd', 'db', 'dc'}:
        assert s in pairs

def test_pair_sum_int():
    with pytest.raises(TypeError):
        pairs = pair_sums(1234)

def test_pair_sum_mixed_list():
    with pytest.raises(TypeError):
        pairs = pair_sums(['a', 'b', 'c', 1])

def test_pair_sum_nans():
    # nans are unequal to themselves... hmm...
    from math import isnan
    pairs = pair_sums([1, 2, 3, nan])
    assert len(pairs) == 10
    assert sum(isnan(n) for n in pairs) == 7

@pytest.mark.parametrize('n', [1, 2, 3, 4, 5, 6])
@pytest.mark.xfail
def test_inexact_prime_count(n):
    exact = {1: 4, 2: 25, 3: 168, 4: 1229, 5:9592, 6:78_498}
    result = prime_count(10**n)
    assert result == exact[n], f"Got {result} not {exact[n]}"

@pytest.mark.parametrize('n', [1, 2, 3, 4, 5, 6])
def test_sufficient_prime_count(n):
    exact = {1: 4, 2: 25, 3: 168, 4: 1229, 5:9592, 6:78_498}
    result = prime_count(10**n)
    assert result >= exact[n]
    
@pytest.mark.parametrize('ntest', [0, 1, 2, 3, 4])
def test_reachable_from_primes(ntest):
    from statistics import median_low
    medians = [29, 113, 229, 349, 463]
    n = ntest * 20
    group = get_init_primes(100)[n:n+20]
    assert medians[ntest] == median_low(group)
