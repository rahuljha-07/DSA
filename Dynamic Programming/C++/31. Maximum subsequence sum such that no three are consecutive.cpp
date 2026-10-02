#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Helper function to compute the maximum sum using recursion and memoization
int maxSumNoThreeConsecutiveHelper(vector<int> &arr, int n, vector<int> &dp) {
    // Base cases
    if (n == 0) return 0; // No elements
    if (n == 1) return arr[0]; // Only one element
    if (n == 2) return arr[0] + arr[1]; // Two elements

    // If already computed, return the stored value
    if (dp[n] != -1) return dp[n];

    // Recursive relation with memoization
    dp[n] = max({
        maxSumNoThreeConsecutiveHelper(arr, n - 1, dp),                                   // Exclude current element
        arr[n - 1] + maxSumNoThreeConsecutiveHelper(arr, n - 2, dp),                      // Include current, skip previous
        arr[n - 1] + arr[n - 2] + maxSumNoThreeConsecutiveHelper(arr, n - 3, dp)         // Include current and previous, skip two before
    });

    return dp[n];
}

// Main function to find the maximum sum
int maxSumNoThreeConsecutive(vector<int> &arr) {
    int n = arr.size();
    vector<int> dp(n + 1, -1); // Initialize memoization table with -1
    return maxSumNoThreeConsecutiveHelper(arr, n, dp);
}

int main() {
    vector<int> arr1 = {1, 2, 3};
    cout << "Maximum sum: " << maxSumNoThreeConsecutive(arr1) << endl;

    vector<int> arr2 = {3000, 2000, 1000, 3, 10};
    cout << "Maximum sum: " << maxSumNoThreeConsecutive(arr2) << endl;

    vector<int> arr3 = {100, 1000, 100, 1000, 1};
    cout << "Maximum sum: " << maxSumNoThreeConsecutive(arr3) << endl;

    vector<int> arr4 = {1, 1, 1, 1, 1};
    cout << "Maximum sum: " << maxSumNoThreeConsecutive(arr4) << endl;

    vector<int> arr5 = {1, 2, 3, 4, 5, 6, 7, 8};
    cout << "Maximum sum: " << maxSumNoThreeConsecutive(arr5) << endl;

    return 0;
}
