Prime Game Project
Overview
This project implements a solution for the "Prime Game" problem, where two players, Maria and Ben, take turns removing prime numbers and their multiples from a set of consecutive integers starting from 1 up to n. The player who cannot make a move loses the game. The goal is to determine the overall winner after multiple rounds, assuming both players play optimally.
The solution is written in Python 3 and uses efficient algorithms to handle inputs up to n = 10,000. The project adheres to the specified requirements, including PEP 8 style guidelines, and includes a single Python file (0-prime_game.py) along with this README.
Repository Structure

Directory: 0x0A-primegame
Files:
0-prime_game.py: Main Python script containing the game logic and solution.
README.md: This file, providing project documentation.



Requirements

Environment: Ubuntu 20.04 LTS
Python Version: Python 3.4.3
Editors: vi, vim, emacs
Code Style: PEP 8 (version 1.7.x)
File Requirements:
All files must be executable.
The first line of all Python files must be #!/usr/bin/python3.
All files must end with a new line.


Constraints:
No external packages may be imported.
Input values: x (number of rounds) and n (upper limit of integers) will not exceed 10,000.



Problem Description
Maria and Ben play a game with the following rules:

Given a set of consecutive integers from 1 to n (inclusive).
Players take turns, with Maria always going first.
In each turn, a player chooses a prime number from the set and removes it along with all its multiples.
The player who cannot make a move (i.e., no prime numbers remain) loses the game.
The game is played for x rounds, where n may vary for each round.
The task is to determine which player wins the most rounds, assuming optimal play.

Function Prototype
def isWinner(x, nums)


Input:
x: Integer, the number of rounds.
nums: List of integers, where each integer represents the n for a round.


Output:
"Maria": If Maria wins the most rounds.
"Ben": If Ben wins the most rounds.
None: If the number of wins is equal or the winner cannot be determined.



Example
x = 3, nums = [4, 5, 1]


Round 1 (n=4):
Maria picks 2, removes 2, 4 → set = {1, 3}.
Ben picks 3, removes 3 → set = {1}.
No primes left; Maria cannot move, so Ben wins.


Round 2 (n=5):
Maria picks 2, removes 2, 4 → set = {1, 3, 5}.
Ben picks 3, removes 3 → set = {1, 5}.
Maria picks 5, removes 5 → set = {1}.
No primes left; Ben cannot move, so Maria wins.


Round 3 (n=1):
No primes available; Maria cannot move, so Ben wins.


Result: Ben wins 2 rounds, Maria wins 1 round → Return "Ben".

Solution Approach
The solution is implemented in 0-prime_game.py and consists of three main functions:

sieve_of_eratosthenes(n):

Uses the Sieve of Eratosthenes algorithm to generate a boolean array indicating which numbers up to n are prime.
Optimizes prime number identification by marking multiples of each prime as non-prime.
Runs once for the maximum n in the input to avoid redundant calculations.


play_game(n, is_prime):

Simulates a single round of the game for a given n.
Uses a set to track remaining numbers and efficiently remove multiples.
Players alternate turns, always picking the smallest available prime.
Returns True if Maria wins, False if Ben wins.


isWinner(x, nums):

Main function that orchestrates the game for x rounds.
Calls sieve_of_eratosthenes once for the maximum n.
Counts Maria's wins by simulating each round.
Compares Maria's and Ben's wins to determine the overall winner.



Algorithm Efficiency

Sieve of Eratosthenes: O(n log log n) time complexity for generating primes up to n.
Game Simulation: O(n log n) per round due to set operations and prime checking.
Overall: Optimized by computing the sieve once and using sets for fast removals, making it efficient for n, x ≤ 10,000.

Installation and Usage

Clone the Repository:
git clone https://github.com/your-username/alx-interview.git
cd alx-interview/0x0A-primegame


Ensure Executable Permissions:
chmod +x 0-prime_game.py


Run a Test:Create a main file (e.g., main_0.py) to test the solution:
#!/usr/bin/python3
isWinner = __import__('0-prime_game').isWinner
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

Execute:
./main_0.py

Expected output:
Winner: Ben



Testing
The project will be tested automatically by a checker released on June 24, 2025, at 6:00 AM. Ensure the code is compatible with Python 3.4.3 on Ubuntu 20.04 LTS. The checker will verify:

Correctness of the winner determination.
Adherence to input constraints (x, n ≤ 10,000).
Compliance with PEP 8 style.
Proper handling of edge cases (e.g., empty nums, x ≤ 0).

Additional Notes

Edge Cases:
If x ≤ 0 or nums is empty, the function returns None.
If n = 1, no primes are available, so the first player (Maria) loses.


Optimization:
The sieve is computed only once for the maximum n to reduce redundant calculations.
Set operations are used for efficient number removal.


Game Theory:
The solution assumes optimal play, where players always choose the smallest available prime (a simple but effective strategy for this game).
The outcome of each round depends on the number of moves possible, which alternates between players.



Resources

Prime Numbers: Khan Academy: Prime Numbers
Sieve of Eratosthenes: Guide to Sieve in Python
Game Theory: Introduction to Game Theory
Python Lists: Python Official Documentation
Dynamic Programming: Dynamic Programming in Python

Project Timeline

Start: June 23, 2025, 6:00 AM
Checker Release: June 24, 2025, 6:00 AM
Deadline: June 27, 2025, 6:00 AM
Auto Review: Launched at the deadline.

Contact
For questions or issues, refer to the GitHub repository issues section: alx-interview.
