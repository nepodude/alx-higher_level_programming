#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    This means checking for conflicts with previously placed queens.
    """
    # Check for queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check for queens in the same major diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Check for queens in the same minor diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i] == j:
            return False

    return True


def solve_nqueens(N, row, board, solutions):
    """
    Use backtracking to solve the N Queens problem.
    """
    if row == N:
        # Found a valid solution, add it to solutions
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            # Backtrack
            board[row] = -1


def main():
    # Validate command-line arguments
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

    # Initialize the board and solutions
    board = [-1] * N
    solutions = []

    # Solve the N Queens problem
    solve_nqueens(N, 0, board, solutions)

    # Print the solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
