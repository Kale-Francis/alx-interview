0x05. N Queens
Project Overview
   This project, part of the ALX interview preparation, implements a solution to the N Queens problem using Python. The goal is to place N non-attacking queens on an N×N chessboard using a backtracking algorithm. The script takes a command-line argument N and prints all possible solutions.
Requirements

Environment: Ubuntu 20.04 LTS
Python Version: Python 3.4.3
Allowed Editors: vi, vim, emacs
Code Style: PEP 8 (version 1.7.x)
Files: All files must be executable, start with #!/usr/bin/python3, and end with a newline
Dependencies: Only sys module allowed

Task Description
Task 0: N Queens

File: 0-nqueens.py
Description: Solves the N Queens problem by placing N queens on an N×N board such that no two queens attack each other.
Usage: ./0-nqueens.py N
N must be an integer >= 4.
Prints all solutions as lists of [row, col] positions.


Error Handling:
Wrong number of arguments: Usage: nqueens N
Non-integer N: N must be a number
N < 4: N must be at least 4
Exits with status 1 for invalid input.



Setup and Usage

Clone the Repository:git clone <your-repo-url>
cd alx-interview/0x05-nqueens


Ensure Python 3.4.3:python3.4 --version
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.4


Make File Executable:chmod +x 0-nqueens.py


Run the Script:./0-nqueens.py 4

Example output:[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]



Files

0-nqueens.py: Script to solve the N Queens problem.
README.md: This file, describing the project and usage.

Author
   [Kale Francis]
License
   This project is for educational purposes as part of the ALX program.
