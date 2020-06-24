# Accessing XML with XPATH

In this exercise you will compose several XPATH queries against the XML document `Bands.xml`  For example, one question we might ask is "In what year was the third band in the document formed?"  An answer to that question could be:

```python
>>> doc.find('.//band[3]/formation').text
'1975'
```

Because we want to make sure that you use the XPATH API, you need to provide the queries as strings rather than simply as answers that you can eyeball in the XML text itself.  The tests will evaluate these queries, e.g.:

```python
>>> xpath1 = ".//band[3]/formation"
>>> text_of(doc, xpath1)
'1975'
```

* In the variable `xpath2` write an expression that identifies the third to last listed guitarists for Pere Ubu.
* In the variable `xpath3` write an expression that identifies all the band names listed in the document.
* In the variable `xpath4` write an expression that lists the number of albums by each listed artist.
* In the function named `count()`, sum the number of albums as returned by `text_of(doc, xpath4)`


## Setup
```python
import xml.etree.ElementTree as ET
doc = ET.Element('bands')

# Utility function to pull out text from elements
def text_of(doc, xpath):
    matches = doc.findall(xpath)
    texts = [e.text for e in matches]
    return texts[0] if len(texts) == 1 else texts

xpath1 = ".//band[3]/formation"
xpath2 = ...
xpath3 = ...
xpath4 = ...

def count(nums):
    return 13
```

## Test Cases
```python
def test_doc_type():
    assert isinstance(doc, ET.ElementTree)
```

```python
def test_third_formation():
    assert text_of(doc, xpath1) == '1975'

```

```python
def test_guitarist():
    assert text_of(doc, xpath2) == 'Mayo Thompson'
```

```python
def test_bands():
    assert set(text_of(doc, xpath3)) == {'Pere Ubu', 'L7', 'The Runaways'}
```

```python
def test_albums():
    nums = set(text_of(doc, xpath4))
    assert nums == {'18', '7', '4'}
    assert count(nums) == 29
```

## Solution
```python
doc = ET.parse('data/Bands.xml')

xpath2 = ".//band[1]/guitarists[1]/item[last()-2]"
xpath3 = "./band/name"
xpath4 = "./band/numalbums"

def count(nums):
    return sum(map(int, nums))
```