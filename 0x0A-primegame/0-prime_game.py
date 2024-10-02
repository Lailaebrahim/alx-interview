#!/usr/bin/python3
"""_summary_
"""


def SieveOfEratosthenes(n):
    """_summary_

    Args:
        n (_type_): _description_
    """
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    return prime


def isWinner(x, nums):
    """
    They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is.
    """
    winner = {"Maria": 0, "Ben": 0}
    for i in range(x):
        if nums[i] < 2:
            winner["Ben"] += 1
            continue
        game_primes = SieveOfEratosthenes(nums[i])
        prime_count = sum(1 for is_prime in game_primes if is_prime)
        if prime_count % 2 == 0:
            winner["Ben"] += 1
        else:
            winner["Maria"] += 1
    if winner["Maria"] > winner["Ben"]:
        return "Maria"
    else:
        return "Ben"
