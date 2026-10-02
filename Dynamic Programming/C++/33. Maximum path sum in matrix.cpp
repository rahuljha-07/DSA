#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;

// Helper function for recursion with memoization
int maxPathSumHelper(vector<vector<int>> &mat, int r, int c, int n, vector<vector<int>> &dp) {
    // Base case: if out of bounds, return a very small value
    if (c < 0 || c >= n) return INT_MIN;

    // Base case: last row, return the value of the current cell
    if (r == n - 1) return mat[r][c];

    // If already computed, return the stored result
    if (dp[r][c] != -1) return dp[r][c];

    // Recursive calls for the three possible moves
    int down = maxPathSumHelper(mat, r + 1, c, n, dp);
    int downLeft = maxPathSumHelper(mat, r + 1, c - 1, n, dp);
    int downRight = maxPathSumHelper(mat, r + 1, c + 1, n, dp);

    // Store the result in dp and return it
    return dp[r][c] = mat[r][c] + max({down, downLeft, downRight});
}

// Main function to find the maximum path sum
int maxPathSum(vector<vector<int>> &mat) {
    int n = mat.size();
    int maxSum = INT_MIN;

    // Create a memoization table initialized to -1
    vector<vector<int>> dp(n, vector<int>(n, -1));

    // Try starting from every column in the first row
    for (int c = 0; c < n; c++) {
        maxSum = max(maxSum, maxPathSumHelper(mat, 0, c, n, dp));
    }

    return maxSum;
}


// bottom up
int maxPathSumBottomUp(vector<vector<int>> &mat) {
    int n = mat.size();
    if (n == 0) return 0;

    vector<vector<int>> dp = mat; // Copy initial values

    for (int row = n - 2; row >= 0; row--) {
        for (int col = 0; col < n; col++) {
            int down = dp[row + 1][col];
            int downLeft = (col > 0) ? dp[row + 1][col - 1] : INT_MIN;
            int downRight = (col < n - 1) ? dp[row + 1][col + 1] : INT_MIN;

            dp[row][col] += max({down, downLeft, downRight});
        }
    }

    // Max value in the first row is the answer
    return *max_element(dp[0].begin(), dp[0].end());
}

int main() {
    vector<vector<int>> mat1 = {{348, 391}, {618, 193}};
    cout << "Maximum path sum: " << maxPathSum(mat1) << endl;

    vector<vector<int>> mat2 = {{2, 2}, {2, 2}};
    cout << "Maximum path sum: " << maxPathSum(mat2) << endl;

    vector<vector<int>> mat3 = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    cout << "Maximum path sum: " << maxPathSum(mat3) << endl;

    vector<vector<int>> mat4 = {
        {10, 10, 2, 0, 20, 4},
        {1, 0, 0, 30, 2, 5},
        {0, 10, 4, 0, 2, 0},
        {1, 0, 2, 20, 0, 4}
    };
    cout << "Maximum path sum: " << maxPathSum(mat4) << endl;

    return 0;
}
