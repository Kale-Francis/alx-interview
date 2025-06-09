#!/usr/bin/python3
"""
This module contains the makeChange function
"""

def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total.
    If total cannot be met by any number of coins, returns -1.
    """
    if total <= 0:
        return 0

    # Set to a large number initially (greater than any possible number of coins needed)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total of 0

    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
