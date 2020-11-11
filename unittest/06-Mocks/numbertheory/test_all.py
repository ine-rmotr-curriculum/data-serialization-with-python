import pytest
from utilities import *
from pathlib import Path


@pytest.fixture(params=list(range(10)))
def randoms_uint64(request):
    # Do not actually use parameter, just want to test multiple
    count = 10_000
    fname = random_uint64_to_file(count=count)
    yield fname, count
    Path(fname).unlink()


@pytest.fixture(scope="session", params=list(range(1, 6)))
def number_file(request):
    n = 10**request.param
    fname = f'numbers-{n}.txt'
    with open(fname, 'w') as fh:
        for i in range(1, n+1):
            print(i, file=fh)
    yield fname, request.param
    Path(fname).unlink()


@pytest.fixture(scope="session")
def primes_5000():
    fname = 'primes-5000.txt'
    with open(fname, 'w') as fh:
        for i in get_init_primes(5000):
            print(i, file=fh)
    yield fname, 5000
    Path(fname).unlink()

    
@pytest.fixture
def exact_prime_count():
    return {1:4, 2:25, 3:168, 4:1229, 5:9592, 6:78_498}


def test_true_prime_count(number_file, exact_prime_count):
    fname, nlog = number_file
    pnum = count_primes_in_file(fname)
    assert exact_prime_count[nlog] == pnum.numerator


def test_primes_are_likely_primes(primes_5000):
    fname, count = primes_5000
    pnum = count_primes_in_file(fname)
    assert count == pnum.numerator


def test_primality_randoms(randoms_uint64):
    fname, n = randoms_uint64
    if n != 10_000:
        assert False, f"Distribution not checked for size {n}"
    pnum = count_primes_in_file(fname)
    assert 170 < pnum.numerator < 295
