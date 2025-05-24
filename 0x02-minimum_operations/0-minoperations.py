#!/usr/bin/python3
"""
0-minoperations module
"""


def minOperations(n):
    """
    Calculates the minimum number of operations to get n 'H' characters.
    Operations allowed: Copy All, Paste.
    Starts with 1 'H'.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations.
             Returns 0 if n is 1 or less.
    """

    # 1. Immediate Return for Base Case:
    if n <= 1:
        return 0  # No comma here!

    # 2. Initialize Variables:
    operations = 0  # No comma here!
    divisor = 2     # Start checking for factors from 2

    # 3. The Main Loop (Finding Prime Factors):
    while n > 1:  # Continue as long as n hasn't been reduced to 1
        # Check if n is perfectly divisible by divisor
        if n % divisor == 0:
            # If divisible, this 'divisor' is a prime factor.
            # It costs 'divisor' operations (1 Copy All + (divisor-1) Pastes)
            operations += divisor
            # Reduce n by dividing it by this factor
            n //= divisor
            # IMPORTANT: Do NOT increment divisor. Stay on this divisor
            # to check if it's a repeated factor (e.g., for n=9, first 3, then another 3)
        else:
            # If not divisible, move to the next potential divisor
            divisor += 1

    # 4. Final Return:
    return operations
