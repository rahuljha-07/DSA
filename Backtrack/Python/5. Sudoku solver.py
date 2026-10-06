N = 9


# Function to check if placing a number in the grid is safe
def isSafe(grid, row, col, num):
    # Check if the number is not repeated in the row
    for x in range(N):
        if grid[row][x] == num:
            return False
    # Check if the number is not repeated in the column
    for x in range(N):
        if grid[x][col] == num:
            return False
    # Check if the number is not repeated in the 3x3 subgrid
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


# Backtracking function to solve Sudoku
def solve(grid, row, col):
    # If we have filled all the rows, return true (solved)
    if row == N - 1 and col == N:
        return True
    # If we reach the end of the column, move to the next row and reset column
    if col == N:
        row += 1
        col = 0
    # Skip cells that are already filled
    if grid[row][col] != 0:
        return solve(grid, row, col + 1)
    # Try placing digits 1 to 9
    for num in range(1, N + 1):
        if isSafe(grid, row, col, num):
            # Place the number
            grid[row][col] = num
            # Recur to place next number in the next cell
            if solve(grid, row, col + 1):
                return True
            # If placing the current number doesn't lead to a solution, backtrack
            grid[row][col] = 0
    # Trigger backtracking
    return False


# Function to solve the Sudoku puzzle
def SolveSudoku(grid):
    return solve(grid, 0, 0)


# Function to print the Sudoku grid
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
