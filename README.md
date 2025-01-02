# Advent of Code

#### Solutions to the Advent of Code challenges

---

##### how to use

First create an .env file in the root directory with the following content:

```
SESSION=<your session cookie>
```

Then create a python file with the sub creator:

```
python3 create_stub.py <year> <day>
```

This wil create stubs for you in the following folders

```
your python puzzle code:
<year>
-- <day>.py

your example input
input
-- <year>
---- <day>.yaml
```

The test files only require the data and answer, but can have args or kwargs. If you do add them make sure to add them to the puzzle file as well.

Example:

```yaml
part_one:
    - data: &data |
        1
        2
        3
      answer: 2
      args: [1] # optional
      kwargs: # optional
        key: value
```
---
```python
from modules.advent_of_code import solve

def parse(data, count, key):
    return data

def part_one(data, count, key):
    return 0

def part_two(data, count, key):
    return 0

solve(part_one, parse, 5, key='value')
```


The python file should print the results and download the input file for you