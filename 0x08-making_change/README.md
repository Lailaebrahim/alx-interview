# alx-interview

## Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

### Dynamic Programming
Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems. It is applicable when the problem can be divided into overlapping subproblems that can be solved independently. DP uses a table to store the results of subproblems to avoid redundant computations, thus optimizing the overall solution. This technique is particularly useful for optimization problems where the goal is to find the best solution among many possible ones.

### Problem Analysis
The problem of finding the fewest number of coins needed to meet a given amount total can be solved
by finding the fewest number of coins needed to get each number from one till the required 
amount. This can be done by using a DP table where each cell dp[i] represents the fewest number of coins needed to get the amount i.
