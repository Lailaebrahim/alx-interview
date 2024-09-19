#!/usr/bin/python3
""" Find min number of coins to get the required sum"""


def makeChange(coins, total):
    """
    Find the minimum number of coins to get the required sum
    """
    if total <= 0:
        return 0
    memo = {i: float('inf') for i in range(1, total + 1)}
    memo[0] = 0
    sorted_coins = sorted(coins)
    for i in range(1, total + 1):
        for coin in sorted_coins:
            subTotal = i - coin
            if subTotal < 0:
                break
            memo[i] = memo[i] if memo[i] < (
                memo[subTotal] + 1) else memo[subTotal] + 1

    return memo[total] if memo[total] != float('inf') else -1
