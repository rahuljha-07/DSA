#include <bits/stdc++.h>
using namespace std;

int longestSubsequence(int n, int a[]) {
    // Create a dynamic programming array to store subsequence lengths
    int dp[n];
    
    // Initialize all elements of dp to 1, as every element is a subsequence of length 1 by itself
    for (int i = 0; i < n; i++) 
        dp[i] = 1;

    // Iterate over the array to fill the dp array
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            // Check if the absolute difference between elements is 1
            if (abs(a[i] - a[j]) == 1) {
                // Update dp[i] considering the subsequence ending at j
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }

    // Find the maximum value in the dp array
    int ma = 0;
    for (int i = 0; i < n; i++) {
        ma = max(ma, dp[i]);
    }

    return ma;
}

int main() {
    int n = 7;
    int a[] = {1, 2, 3, 4, 5, 3, 2};
    cout << "Length of the longest subsequence: " << longestSubsequence(n, a) << endl;
    return 0;
}
