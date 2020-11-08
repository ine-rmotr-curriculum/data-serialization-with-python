import pytest
import numpy as np
from fractal.sierpiński import gasket
from utility.exchange import make_archive
from utility import exchange
import datetime


@pytest.fixture(scope='session')
def sample_gasket():
    return gasket(pixels=729, N=2)


@pytest.fixture
def fixed_timestamp(monkeypatch):
    class Fixed_datetime(datetime.datetime):
        @classmethod
        def now(cls):
            return datetime.datetime(2020, 1, 1)
    monkeypatch.setattr(exchange, 'datetime', Fixed_datetime)


def test_archive_gasket():
    desc = "Test Description"
    archive = make_archive(gasket(pixels=729, N=3), desc)
    assert archive.description == desc
    assert archive.canvas.shape == (729, 729)
    assert archive.hash_ == '04dbb469a0fa7717be4973dfe725b782980da767'
    
def test_non_square():
    with pytest.raises(ValueError) as err:
        make_archive(np.zeros([100, 200]))
    assert str(err.value) == "Canvas must be 2-D and square, not (100, 200)"
        
        
def test_non_2d():
    with pytest.raises(ValueError):
        make_archive(np.ones([30, 30, 30]))
    

def test_archive_timestamp(fixed_timestamp, sample_gasket):
    archive = make_archive(sample_gasket)
    assert archive.timestamp == '2020-01-01T00:00:00'


def test_archive_uuid(monkeypatch, sample_gasket):
    monkeypatch.setattr(exchange, "uuid4", lambda: "Generic-UUID")
    archive = make_archive(sample_gasket)
    assert archive.uuid == "Generic-UUID"


