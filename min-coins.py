def find_min(a,b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a,b)

def min_coins(total, coins):
    memo = {}
    memo[0]= 0
    for i in range(1, total + 1):
        for coin in coins:
            subTotal = i - coin
            if subTotal < 0:
                continue
            memo[i] = find_min(memo.get(i), memo.get(subTotal) + 1)
            
    return memo[total]

print(min_coins(137, [1,2,5]))