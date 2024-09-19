#!/usr/bin/python3
""" Find min number of coins to get the required sum"""
import sys


def find_min(a, b):
    """
    Find the minimum of two numbers
    igonre the none number
    """
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


def makeChange(coins, total):
    """
    Find the minimum number of coins to get the required sum
    """
    if total <= 0:
        return 0
    memo = {}
    memo[0] = 0
    coins.sort()
    for i in range(1, total + 1):
        memo[i] = sys.maxsize
        for coin in coins:
            subTotal = i - coin
            if subTotal < 0:
                break
            memo[i] = find_min(memo.get(i), memo.get(
                subTotal,  sys.maxsize) + 1)

    return memo[total] if memo[total] != sys.maxsize else -1
