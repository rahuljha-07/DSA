#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

// Function to check if there exists a subset with the given sum
bool subsetHelper(vector<vector<int>>& dp, int arr[], int n, int sum) {
    // Base cases
    if (sum == 0) return true; // Sum of 0 can always be achieved with an empty subset
    if (n == 0) return false; // If no elements are left, we cannot achieve any non-zero sum

    // If already computed, return the value from memoization table
    if (dp[n][sum] != -1) return dp[n][sum];

    // If the current element is less than or equal to the target sum
    if (arr[n - 1] <= sum) {
        // Include the current element or exclude it
        dp[n][sum] = subsetHelper(dp, arr, n - 1, sum - arr[n - 1]) || subsetHelper(dp, arr, n - 1, sum);
    } else {
        // Exclude the current element
        dp[n][sum] = subsetHelper(dp, arr, n - 1, sum);
    }

    return dp[n][sum];
}
// bottom up approach

bool subsetSumPartition(int n, int arr[], int sum) {
    // Initialize a 2D dp array with -1 (indicating uncomputed states)
    vector<vector<int>> dp(n + 1, vector<int>(sum + 1, -1));

    // Call the recursive helper function
    return subsetHelper(dp, arr, n, sum);
}

int main() {
    int arr[] = {2, 3, 7, 8, 10};
    int n = sizeof(arr) / sizeof(arr[0]);
    int sum = 11;

    if (subsetSumPartition(n, arr, sum)) {
        cout << "Subset with the given sum exists.\n";
    } else {
        cout << "Subset with the given sum does not exist.\n";
    }

    return 0;
}

// top down approach
// Function to check if there exists a subset with the given sum using the top-down approach
bool subsetSumTopDown(int arr[], int n, int sum) {
    // Create a DP table to store solutions to subproblems
    bool t[n + 1][sum + 1];

    // Initialize the DP table
    // If the sum is 0, it is always possible to achieve it with an empty subset
    for (int i = 0; i <= n; i++) {
        t[i][0] = true;
    }
    // If no elements are available and sum > 0, it is not possible to achieve the sum
    for (int j = 1; j <= sum; j++) {
        t[0][j] = false;
    }

    // Fill the table iteratively
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= sum; j++) {
            // If the current element can be included (arr[i-1] <= j)
            if (arr[i - 1] <= j) {
                // Include the element or exclude it
                t[i][j] = t[i - 1][j - arr[i - 1]] || t[i - 1][j];
            } else {
                // Exclude the element
                t[i][j] = t[i - 1][j];
            }
        }
    }

    // The final answer is stored in t[n][sum]
    return t[n][sum];
}

