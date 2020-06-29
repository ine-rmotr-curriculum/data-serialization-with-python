# Sharing JSON Among Languages

In this exercise you will simulate a RESTful call between services that uses JSON as a data interchange format.  You will simply write two local functions for this purpose, but hypothetically they might be ones that ran on different machines and communicated over HTTP.  The functions you will create are:

* `make_json()` that will accept as data a Python list of namedtuples (shown below) and produce a suitable JSON representation of them.  Each named tuple object will contain a name and a collection of scores.  In the scenario, this is several students in a training course, each of whom receive several percentages on course assignments.  For example:

```python
>>> course
[Student(name='David', scores=[95, 83, 72, 100]),
 Student(name='Santiago', scores=[97, 92, 87]),
 Student(name='Chris', scores=[88, 99, 94, 100, 87])]
```

* `average_grade()` that will accept a JSON string as input, and produce a JSON string as a result.  The result string should give the average score per student as a JSON object. For example:

```python
>>> average_grade(make_json(course))
'{"David": 87.5, "Santiago": 92, "Chris": 93.6}'
```

Note that there are many different reasonable ways to represent the Python data structure we start with as JSON.  The tests will not assume anything other than that the inputs and outputs are JSON strings and that the two functions cooperate as required.


## Setup

```python
import json
from collections import namedtuple

Student = namedtuple("Student", "name scores")
course = [Student("David", [95, 83, 72, 100]),
          Student("Santiago", [97, 92, 87]),
          Student("Chris", [88, 99, 94, 100, 87])]

def make_json(course):
    "Create a JSON representation of the data"
    return json.dumps({"ak": "bar"})

def average_grade(students):
    "Compute the average grade as JSON object mapping name to score"
    return json.dumps({"Akbar": 85, "Jeff": 83})
```


## Test Cases

```python
def test_make_json():
    jstr = make_json(course)
    try:
        json.loads(jstr)
    except json.JSONDecodeError:
        assert False, "Invalid JSON string produced by make_json()"
```

```python
def test_average_grade():
    jstr = make_json(course)
    final = average_grade(jstr)
    try:
        scores = json.loads(final)
    except json.JSONDecodeError:
        assert False, "Invalid JSON string produced by average_grade()"
        
    assert scores == {"David": 87.5, "Santiago": 92, "Chris": 93.6}
```


## Solution

```python
from statistics import mean

def make_json(course):
    return json.dumps({student.name: student.scores for student in course})

def average_grade(students):
    students = json.loads(students)
    return json.dumps({name: mean(score) for (name, score) in students.items()})
```