# Universal Python Serialization

This exercise has two parts.  

For the first we ask you to think about what transient state is, and identify *three* objects that cannot be pickled (and why).  You may create more than three objects if you wish to practice more.

* Create your objects, e.g. `obj1`, `obj2` and `obj3`, each of a different datatype.
* Put these objects in a list `unpickle = [obj1, obj2, obj3]`
* Assure that objects of these types are not pickleable, and each is a distinct type.

For the second part of this exercise, you need to create a "person record" with attributes `name`, `address`, `favorite_color`, and `created_at`.  The first three attributes may store whatever values you prefer; the `created_at` attribute should have the property that when a record is deserialized, it reflects the datetime of deserialization rather than that of original creation.  For example:

```python
>>> person.name
'David Mertz'
>>> person.address
'45 Main St'
>>> person.favorite_color
'Red'
>>> datetime.isoformat(person.created_at)
'2020-06-17T22:54:19.586983'
```

Create an object with the name `person` in your code.

## Setup

```python
import pickle
from datetime import datetime
# import other modules as needed
```

## Test Cases

```python
def test_listed_types():
    from itertools import combinations
    assert len(unpickle) >= 3, "Provide at least 3 objects"
    for (a, b) in combinations(unpickle, 2):
        assert not issubclass(type(a), type(b)), \
            f"issubclass({a}, {b}) not permitted"
        assert not issubclass(type(b), type(a)), \
            f"issubclass({b}, {a}) not permitted"
```

```python
def test_pickle_failure():
    for obj in unpickle:
        pickled = False
        try:
            pkl = pickle.dumps(obj)
            pickled = True
        except:
            pass
            
        if pickled:
            assert False, f"{repr(obj)} should not be pickleable"
```

```python
def test_person_attributes():
    assert hasattr(person, 'name')
    assert hasattr(person, 'address')
    assert hasattr(person, 'favorite_color')
    assert hasattr(person, 'created_at')
    assert isinstance(person.created_at, datetime)
```

```python
def test_deserialize():
    pkl = pickle.dumps(person)
    t1 = datetime.now()
    new = pickle.loads(pkl)
    t2 = datetime.now()
    assert person.created_at < t1 < new.created_at < t2, \
        "Time must be refreshed when record is deserialized"
    assert person.name == new.name
    assert person.address == new.address
    assert person.favorite_color == new.favorite_color
```

## Solution

```python
from urllib.request import urlopen
from tempfile import TemporaryFile

tmp = TemporaryFile('w+b')
web = urlopen('http://example.com')
anon = lambda: None

unpickle = [tmp, web, anon]
```

```python
class Person:
    "Plain class that holds file descriptor"
    def __init__(self, name, address, favorite_color):
        self.name = name
        self.address = address
        self.favorite_color = favorite_color
        self.created_at = datetime.now()

    def __setstate__(self, data):
        self.__dict__ = data
        self.created_at = datetime.now()
        
person = Person('David', '45 Main St', 'Red')
```