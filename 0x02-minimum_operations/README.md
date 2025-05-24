# 0x02. Minimum Operations

## Project Overview

This project tackles a classic algorithmic problem that challenges you to find the minimum number of operations required to achieve a specific number of 'H' characters (`n`) on a text editor screen, starting from a single 'H'. The only two allowed operations are:

1.  **Copy All**: Copies all characters currently on the screen into a buffer.
2.  **Paste**: Pastes the characters from the buffer onto the screen.

This problem is a fascinating blend of algorithmic thinking, dynamic programming principles, and number theory (specifically prime factorization).

## Concepts Explored

To arrive at an efficient solution for this problem, a good grasp of the following concepts is essential:

* **Prime Factorization:** The key insight for solving this problem optimally lies in understanding that the minimum number of operations to reach `n` characters is the sum of its prime factors. For example, to get 6 'H's (prime factors 2 and 3), it costs 2 operations to get to 2 'H's (Copy, Paste) and then 3 operations to multiply that to 6 'H's (Copy, Paste, Paste), totaling 5 operations (2+3).
* **Greedy Algorithms:** The solution employs a greedy approach. At each step, it identifies the smallest prime factor of the current number of characters and performs the corresponding "Copy All" and "Paste" operations. This greedy choice locally leads to a globally optimal solution.
* **Dynamic Programming (underlying principle):** Although the direct implementation might not look like a traditional DP table, the problem can be framed as one where the solution for `n` depends on solutions for its factors, building up from smaller numbers. The prime factorization approach implicitly leverages this.
* **Code Optimization:** The problem requires finding the *minimum* operations, emphasizing the need for an efficient algorithm. The prime factorization method provides this efficiency.
* **Basic Python Programming:** Proficiency with Python fundamentals including `while` loops, `if/else` conditionals, arithmetic operations (especially the modulo `%` and integer division `//`), and function definitions.

## Project Structure

The project directory `0x02-minimum_operations` is expected to contain the following files:

* **`0-minoperations.py`**: This is the main solution file. It contains the `minOperations` function that calculates the minimum operations.
* **`main_0.py`**: (Likely provided by the project's auto-checker) A test script used to verify the `minOperations` function's correctness with various `n` values.
* **`README.md`**: This file, providing a detailed explanation of the project.

## How to Run (Testing)

To test your `0-minoperations.py` solution:

1.  **Navigate to your project directory:**
    ```bash
    cd alx-backend-javascript/0x02-minimum_operations
    ```
2.  **Ensure your script is executable:**
    ```bash
    chmod +x 0-minoperations.py
    chmod +x main_0.py  # If main_0.py is provided and needs execution
    ```
3.  **Run the test script:**
    ```bash
    ./main_0.py
    ```
    (Note: The exact output will depend on the `main_0.py` content, but it should print the results of `minOperations` for different `n` values).

## Solution Approach (`0-minoperations.py`)

The `minOperations(n)` function calculates the minimum operations using a greedy prime factorization approach:

1.  **Base Case Handling:**
    * If `n` is `1` or less, `0` operations are needed as you either already have 1 'H' or cannot achieve less than 1.

2.  **Initialization:**
    * `operations = 0`: This variable will accumulate the total number of operations.
    * `divisor = 2`: We start checking for the smallest possible prime factor.

3.  **Factorization Loop:**
    * A `while` loop continues as long as `n` is greater than `1`. This loop systematically finds and "removes" prime factors from `n`.
    * **Check for Divisibility:** Inside the loop, it checks if the current `n` is perfectly divisible by `divisor` (`n % divisor == 0`).
        * **If Divisible:** This means `divisor` is a prime factor.
            * We add `divisor` to `operations`. (This represents the cost: 1 "Copy All" and `divisor - 1` "Paste" operations to multiply the current `n` by `divisor`).
            * We then update `n` by dividing it by this `divisor` (`n //= divisor`). This reduces the problem to finding the operations for the remaining part of `n`.
            * Crucially, we **do not increment `divisor`**. We keep checking with the *same* `divisor` because a number can have repeated prime factors (e.g., `9 = 3 * 3`).
        * **If Not Divisible:** This means `divisor` is not a factor of the current `n`. We increment `divisor` to check the next potential prime factor.

4.  **Return Result:**
    * Once the `while` loop terminates (when `n` has been reduced to `1`), the `operations` variable will hold the sum of all prime factors, which is the minimum number of operations required.

This method correctly finds the minimum operations by decomposing the target number `n` into its prime factors and summing them up, aligning with the observed pattern of operation costs.

## Author

Kale-Francis
https://github.com/Kale-Francis