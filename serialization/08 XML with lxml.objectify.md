# Reading XML with lxml.objectify

In this exercise you will compose several "objectify" style queries against the XML document `Bands.xml`  For example, one question we might ask is "In what year was the third band in the document formed?"  An answer to that question could be:

```python
>>> doc.bands.band[2].formation
1975
```

Because we want to make sure that you use the `lxml.objectify` API, you need to provide the queries as strings rather than simply as answers that you can eyeball in the XML text itself.  The tests will simply `eval()` these queries, e.g.:

```python
>>> query1 = "doc.bands.band[2].formation"
>>> eval(query1)
1975
```

* In the variable `query2` write an expression that identifies the last two listed guitarists for Pere Ubu.
* In the variable `query3` write an expression that identifies all the band names listed in the document.
* In the variable `query4` write an expression that counts the number of albums by all listed artists.


## Setup
```python
from lxml import objectify
# Fix this to read actual document
doc = objectify.ObjectifiedElement() 

query1 = "doc.bands.band[2].formation"
query2 = ...
query3 = ...
query4 = ...
```

## Test Cases
```python
def test_doc_type():
    assert isinstance(doc, objectify.ObjectifiedElement)
```

```python
def test_third_formation():
    assert isinstance(query1, str)
    assert eval(query1) == 1975
```

```python
def test_guitarists():
    assert query2.startswith('doc.')
    assert set(eval(query2)) == {'Jim Jones', 'Wayne Kramer'}
```

```python
def test_bands():
    assert isinstance(query3, str)
    assert 'doc.' in query4
    assert set(eval(query3)) == {'Pere Ubu', 'L7', 'The Runaways'}
```

```python
def test_albums():
    assert isinstance(query4, str)
    assert 'doc.' in query4
    assert eval(query4) == 29
```

## Solution
```python
doc = objectify.parse(open('data/Bands.xml'))
doc = objectify.E.root(doc.getroot())

query2 = "doc.bands.band[0].guitarists.item[-2:]"
query3 = "[b.name for b in doc.bands.band[:]]"
query4 = "sum(b.numalbums for b in doc.bands.band[:])"
```