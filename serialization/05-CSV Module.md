# Reading CSV with Standard Library

In this exercise you will read in a delimited data file as a list of records.  Each record will be an instance of `InventoryItem`.  The format of the delimited file is unusual, but can be handled by the Python `csv` module with appropriate configuration.

For example, the first few lines of `data/Inventory.txt` contain:

```
Name|Price|Quantity
/Wankle rotary engine/|555.55|527
/Sousaphone w%/ stand/|333.33|123

Feather Duster|22.22|900

/Area 51 metal fragment/|9999.99|
```

Notice the delimiter used and the manner of escaping a delimiter within a field.  Blank lines should be ignored. Your result should match the datatypes annotated in the Data Class.

## Setup

```python
import csv
from dataclasses import dataclass

@dataclass
class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
    
items = []  # List of dataclass objects in this variable
```

## Test Cases

```python
def test_structure():
    import pickle
    correct = pickle.load(open('data/Inventory.pkl', 'rb'))
    assert len(correct) == len(items), "Wrong number of records constructed"
    assert correct == items, "Error in one or more records"
```

## Solution

```python
with open('data/Inventory.txt') as fh:
    inventory = csv.reader(fh, delimiter="|", 
                               quotechar="/",
                               escapechar="%")
    skip_header = next(inventory)
    for record in inventory:
        if not record:
            continue
        name = record[0]
        price = float(record[1])
        quantity = int(record[2].replace(',','')) if record[2] else 0
        record = InventoryItem(name, price, quantity)
        items.append(record)
```