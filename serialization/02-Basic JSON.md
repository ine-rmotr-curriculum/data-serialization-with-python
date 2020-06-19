# Basic JSON

For this exercise you will perform two tasks.  

* You are provided with a string in the variable `bad_json` that is almost JSON, but has some flaws in it.  Correct the string to be valid JSON and to deserialize into the expected dict.  Put your corrected version in the variable `good_json`.

* An instance of a custom class `Person` is provided as the variable `person`.  However, trying to serialize and deserialize this as JSON will fail.  To fix this, expand the `.toJSON()` and `fromJSON()` methods so that you can round-trip instances of this class.

## Setup
```python
import json

class Person:
    def __init__(self, name=None, address=None, 
                       favorite_color=None):
        self.name = name
        self.address = address
        self.favorite_color = favorite_color
        
    def toJSON(self):
        return "JSON string here"
    
    def fromJSON(self, jstr):
        return "Return new instance"

Red = "Red"
person = Person('David', '45 Main St', 'Red')
```

```python
bad_json = """
{"name": "David",
 "address": '45 Main St',
 "favorite_color": Red,
}
"""
good_json = bad_json
```


## Test Cases
```python
def test_json_fixed():
    try:
        person = json.loads(good_json)
    except:
        person = dict()
    assert set(person.keys()) == {'name', 'address', 'favorite_color'}
    assert person.get('name') == 'David'
    assert person.get('address') == "45 Main St"
    assert person.get('favorite_color') == Red
```

```python
def test_round_trip():
    from random import randint
    name = f"Jane-{randint(1, 1000)}"
    person = Person(name, "123 Any Road", "Green")
    jstr = person.toJSON()
    try:
        json.loads(jstr)
    except json.JSONDecodeError:
        assert False, "Invalid JSON string produced"
    new = person.fromJSON(jstr)
    assert isinstance(new, Person), f"Not a Person: {repr(new)}"
    assert person.name == new.name
```

## Solution

```python
# Solution part 1
good_json = """
{"name": "David",
 "address": "45 Main St",
 "favorite_color": "Red"
}
"""
```

```python
# Solution part 2
_Person = Person

class Person(_Person):
    def toJSON(self):
        return json.dumps(self.__dict__)
    
    def fromJSON(self, jstr):
        new = self.__class__()
        new.__dict__ = json.loads(jstr)
        return new
        
person =  Person('David', '45 Main St', Red)        
```
