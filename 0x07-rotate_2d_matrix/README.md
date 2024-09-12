# alx-interview

Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: `def rotate_2d_matrix(matrix)`

Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.

Solution:
1. Find transpose:
    - Fix the diagonal in place.
    - Iterate over the upper right triangle and swap it with the lower left triangle.
2. Reverse the order for each row.

Example:
Let's say we have the following 2D matrix:

```
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```

After applying the rotation steps, the matrix will be transformed to:

```
matrix = [
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
```