#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Generate list of prime numbers up to n using Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

def play_game(n, is_prime):
    """Simulate one game round and return True if Maria wins, False if Ben wins."""
    numbers = set(range(1, n + 1))
    maria_turn = True
    
    while True:
        # Find available prime numbers
        available_primes = [num for num in numbers if is_prime[num]]
        
        # If no primes left, current player loses
        if not available_primes:
            return not maria_turn  # Return True if Maria wins, False if Ben wins
            
        # Current player picks the smallest prime
        prime = min(available_primes)
        
        # Remove prime and its multiples
        multiples = set(range(prime, n + 1, prime))
        numbers -= multiples
        
        # Switch turns
        maria_turn = not maria_turn

def isWinner(x, nums):
    """Determine the winner of x rounds with given n values."""
    if not nums or x <= 0:
        return None
        
    # Find maximum n to create sieve once
    max_n = max(nums)
    
    # Generate prime numbers up to max_n
    is_prime = sieve_of_eratosthenes(max_n)
    
    # Count Maria's wins
    maria_wins = 0
    for n in nums:
        if play_game(n, is_prime):
            maria_wins += 1
    
    # Determine overall winner
    ben_wins = x - maria_wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
