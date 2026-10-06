import sys


# Function to check if it's safe to place a queen at board[i][j]
def isSafe(i, j, board):
    # Column check: ensure no queen is in the same column in rows above `i`
    for row in range(i):
        if board[row][j] == 1:
            # A queen is present in the same column above
            return False
    row, col = i, j
    while row >= 0 and col >= 0:
        if board[row][col] == 1:
            # A queen is present in the left-up diagonal
            return False
        # Move one row up
        # Right-up diagonal check
        row -= 1
        # Move one column left
        col -= 1
    row, col = i, j
    while row >= 0 and col < len(board):
        if board[row][col] == 1:
            # A queen is present in the right-up diagonal
            return False
        row -= 1
        # Move one column right
        col += 1
    # If no conflicts are found, it's safe to place a queen at (i, j)
    return True


# Recursive function to solve the N-Queens problem
def solve(row, board, solutions):
    n = len(board)
    # If all queens are placed, store the solution
    if row == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    # Store 1-based column index
                    solution.append(j + 1)
        solutions.append(solution)
        return
    # Try placing a queen in each column of the current row
    for col in range(n):
        if isSafe(row, col, board):
            # Place the queen
            board[row][col] = 1
            # Recurse for the next row
            solve(row + 1, board, solutions)
            # Backtrack: remove the queen
            board[row][col] = 0


def solveNQueens(n):
    # Initialize an empty board
    board = [[0] * n for _ in range(n)]
    # Store all solutions
    solutions = []
    # Start solving from row 0
    solve(0, board, solutions)
    return solutions


def main():
    print("Enter the number of queens: ", end="")
    n = int(sys.stdin.read())
    solutions = solveNQueens(n)
    for solution in solutions:
        print(*solution)


if __name__ == "__main__":
    main()


'''
Let n be board size and S the number of solutions.
Time: O(n^2*n!) conservative bound: row placements have at most factorial
valid-column branching, but each attempted row loops over n columns and
isSafe scans up to n cells. Each solution additionally scans n^2 cells.
Space: O(n^2) auxiliary board plus O(n) recursion; O(S*n) output column
positions. The same board is reused and restored for each branch.
'''
