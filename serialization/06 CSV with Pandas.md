# Reading CSV with Pandas

In this exercise you will read in a delimited data file into a Pandas DataFrame. The format of the delimited file is unusual, but can be handled by the Pandas library with appropriate configuration.

For example, the first few lines of `data/Inventory.txt` contain:

```
Name|Price|Quantity
/Wankle rotary engine/|555.55|527
/Sousaphone w%/ stand/|333.33|123

Feather Duster|22.22|900

/Area 51 metal fragment/|9999.99|
```

Notice the delimiter used and the manner of escaping a delimiter within a field.  Blank lines should be ignored. The DataFrame you generate should have all the same datetypes and values as the stored canonical version.

## Setup

```python
import pandas
items = pd.DataFrame  # List of dataclass objects in this variable
```

## Test Cases

```python
def test_correct_df():
    import pickle
    correct = pickle.load(open('data/Inventory-df.pkl', 'rb'))
    assert isinstance(items, pd.DataFrame)
    assert correct.equals(items), "Generated DataFrame does not match"
```

## Solution

```python
items = pd.read_csv('data/Inventory.txt', 
                    skip_blank_lines=True, 
                    sep='|',
                    quotechar='/',
                    escapechar='%',
                    thousands=',')
```