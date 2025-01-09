#include <bits/stdc++.h>
using namespace std;

// Recursive function to find all paths
void findPaths(vector<vector<int>>& matrix, int i, int j, vector<int>& path, vector<vector<int>>& result) {
    int rows = matrix.size();
    int cols = matrix[0].size();

    // Return if the current cell is out of bounds
    if (i >= rows || j >= cols) {
        return;
    }

    // Add the current cell to the path
    path.push_back(matrix[i][j]);

    // If we have reached the bottom-right corner, store the path
    if (i == rows - 1 && j == cols - 1) {
        result.push_back(path);
    } else {
        // Call the function for moving down
        findPaths(matrix, i + 1, j, path, result);

        // Call the function for moving right
        findPaths(matrix, i, j + 1, path, result);
    }

    // Backtrack: remove the current cell from the path
    path.pop_back();
}


vector<vector<int>> allPaths(vector<vector<int>>& matrix) {
    vector<vector<int>> result;
    vector<int> path;
    findPaths(matrix, 0, 0, path, result);
    return result;
}

int main() {
    vector<vector<int>> matrix = {
        {1, 2, 3},
        {4, 5, 6}
    };

    // Get all paths
    vector<vector<int>> paths = allPaths(matrix);

    // Print the paths
    for (const auto& path : paths) {
        cout << "[";
        for (size_t i = 0; i < path.size(); i++) {
            cout << path[i];
            if (i != path.size() - 1) cout << ", ";
        }
        cout << "]" << endl;
    }

    return 0;
}
