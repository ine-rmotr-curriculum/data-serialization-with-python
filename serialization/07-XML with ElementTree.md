# ElementTree for XML

In this exercise, you will construct an XML document from scratch using ElementTree.  The whimsical example is similar to one used in some other exercises in terms of content.  When rendered, this XML will look similar to:

```xml
<?xml version="1.0" ?>
<band>
  <name>L7</name>
  <guitarists>
    <item>Suzi Gardner</item>
    <item>Donita Sparks</item>
  </guitarists>
  <numalbums>7</numalbums>
</band>
```

You should create this top-level element with the variable name `band`, and may use the provided utility function `pretty_etree()` to check your intermediate work.  The tests do not look at exact formatting of semantically incidental aspect of the output (e.g. amount of indent), but only at the ElementTree object created.

## Setup
```python
import xml.etree.ElementTree as ET

# Unfortunately, ElementTree lacks pretty print
import xml.dom.minidom
def pretty_etree(doc):
    dom = xml.dom.minidom.parseString(ET.tostring(doc))
    return dom.toprettyxml(indent='  ')
```

## Test Cases
```python
def test_doc_type():
    assert isinstance(band, ET.Element)
```

```python
def test_doc_structure():
    assert [e.tag for e in band] == ['name', 'guitarists', 'numalbums']
```

```python
def test_guitarists():
    guitarists = band.find('guitarists').findall('item')
    assert [g.text for g in guitarists] == ['Suzi Gardner', 'Donita Sparks']
```

## Solution

```python
band = ET.Element('band')
name = ET.SubElement(band, 'name')
name.text = 'L7'
guitarists = ET.SubElement(band, 'guitarists')
for guitarist in ["Suzi Gardner", "Donita Sparks"]:
    g = ET.SubElement(guitarists, 'item')
    g.text = guitarist
numalbum = ET.SubElement(band, 'numalbums')
numalbum.text = '7'
```