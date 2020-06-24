# Saving and Loading NumPy Arrays

For this exercise, you will need to create several NumPy arrays, then serialize them to disk using the appropriate NumPy function(s).  Create the following:

* An array called `arr1` that contains random 8-bit unsigned integers ranging from 10 to 50 (inclusive).  The shape of this array should be 4-dimensional with sides 20✕30✕10✕50.
* An array called `arr2` that should contain 100 complex numbers.
* An array called `arr3` of Python strings 'Red', 'Green', 'Blue'

Then save the three arrays (in order) to an archive named `tmp/exercize.npz` in compressed format.

## Setup

```python
import numpy as np

arr1 = ...
arr2 = ...
arr3 = ...
```

## Test Cases

```python
def test_arr1():
    assert str(arr1.dtype) == 'uint8'
    assert arr1.shape == (20, 30, 10, 50)
    assert arr1.min() == 10
    assert arr1.max() == 50
```

```python
def test_arr2():
    assert 'complex' in str(arr2.dtype)
    assert arr2.size == 100
```

```python
def test_arr3():
    assert arr3.size == 3
    assert arr3[0] == 'Red'
    assert arr3[1] == 'Green'
    assert arr3[2] == 'Blue'
```

```python
def test_archive():
    import os
    fsize = os.stat('tmp/exercise.npz').st_size 
    assert fsize < 220_000, "The file might not have been compressed"
    data = list(np.load('tmp/exercise.npz').values())
    assert data[0].shape == (20, 30, 10, 50)
    assert str(data[0].dtype) == 'uint8'
    assert 'complex' in str(data[1].dtype)
    assert set(data[2]) == {'Red', 'Green', 'Blue'}
```

## Solution

```python
arr1 = np.random.randint(10, 51, 300_000, dtype=np.uint8).reshape(20, 30, 10, 50)
arr2 = np.zeros(100, dtype=complex)
arr3 = np.array(['Red', 'Green', 'Blue'])

np.savez_compressed('tmp/exercise', arr1, arr2, arr3)
```
