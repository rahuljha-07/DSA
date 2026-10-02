#include <bits/stdc++.h>
using namespace std;

// Directions for moving up, down, left, and right
int rowDir[] = {-1, 1, 0, 0};
int colDir[] = {0, 0, -1, 1};

// Function to check if the cell is within bounds and not a hurdle
bool isSafe(int x, int y, vector<vector<int>>& matrix, vector<vector<bool>>& visited) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    return (x >= 0 && x < rows && y >= 0 && y < cols && matrix[x][y] == 1 && !visited[x][y]);
}

// Function to find the longest path from (srcX, srcY) to (destX, destY)
void findLongestPath(vector<vector<int>>& matrix, vector<vector<bool>>& visited, 
                     int srcX, int srcY, int destX, int destY, int pathLen, int& maxPathLen) {
    // If the destination is reached, update the maximum path length
    if (srcX == destX && srcY == destY) {
        maxPathLen = max(maxPathLen, pathLen);
        return;
    }

    // Mark the current cell as visited
    visited[srcX][srcY] = true;

    // Explore all four directions
    for (int i = 0; i < 4; i++) {
        int newX = srcX + rowDir[i];
        int newY = srcY + colDir[i];

        if (isSafe(newX, newY, matrix, visited)) {
            findLongestPath(matrix, visited, newX, newY, destX, destY, pathLen + 1, maxPathLen);
        }
    }

    // Backtrack: Unmark the current cell
    visited[srcX][srcY] = false;
}

int main() {
    // Input matrix
    vector<vector<int>> matrix = {
        {1, 1, 1, 1, 1, 1, 1, 1},
        {1, 0, 0, 1, 0, 0, 0, 1},
        {1, 1, 1, 1, 1, 1, 0, 1},
        {0, 0, 0, 0, 1, 0, 0, 1},
        {1, 1, 1, 1, 1, 1, 1, 1}
    };

    // Starting point (source) and destination point
    int srcX = 0, srcY = 0, destX = 4, destY = 7;

    // Check if the source or destination is blocked
    if (matrix[srcX][srcY] == 0 || matrix[destX][destY] == 0) {
        cout << "No path possible" << endl;
        return 0;
    }

    // Visited matrix to track visited cells
    vector<vector<bool>> visited(matrix.size(), vector<bool>(matrix[0].size(), false));

    // Variable to store the maximum path length
    int maxPathLen = 0;

    // Call the function to find the longest path
    findLongestPath(matrix, visited, srcX, srcY, destX, destY, 0, maxPathLen);

    // Output the result
    if (maxPathLen > 0)
        cout << "Longest Path Length: " << maxPathLen << endl;
    else
        cout << "No path possible" << endl;

    return 0;
}
