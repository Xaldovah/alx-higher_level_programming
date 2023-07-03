#!/usr/bin/python3
import sys


def is_safe(bd, row, col):
    # Check if a queen can be placed at board[row][col] position
    for i in range(row):
        # Check if there is a queen in the same column or diagonals
        if bd[i] == col or bd[i] - col == i - row or bd[i] - col == row - i:
            return False
    return True


def solve_nqueens(bd, row, n):
    # Base case: If all queens are placed, print the solution
    if row == n:
        print([[i, bd[i]] for i in range(n)])
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(bd, row, col):
            bd[row] = col  # Place the queen at board[row][col]
            solve_nqueens(bd, row + 1, n)  # Recur for the next row
            bd[row] = -1  # Backtrack: Remove the queen


def root(P):
    return P


def reject(P, c):
    return False


def accept(P, c):
    return True


def first(P, c):
    return c


def next(P, s):
    if s == P:
        return None
    return P


def output(P, c):
    pass


def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    bd = [-1] * n  # Initialize an empty chessboard

    solve_nqueens(bd, 0, n)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be an integer")
        sys.exit(1)
