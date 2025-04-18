#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Recursive helper function with memoization
int minRemovalsHelper(int left, int right, vector<int> &arr, int k, vector<vector<int>> &dp) {
    // Base case: If the range is valid
    if (arr[right] - arr[left] <= k) {
        return 0;
    }

    // If already computed, return the stored value
    if (dp[left][right] != -1) return dp[left][right];

    // Remove either the leftmost or the rightmost element
    int removeLeft = minRemovalsHelper(left + 1, right, arr, k, dp);
    int removeRight = minRemovalsHelper(left, right - 1, arr, k, dp);

    // Store and return the result
    return dp[left][right] = 1 + min(removeLeft, removeRight);
}

int minRemovalsToSatisfyCondition(vector<int> &arr, int k) {
    int n = arr.size();

    // Sort the array
    sort(arr.begin(), arr.end());

    // Create a memoization table initialized to -1
    vector<vector<int>> dp(n, vector<int>(n, -1));

    // Call the recursive helper function
    return minRemovalsHelper(0, n - 1, arr, k, dp);
}

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << minRemovalsToSatisfyCondition(arr, k) << endl;

    return 0;
}
