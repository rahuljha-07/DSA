N = 9


def isSafe(grid, row, col, num):
    for x in range(N):
        if grid[row][x] == num:
            return False
    for x in range(N):
        if grid[x][col] == num:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def solve(grid, row, col):
    if row == N - 1 and col == N:
        return True
    if col == N:
        row += 1
        col = 0
    if grid[row][col] != 0:
        return solve(grid, row, col + 1)
    for num in range(1, N + 1):
        if isSafe(grid, row, col, num):
            grid[row][col] = num
            if solve(grid, row, col + 1):
                return True
            grid[row][col] = 0
    return False


def SolveSudoku(grid):
    return solve(grid, 0, 0)


def printGrid(grid):
    for i in range(N):
        for j in range(N):
            print(grid[i][j], end=" ")
        print()


def main():
    grid = [[5,3,0,0,7,0,0,0,0], [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0], [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1], [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0], [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]
    print("Original Sudoku Puzzle:")
    printGrid(grid)
    if SolveSudoku(grid):
        print("\nSolved Sudoku Puzzle:")
        printGrid(grid)
    else:
        print("\nNo solution exists!")


if __name__ == "__main__":
    main()


'''
Let E be initially empty cells in the fixed 9x9 puzzle.
Time: O(9^E) search-tree bound: each empty cell can try nine digits;
row/column/box scans are bounded constants for this fixed board.
Space: O(81) auxiliary recursion depth (also includes calls through filled
cells), constant for a 9x9 board. grid is solved in place.
As in the source, prefilled givens must already be consistent; there is
no separate validation pass for an initially contradictory filled board.
'''
