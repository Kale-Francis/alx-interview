#!/usr/bin/python3
"""
N Queens solver using backtracking
"""
import sys


def is_safe(board, row, col, N, cols, diag1, diag2):
    """Check if a queen can be placed at board[row][col]

    Args:
        board: List of queen positions
        row: Current row
        col: Current column
        N: Board size
        cols: Set of occupied columns
        diag1: Set of occupied main diagonals (row - col)
        diag2: Set of occupied anti-diagonals (row + col)

    Returns:
        bool: True if safe to place queen, False otherwise
    """
    return col not in cols and (row - col) not in diag1 and (row + col) not in diag2


def solve_nqueens(N, row, cols, diag1, diag2, board, solutions):
    """Recursively solve N Queens problem

    Args:
        N: Board size
        row: Current row to place queen
        cols: Set of occupied columns
        diag1: Set of occupied main diagonals
        diag2: Set of occupied anti-diagonals
        board: List of [r, c] positions for queens
        solutions: List to store all solutions
    """
    if row == N:
        solutions.append(board[:])
        return

    for col in range(N):
        if is_safe(board, row, col, N, cols, diag1, diag2):
            board.append([row, col])
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            solve_nqueens(N, row + 1, cols, diag1, diag2, board, solutions)
            board.pop()
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)


def nqueens(N):
    """Solve N Queens problem and print solutions

    Args:
        N: Size of the chessboard (N x N)
    """
    solutions = []
    solve_nqueens(N, 0, set(), set(), set(), [], solutions)
    for solution in solutions:
        print(solution)


def main():
    """Main function to handle input and validation"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    nqueens(N)


if __name__ == "__main__":
    main()
