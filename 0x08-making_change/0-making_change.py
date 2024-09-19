#!/usr/bin/python3
""" Find min number of coins to get the required sum"""
import sys


def makeChange(coins, total):
    """
    Find the minimum number of coins to get the required sum
    """
    # fill memorization with infinity
    memo = [float('inf')] * (total + 1)
    # set base solution of zero
    memo[0] = 0
    # order coins in desc for optimization
    coins.sort(reverse=True)
    # start using bottom up approach
    for i in range(1, total + 1):
        # iterate over coins
        for coin in coins:
            # if coin is less than or equal to i
            if coin <= i:
                # choose min between the current number of coins
                # or prev number of coins stored in memeo[i]
                memo[i] = min(memo[i], memo[i - coin] + 1)
            # if a coin value which is greater reached
            # break the loop as it's desc so all is comming will be greater
            else:
                break
    # return solution for total if it's infinity then no solution return -1
    return memo[total] if memo[total] != [float('inf')] else -1
