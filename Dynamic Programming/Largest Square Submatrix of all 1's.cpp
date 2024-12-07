#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int largestSquare(vector<vector<int>> &mat) {
    int n = mat.size();
    int m = mat[0].size();
    int maxSize = 0;

    // Create a DP table to store the size of the largest square ending at each cell
    vector<vector<int>> dp(n, vector<int>(m, 0));

    // Initialize the last row and last column explicitly
    for (int i = 0; i < n; i++) {
        dp[i][m - 1] = mat[i][m - 1];
        maxSize = max(maxSize, dp[i][m - 1]);
    }
    for (int j = 0; j < m; j++) {
        dp[n - 1][j] = mat[n - 1][j];
        maxSize = max(maxSize, dp[n - 1][j]);
    }

    // Fill the DP table for the remaining cells
    for (int i = n - 2; i >= 0; i--) {
        for (int j = m - 2; j >= 0; j--) {
            if (mat[i][j] == 1) {
                dp[i][j] = 1 + min({dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1]});
            } else {
                dp[i][j] = 0; // Cell is 0, so no square can end here
            }
            // Update the maximum size
            maxSize = max(maxSize, dp[i][j]);
        }
    }

    // Return the maximum size of the square
    return maxSize;
}

int main() {
    vector<vector<int>> mat1 = {
        {0, 1, 1, 0, 1},
        {1, 1, 0, 1, 0},
        {0, 1, 1, 1, 0},
        {1, 1, 1, 1, 0},
        {1, 1, 1, 1, 1},
        {0, 0, 0, 0, 0}
    };
    cout << "Largest square size: " << largestSquare(mat1) << endl;

    vector<vector<int>> mat2 = {
        {1, 1},
        {1, 1}
    };
    cout << "Largest square size: " << largestSquare(mat2) << endl;

    vector<vector<int>> mat3 = {
        {0, 0},
        {0, 0}
    };
    cout << "Largest square size: " << largestSquare(mat3) << endl;

    return 0;
}
