// recrusion+ memorization
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

// Global memoization table
vector<vector<int>> t;

int LCS(int n, int m, const string &str1, const string &str2) {
    // Base case: if either string is empty, the LCS is 0
    if (n == 0 || m == 0)
        return 0;

    // Check if the result is already calculated
    if (t[n][m] != -1)
        return t[n][m];

    // If the last characters match, add 1 to the result and move both indices
    if (str1[n - 1] == str2[m - 1])
        t[n][m] = 1 + LCS(n - 1, m - 1, str1, str2);
    else
        // If last characters don't match, take the max by either moving `n` or `m`
        t[n][m] = max(LCS(n - 1, m, str1, str2), LCS(n, m - 1, str1, str2));

    return t[n][m];
}

int lcs(int n, int m, const string &str1, const string &str2) {
    // Initialize the memoization table with -1
    t.assign(n + 1, vector<int>(m + 1, -1));
    
    // Call the helper LCS function
    return LCS(n, m, str1, str2);
}

// top down approach
int lcs(int n, int m, const string &str1, const string &str2) {
    // Create a 2D DP table initialized with 0
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    // Build the DP table iteratively
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            // If characters match, add 1 to the result from previous indices
            if (str1[i - 1] == str2[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                // If characters don't match, take the maximum LCS by moving one index in either string
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    // The LCS length will be in the bottom-right cell of the DP table
    return dp[n][m];
}