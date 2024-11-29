#include <iostream>
#include <vector>
using namespace std;

// Directions for 8 possible movements
const vector<pair<int, int>> directions = {
    {-1, 0}, {1, 0}, {0, -1}, {0, 1}, // Up, Down, Left, Right
    {-1, -1}, {-1, 1}, {1, -1}, {1, 1} // Diagonals
};

// Helper function to perform DFS
void dfs(int row, int col, vector<vector<char>>& grid, vector<vector<bool>>& visited) {
    int n = grid.size();
    int m = grid[0].size();
    visited[row][col] = true;

    // Explore all 8 possible directions
    for (auto dir : directions) {
        int newRow = row + dir.first;
        int newCol = col + dir.second;

        // Check boundaries and whether the cell is unvisited land
        if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < m &&
            grid[newRow][newCol] == '1' && !visited[newRow][newCol]) {
            dfs(newRow, newCol, grid, visited);
        }
    }
}

// Function to count the number of islands
int numIslands(vector<vector<char>>& grid) {
    int n = grid.size();
    int m = grid[0].size();

    vector<vector<bool>> visited(n, vector<bool>(m, false)); // Visited array
    int count = 0;

    // Traverse the entire grid
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            // If it's land ('1') and not visited, it's a new island
            if (grid[i][j] == '1' && !visited[i][j]) {
                count++; // Increment the island count
                dfs(i, j, grid, visited); // Perform DFS to mark the whole island
            }
        }
    }

    return count;
}

int main() {
    vector<vector<char>> grid = {
        {'1', '1', '0', '0', '0'},
        {'1', '1', '0', '0', '0'},
        {'0', '0', '1', '0', '0'},
        {'0', '0', '0', '1', '1'}
    };

    cout << "Number of Islands: " << numIslands(grid) << endl; // Output: 3

    return 0;
}
