#include <bits/stdc++.h>
using namespace std;

// Recursive function to find the shortest safe route
int findShortestSafeRoute(int rows, int cols, set<pair<int, int>>& unsafeCells,
                          vector<vector<bool>>& visited, int currentRow, int currentCol, int steps) {
    // Base case: Check if the current cell is out of bounds, unsafe, or already visited
    if (currentRow < 0 || currentRow >= rows || currentCol < 0 || currentCol >= cols ||
        unsafeCells.count({currentRow, currentCol}) || visited[currentRow][currentCol]) {
        return INT_MAX;
    }

    // If the destination (last column) is reached, return the steps taken
    if (currentCol == cols - 1) {
        return steps;
    }

    // Mark the current cell as visited
    visited[currentRow][currentCol] = true;

    // Explore all four possible directions
    int moveDown = findShortestSafeRoute(rows, cols, unsafeCells, visited, currentRow + 1, currentCol, steps + 1);
    int moveUp = findShortestSafeRoute(rows, cols, unsafeCells, visited, currentRow - 1, currentCol, steps + 1);
    int moveRight = findShortestSafeRoute(rows, cols, unsafeCells, visited, currentRow, currentCol + 1, steps + 1);
    int moveLeft = findShortestSafeRoute(rows, cols, unsafeCells, visited, currentRow, currentCol - 1, steps + 1);

    // Unmark the current cell for backtracking
    visited[currentRow][currentCol] = false;

    // Return the minimum steps from all possible directions
    return min({moveDown, moveUp, moveRight, moveLeft});
}

int main() {
    int rows, cols;
    cout << "Enter the number of rows and columns: ";
    cin >> rows >> cols;

    vector<vector<int>> grid(rows, vector<int>(cols)); // Input grid
    vector<vector<bool>> visited(rows, vector<bool>(cols, false)); // Visited cells tracker

    cout << "Enter the grid (0 for landmine, 1 for safe cell):\n";
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            cin >> grid[i][j];
        }
    }

    // Identify unsafe cells and mark neighboring cells as unsafe
    set<pair<int, int>> unsafeCells;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] == 0) { // Landmine cell
                unsafeCells.insert({i, j});
                if (i + 1 < rows) unsafeCells.insert({i + 1, j}); // Down
                if (i - 1 >= 0) unsafeCells.insert({i - 1, j});   // Up
                if (j + 1 < cols) unsafeCells.insert({i, j + 1}); // Right
                if (j - 1 >= 0) unsafeCells.insert({i, j - 1});   // Left
            }
        }
    }

    // Find the shortest safe route from the first column to the last column
    int shortestRoute = INT_MAX;
    for (int i = 0; i < rows; ++i) {
    // Check if the cell (i, 0) is not in unsafeCells
    if (unsafeCells.find({i, 0}) == unsafeCells.end()) {
        int pathLength = findShortestSafeRoute(rows, cols, unsafeCells, visited, i, 0, 0);
        shortestRoute = min(shortestRoute, pathLength);
    }
}

    // Output the result
    if (shortestRoute == INT_MAX) {
        cout << "No safe route exists.\n";
    } else {
        cout << "The length of the shortest safe route is: " << shortestRoute << endl;
    }

    return 0;
}
