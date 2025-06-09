#!/usr/bin/python3
"""Solves the N Queens problem"""
import sys

def is_safe(row, col, solution):
    """Checks if a queen can be placed at (row, col)"""
    for r, c in solution:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True

def solve_nqueens(n, row=0, solution=[], all_solutions=[]):
    """Uses backtracking to find all solutions"""
    if row == n:
        all_solutions.append(solution.copy())
        return

    for col in range(n):
        if is_safe(row, col, solution):
            solution.append([row, col])
            solve_nqueens(n, row + 1, solution, all_solutions)
            solution.pop()

def main():
    """Entry point of the script"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    all_solutions = []
    solve_nqueens(n, all_solutions=all_solutions)
    for solution in all_solutions:
        print(solution)

if __name__ == "__main__":
    main()
