import pytest
from unittest.mock import MagicMock
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


def test_server_API(monkeypatch):
    server = make_server()
    _command = server.command
    monkeypatch.setattr(server, 'command', lambda cmd: None)
    monkeypatch.setattr(server, 'get', lambda n: list(range(n)))
    server.command('START PRIMES')
    nums = server.get(1000)
    # Loosely ascending order
    assert max(nums[:100]) < max(nums[450:550]) < max(nums[-100:])
    # This API internally calls `self.get()` on a server
    assert server.get_one() == 0
    _command('STOP')


def test_server_API2():
    class StubServer:
        def command(self, cmd): pass
        def get(self, n=1):
            return list(range(n))
        def get_one(self):
            return self.get()[0]
        
    server = StubServer()
    server.command('START PRIMES')
    nums = server.get(1000)
    assert len(nums) == 1000
    assert max(nums[:100]) < max(nums[450:550]) < max(nums[-100:])
    assert server.get_one() == 0


def test_prime_jumps():
    expected = iter([1, 2, 5, 19, 103, 733, 6691, 76831, 1081429])
    server = make_server().command('START PRIMES')
    server.get = MagicMock(wraps=server.get)
    n = 1
    while n < 1_000_000:
        nums = server.get(n)
        n = nums[-1]
        server.get.assert_called_with(next(expected))
    server.command('STOP')
