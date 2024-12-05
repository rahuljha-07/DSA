// Function to compute LCS of two arrays
int LCS(const vector<int>& arr1, const vector<int>& arr2) {
    int n = arr1.size();
    int m = arr2.size();

    // Create a DP table
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    // Fill the DP table
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (arr1[i - 1] == arr2[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    return dp[n][m]; // The length of LCS
}

// Function to find the length of the longest increasing subsequence
int longestSubsequence(vector<int>& arr) {
    vector<int> sortedArr = arr;

    // Sort and remove duplicates
    sort(sortedArr.begin(), sortedArr.end());
    sortedArr.erase(unique(sortedArr.begin(), sortedArr.end()), sortedArr.end());

    // Find the LCS between arr and sortedArr
    return LCS(arr, sortedArr);
}