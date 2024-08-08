#!/usr/bin/python3
"""_summary_ module define a method that calculate
  the min operations to reach a number"""
  

def minOperations(n):
    """
    Calculates the minimum number of operations required to reach a given number.
    Args:
      n (int): The target number.
    Returns:
      int: The minimum number of operations required.
    Examples:
      >>> minOperations(6)
      5
      >>> minOperations(8)
      4
    """
    if n <= 0:
        return 0

    operations: int = 0
    current: int = 1

    while current < n:
        current *= 2
        operations += 1

    if current == n:
        return operations

    return operations + (n - current // 2)
