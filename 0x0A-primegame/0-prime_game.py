#!/usr/bin/python3

"""
Prime Game module.
Determines the winner of a game where players take turns removing
prime numbers and their multiples from a set of integers 1 to n.
"""

def sieve_of_eratosthenes(n):
    """Generate list of prime numbers up to n using Sieve of Eratosthenes."""
    if n < 0:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

def count_primes(n, is_prime):
    """Count prime numbers up to n."""
    if n < 0:
        return 0
    return sum(1 for i in range(n + 1) if is_prime[i])

def isWinner(x, nums):
    """
    Determine the winner of x rounds of the prime game.
    
    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing n for each round.
    
    Returns:
        str or None: Name of the player who won the most rounds ("Maria" or "Ben"),
                    or None if the winner cannot be determined.
    """
    if x < 0 or not nums:
        return None
    
    # Find maximum n to create sieve once
    max_n = max((n for n in nums if n >= 0), default=0)
    
    # Generate prime numbers up to max_n
    is_prime = sieve_of_eratosthenes(max_n)
    
    # Count Maria's wins
    maria_wins = 0
    for i in range(min(x, len(nums))):
        n = nums[i]
        if n < 0:
            continue
        # The player who makes the last move wins. Count primes to determine moves.
        # If number of primes is odd, Maria (first player) wins; if even, Ben wins.
        if count_primes(n, is_prime) % 2 == 1:
            maria_wins += 1
    
    # Determine overall winner
    ben_wins = min(x, len(nums)) - maria_wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
