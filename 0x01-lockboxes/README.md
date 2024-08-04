You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
## Problem Description

Write a method that determines if all the boxes can be opened.

### Prototype

```python
def canUnlockAll(boxes: List[List[int]]) -> bool:
  pass
```

### Constraints

- `boxes` is a list of lists.
- A key with the same number as a box opens that box.
- You can assume all keys will be positive integers.
- There can be keys that do not have boxes.
- The first box `boxes[0]` is unlocked.

### Output

Return `True` if all boxes can be opened, else return `False`.
