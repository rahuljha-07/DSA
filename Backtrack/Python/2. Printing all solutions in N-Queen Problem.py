import sys


def isSafe(i, j, board):
    for row in range(i):
        if board[row][j] == 1:
            return False
    row, col = i, j
    while row >= 0 and col >= 0:
        if board[row][col] == 1:
            return False
        row -= 1
        col -= 1
    row, col = i, j
    while row >= 0 and col < len(board):
        if board[row][col] == 1:
            return False
        row -= 1
        col += 1
    return True


def solve(row, board, solutions):
    n = len(board)
    if row == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append(j + 1)
        solutions.append(solution)
        return
    for col in range(n):
        if isSafe(row, col, board):
            board[row][col] = 1
            solve(row + 1, board, solutions)
            board[row][col] = 0


def solveNQueens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
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
