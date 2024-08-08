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
    minOps = 2
    totalOps = 0
    while n > 1:
        while n % minOps == 0:
            totalOps += minOps
            n /= minOps
        minOps += 1
    return totalOps
