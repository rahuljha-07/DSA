#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int AlternatingMaxLength(vector<int>& a) {
    int n = a.size();
    if (n == 1) return 1;

    // DP table to store LAS lengths
    vector<vector<int>> dp(n, vector<int>(2, 1)); // dp[i][0]: decreasing, dp[i][1]: increasing

    int maxLength = 1; // To track the maximum length of LAS

    // Populate the DP table
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            // If a[i] > a[j], it can extend an increasing subsequence
            if (a[i] > a[j] && dp[i][1] < dp[j][0] + 1) {
                dp[i][1] = dp[j][0] + 1;
            }
            // If a[i] < a[j], it can extend a decreasing subsequence
            if (a[i] < a[j] && dp[i][0] < dp[j][1] + 1) {
                dp[i][0] = dp[j][1] + 1;
            }
        }
        // Update the maximum length
        maxLength = max(maxLength, max(dp[i][0], dp[i][1]));
    }

    return maxLength;
}

int main() {
    vector<int> a = {1, 5, 4, 9, 2};
    cout << "Length of Longest Alternating Subsequence: " << AlternatingMaxLength(a) << endl;
    return 0;
}