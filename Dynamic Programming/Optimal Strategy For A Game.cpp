#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to solve the game optimally for the given subarray from i to j using memoization
int solve(int i, int j, vector<int>& a, vector<vector<int>>& dp) {
    // Base case: If there is only one coin left, return its value
    if (i == j) {
        return a[i];
    }

    // Check if the value is already computed (memoization)
    if (dp[i][j] != -1) {
        return dp[i][j];
    }

    // Option 1: Take the first coin (a[i]) and the opponent plays optimally on the remaining subarray (i+1 to j)
    int take_first = a[i] + min(solve(i + 2, j, a, dp), solve(i + 1, j - 1, a, dp));

    // Option 2: Take the last coin (a[j]) and the opponent plays optimally on the remaining subarray (i to j-1)
    int take_last = a[j] + min(solve(i + 1, j - 1, a, dp), solve(i, j - 2, a, dp));

    // Store the result in dp[i][j] to avoid redundant computations
    dp[i][j] = max(take_first, take_last);

    return dp[i][j];
}

// Wrapper function to start solving the game from the whole array
int maxAmount(int n, vector<int>& a) {
    // Create a dp table initialized to -1 (indicating uncalculated values)
    vector<vector<int>> dp(n, vector<int>(n, -1));

    // Call the recursive solve function starting from the whole array (0 to n-1)
    return solve(0, n - 1, a, dp);
}

int main() {
    vector<int> arr = {8, 15, 3, 7}; // Example input
    int n = arr.size();
    
    // Output the maximum amount the first player can win
    cout << "Maximum amount that can be won: " << maxAmount(n, arr) << endl;

    return 0;
}
