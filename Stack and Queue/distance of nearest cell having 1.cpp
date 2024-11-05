#include <iostream>
#include <vector>
#include <queue>
#include <climits> // For INT_MAX

using namespace std;

// Function to find the distance of the nearest cell having 1
vector<vector<int>> nearest(vector<vector<int>> grid) {
    int n = grid.size(); // Number of rows in the grid
    int m = grid[0].size(); // Number of columns in the grid
    int i, j;

    // Initialize the distance matrix with a high value (INT_MAX-1)
    // to represent unvisited cells. We use INT_MAX-1 to avoid overflow later.
    vector<vector<int>> v(n, vector<int>(m, INT_MAX - 1));

    queue<pair<int, int>> q; // Queue to perform BFS

    // Enqueue all cells containing '1' and set their distance to 0
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            if (grid[i][j] == 1) {
                q.push({i, j}); // Add the cell to the queue
                v[i][j] = 0; // Distance to itself is zero
            }
        }
    }

    // Directions for moving up, down, left, and right
    int dx[4] = {-1, 1, 0, 0}; // Row changes
    int dy[4] = {0, 0, 1, -1}; // Column changes

    // Perform BFS to find the nearest distance to a cell having '1'
    while (!q.empty()) {
        int x = q.front().first; // Get current cell's row index
        int y = q.front().second; // Get current cell's column index
        q.pop(); // Remove the cell from the queue

        // Explore all four possible directions
        for (i = 0; i < 4; i++) {
            int nx = x + dx[i]; // New row index
            int ny = y + dy[i]; // New column index
            
            // Check if the new position is within the grid boundaries
            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                // If the current distance + 1 is less than the stored distance
                if (v[nx][ny] > v[x][y] + 1) {
                    v[nx][ny] = v[x][y] + 1; // Update the distance
                    q.push({nx, ny}); // Enqueue the new cell for further processing
                }
            }
        }
    }

    // Return the distance matrix
    return v;
}

// Example usage
int main() {
    vector<vector<int>> grid = {
        {0, 0, 1, 0},
        {0, 0, 0, 0},
        {1, 0, 0, 0},
        {0, 0, 0, 1}
    };
    
    vector<vector<int>> result = nearest(grid); // Find nearest distances

    // Print the result
    for (const auto& row : result) {
        for (int distance : row) {
            cout << distance << " ";
        }
        cout << endl;
    }

    return 0;
}
