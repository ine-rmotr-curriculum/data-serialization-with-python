# JSON Schema

In this exercise you will need to write JSON Schema definitions that will accept some JSON documents and reject others.  A utility wrapper function, `is_valid()` is provided for tests and for your own experimentation.  You need to define:

* `schema1`: Accept `json1` and `json2` but reject `json3`
* `schema2`: Accept `json2` and `json3` but reject `json1`
* `schema3`: Accept `json1` and `json3` but reject `json2`

## Setup
```python
import json
from jsonschema import validate, ValidationError

def is_valid(instance, schema):
    try:
        validate(instance, schema)
        return True
    except:
        return False

json1 = """{
    "Band": "Pere Ubu",
    "Guitarists": ["Michele Temple", "Keith Moliné",
                   "Peter Laughner", "Tom Herman",
                   "Mayo Thompson", "Jim Jones",
                   "Wayne Kramer"],
    "NumAlbums": 18,
    "Formation": 1975
}"""

json2 = """{
    "Band": "L7",
    "Guitarists": ["Suzi Gardner", "Donita Sparks"],
    "NumAlbums": 7
}"""

json3 = """{
    "Band": "The Runaways",
    "Guitarists": ["Joan Jett", "Lita Ford"],
    "NumAlbums": 4,
    "Formation": "1975"
}"""

schema1 = {"type": "object"}
schema2 = {"type": "string"}
schema3 = {"type": "array"}
```

## Test Cases
```python
def test_schema1():
    assert is_valid(json1, schema1), "schema1 must accept json1"
    assert is_valid(json2, schema1), "schema1 must accept json2"
    assert not is_valid(json3, schema1), "schema1 must reject json3"

def test_schema2():
    assert not is_valid(json1, schema2), "schema2 must reject json1"
    assert is_valid(json2, schema2), "schema2 must accept json2"
    assert is_valid(json3, schema2), "schema2 must accept json3"
    
def test_schema3():
    assert is_valid(json1, schema3), "schema3 must accept json1"
    assert not is_valid(json2, schema3), "schema3 must reject json2"
    assert is_valid(json3, schema3), "schema3 must accept json3"
```

## Solution

```python
schema1 = {
    "type": "object",
    "properties": {
        "NumAlbums": {
            "type": "number",
            "minimum": 5
        }
    }
}
schema2 = {
    "type": "object",
    "properties": {
        "Guitarists": {
             "type": "array",
             "maxItems": 3
        }
    }
}
schema3 = {
    "type": "object",
    "required": ["Formation"]
}
```