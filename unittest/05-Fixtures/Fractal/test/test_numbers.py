import pytest
from pytest import param
import numpy as np
from server.number_server import make_server
from fractal.sequences import scatter
from statistics import mean

@pytest.fixture(scope="session")
def pixels():
    return 200


@pytest.fixture(scope="module")
def zero_seq():
    zero_seq = make_server()
    zero_seq.command('START ZEROES')
    yield zero_seq
    zero_seq.command('FLUSH')
    zero_seq.command('STOP')


@pytest.fixture(scope="function")
def make_prime_server():  # factory pattern
    def _func():
        return 0
    
    return _func


@pytest.fixture(scope="function")
def slow_seq_A():
    slow_seq = make_server()
    slow_seq.command('START STOCHASTIC_SLOW')
    yield slow_seq
    slow_seq.command('FLUSH')
    slow_seq.command('STOP')


@pytest.fixture(scope="function")
def slow_seq_B():
    slow_seq = make_server()
    slow_seq.command('START STOCHASTIC_SLOW')
    yield slow_seq
    slow_seq.command('FLUSH')
    slow_seq.command('STOP')


def test_density(slow_seq_A, slow_seq_B, pixels):
    canvas = scatter(slow_seq_A, slow_seq_B, pixels=pixels)
    ratio = np.count_nonzero(canvas)/pixels**2
    assert 0.25 < ratio < 0.40


def test_zeroes(zero_seq):
    # Server gives all zeroes and fetches more than buffer
    assert zero_seq.n_ready == 50
    assert all(n == 0 for n in zero_seq.get(1000))

    
@pytest.fixture
def make_slow_seq():
    seqs = []
    # Inner function to return one server object
    def _slow_seq():
        slow_seq = make_server()
        slow_seq.command('START STOCHASTIC_SLOW')
        seqs.append(slow_seq)
        return slow_seq
    
    # yield the inner function
    yield _slow_seq
    
    # Cleanup all of the manufactured fixtures
    for seq in seqs:
        seq.command('FLUSH')
        seq.command('STOP')


def test_density2(make_slow_seq, pixels):
    canvas = scatter(make_slow_seq(), make_slow_seq(), pixels=200)
    ratio = np.count_nonzero(canvas)/pixels**2
    assert 0.25 < ratio < 0.40

    
@pytest.fixture(scope="module", 
                params=['PRIMES', 'FIBONACCI', 'NATURAL', 
                        'STOCHASTIC_INCREASING', 'STOCHASTIC_SLOW'])
def seq_kind(request):
    seq = make_server()
    seq.command(f'START {request.param}')
    yield seq
    seq.command('FLUSH')
    seq.command('STOP')
    

def test_ascending_ints(seq_kind):
    nums = seq_kind.get(1000)
    # Only integers in produced list
    assert all(isinstance(n, int) for n in nums)
    # Loosely ascending order
    assert mean(nums[:100]) < mean(nums[450:550]) < mean(nums[-100:])

    
@pytest.fixture(scope="function", params=[2, 3, 4, 5])
def fixnum(request):
    return request.param


@pytest.mark.parametrize("num", [param(7), param(8)])
def test_param_product(fixnum, num):
    assert True
    