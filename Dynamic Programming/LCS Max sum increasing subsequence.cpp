#include <iostream>
#include <vector>
#include <algorithm> // For std::max, std::unique
using namespace std;

// Function to find the maximum sum increasing subsequence using LCS-like approach
int maxSumIncreasingSubsequence(vector<int> &arr) {
    int n = arr.size();

    // Create a sorted array with distinct elements
    vector<int> sortedArr = arr;
    sort(sortedArr.begin(), sortedArr.end());
    sortedArr.erase(unique(sortedArr.begin(), sortedArr.end()), sortedArr.end());
    int m = sortedArr.size();

    // Create a dp table
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    // Fill the dp table
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (arr[i - 1] == sortedArr[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + arr[i - 1];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    // The result is in the last cell of the dp table
    return dp[n][m];
}

int main() {
    vector<int> arr1 = {1, 101, 2, 3, 100};
    cout << "Maximum sum of increasing subsequence: " << maxSumIncreasingSubsequence(arr1) << endl;

    vector<int> arr2 = {4, 1, 2, 3};
    cout << "Maximum sum of increasing subsequence: " << maxSumIncreasingSubsequence(arr2) << endl;

    vector<int> arr3 = {4, 1, 2, 4};
    cout << "Maximum sum of increasing subsequence: " << maxSumIncreasingSubsequence(arr3) << endl;

    return 0;
}
