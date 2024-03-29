#!/usr/bin/python3
import sys


def is_safe(bd, row, col):
    """Check if a queen can be placed at board[row][col] position"""
    for i in range(row):
        """Check if there is a queen in the same column or diagonals"""
        if bd[i] == col or bd[i] - col == i - row or bd[i] - col == row - i:
            return False
    return True


def solve_nqueens(bd, row, n, solutions):
    if row == n:
        """Add the solution to the list"""
        solutions.append([[i, bd[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(bd, row, col):
            bd[row] = col
            solve_nqueens(bd, row + 1, n, solutions)
            bd[row] = -1


def output(P, c):
    for solution in c:
        print(solution)


def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    bd = [-1] * n  # Initialize an empty chessboard
    solutions = []

    solve_nqueens(bd, 0, n, solutions)

    output(None, solutions)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)


if __name__ == '__main__':
    main()
