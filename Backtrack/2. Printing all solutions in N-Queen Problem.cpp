#include <iostream>
#include <vector>

using namespace std;

// Function to check if it's safe to place a queen at board[i][j]
bool isSafe(int i, int j, vector<vector<int>> &board) {
    // Column check: ensure no queen is in the same column in rows above `i`
    for (int row = 0; row < i; row++) {
        if (board[row][j] == 1) {
            return false; // A queen is present in the same column above
        }
    }

    // Left-up diagonal check
    int row = i, col = j;
    while (row >= 0 && col >= 0) {
        if (board[row][col] == 1) {
            return false; // A queen is present in the left-up diagonal
        }
        row--; // Move one row up
        col--; // Move one column left
    }

    // Right-up diagonal check
    row = i;
    col = j;
    while (row >= 0 && col < board.size()) {
        if (board[row][col] == 1) {
            return false; // A queen is present in the right-up diagonal
        }
        row--; // Move one row up
        col++; // Move one column right
    }

    // If no conflicts are found, it's safe to place a queen at (i, j)
    return true;
}

// Recursive function to solve the N-Queens problem
void solve(int row, vector<vector<int>> &board, vector<vector<int>> &solutions) {
    int n = board.size();
    // If all queens are placed, store the solution
    if (row == n) {
        vector<int> solution;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 1) {
                    solution.push_back(j + 1); // Store 1-based column index
                }
            }
        }
        solutions.push_back(solution);
        return;
    }

    // Try placing a queen in each column of the current row
    for (int col = 0; col < n; col++) {
        if (isSafe(row, col, board)) {
            board[row][col] = 1; // Place the queen
            solve(row + 1, board, solutions); // Recurse for the next row
            board[row][col] = 0; // Backtrack: remove the queen
        }
    }
}

// Main function to initialize the board and start solving
vector<vector<int>> solveNQueens(int n) {
    vector<vector<int>> board(n, vector<int>(n, 0)); // Initialize an empty board
    vector<vector<int>> solutions; // Store all solutions
    solve(0, board, solutions); // Start solving from row 0
    return solutions;
}

// Testing function
int main() {
    int n;
    cout << "Enter the number of queens: ";
    cin >> n;

    vector<vector<int>> solutions = solveNQueens(n);

    // Output each solution
    for (const auto &solution : solutions) {
        for (int pos : solution) {
            cout << pos << " ";
        }
        cout << endl;
    }

    return 0;
}
