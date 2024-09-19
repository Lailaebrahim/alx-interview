#!/usr/bin/python3
""" Find min number of coins to get the required sum"""
import sys


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
            memo[i] = min(memo[i], memo[subTotal] + 1)

    return memo[total] if memo[total] != sys.maxsize else -1
