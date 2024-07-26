#!/usr/bin/python3
"""_summary_
  Generate Pascal's triangle up to the given number of rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
      n (int): The number of rows to generate.

    Returns:
      list: Pascal's triangle up to the given number of rows.
    """
    if n <= 0:
        return []

    triangle = [[1], [1, 1]]  # Precompute first two rows

    for i in range(2, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element is always 1

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # Last element is always 1
        triangle.append(new_row)

    return triangle[:n]  # Return only the required number of rows
