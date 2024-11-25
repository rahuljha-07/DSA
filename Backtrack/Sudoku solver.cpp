#include <iostream>
#include <vector>

#define N 9 // Size of the Sudoku grid

using namespace std;

// Function to check if placing a number in the grid is safe
bool isSafe(int grid[N][N], int row, int col, int num) {
    // Check if the number is not repeated in the row
    for (int x = 0; x < N; x++) {
        if (grid[row][x] == num) {
            return false;
        }
    }

    // Check if the number is not repeated in the column
    for (int x = 0; x < N; x++) {
        if (grid[x][col] == num) {
            return false;
        }
    }

    // Check if the number is not repeated in the 3x3 subgrid
    int startRow = row - row % 3;
    int startCol = col - col % 3;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (grid[i + startRow][j + startCol] == num) {
                return false;
            }
        }
    }

    return true;
}

// Backtracking function to solve Sudoku
bool solve(int grid[N][N], int row, int col) {
    // If we have filled all the rows, return true (solved)
    if (row == N - 1 && col == N) {
        return true;
    }

    // If we reach the end of the column, move to the next row and reset column
    if (col == N) {
        row++;
        col = 0;
    }

    // Skip cells that are already filled
    if (grid[row][col] != 0) {
        return solve(grid, row, col + 1);
    }

    // Try placing digits 1 to 9
    for (int num = 1; num <= N; num++) {
        if (isSafe(grid, row, col, num)) {
            grid[row][col] = num; // Place the number

            // Recur to place next number in the next cell
            if (solve(grid, row, col + 1)) {
                return true;
            }

            // If placing the current number doesn't lead to a solution, backtrack
            grid[row][col] = 0;
        }
    }

    return false; // Trigger backtracking
}

// Function to solve the Sudoku puzzle
bool SolveSudoku(int grid[N][N]) {
    return solve(grid, 0, 0);
}

// Function to print the Sudoku grid
void printGrid(int grid[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }
}

// Main function to test the Sudoku solver
int main() {
    int grid[N][N] = {
        {5, 3, 0, 0, 7, 0, 0, 0, 0},
        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        {0, 9, 8, 0, 0, 0, 0, 6, 0},
        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        {7, 0, 0, 0, 2, 0, 0, 0, 6},
        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        {0, 0, 0, 0, 8, 0, 0, 7, 9}
    };

    cout << "Original Sudoku Puzzle:" << endl;
    printGrid(grid);

    if (SolveSudoku(grid)) {
        cout << "\nSolved Sudoku Puzzle:" << endl;
        printGrid(grid);
    } else {
        cout << "\nNo solution exists!" << endl;
    }

    return 0;
}
