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

//another O(n)
int AlternatingMaxLength(vector<int>& a) {
    int n = a.size();
    if (n == 1) return 1;

    int inc = 1; // Length of increasing subsequence
    int dec = 1; // Length of decreasing subsequence

    for (int i = 1; i < n; i++) {
        if (a[i] > a[i - 1]) {
            // Current element is greater, so extend the decreasing sequence
            inc = dec + 1;
        } else if (a[i] < a[i - 1]) {
            // Current element is smaller, so extend the increasing sequence
            dec = inc + 1;
        }
    }

    // The result is the maximum length of either an increasing or decreasing sequence
    return max(inc, dec);
}