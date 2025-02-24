#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Global memoization table
vector<vector<vector<int>>> t;

// Function to compute LCS of three strings using Memoization (Top-Down)
int LCS3_TopDown(string &x, string &y, string &z, int n, int m, int o) {
    // Base case: If any string is empty, LCS is 0
    if (n == 0 || m == 0 || o == 0) {
        return 0;
    }

    // If the value is already computed, return it
    if (t[n][m][o] != -1) {
        return t[n][m][o];
    }

    // If the last characters of all three strings match
    if (x[n - 1] == y[m - 1] && y[m - 1] == z[o - 1]) {
        t[n][m][o] = 1 + LCS3_TopDown(x, y, z, n - 1, m - 1, o - 1);
    } else {
        // Otherwise, consider all possible cases and take the maximum
        t[n][m][o] = max({
            LCS3_TopDown(x, y, z, n - 1, m, o),
            LCS3_TopDown(x, y, z, n, m - 1, o),
            LCS3_TopDown(x, y, z, n, m, o - 1)
        });
    }

    return t[n][m][o];
}

// Helper function to initialize memoization table and compute LCS of three strings
int computeLCS3_TopDown(string x, string y, string z) {
    int n = x.length();
    int m = y.length();
    int o = z.length();

    // Resize and initialize the memoization table with -1
    t.assign(n + 1, vector<vector<int>>(m + 1, vector<int>(o + 1, -1)));

    return LCS3_TopDown(x, y, z, n, m, o);
}

// Function to compute LCS of three strings using Tabulation (Bottom-Up)
int LCS3_BottomUp(string x, string y, string z) {
    int n = x.length();
    int m = y.length();
    int o = z.length();

    // Create a 3D DP table
    vector<vector<vector<int>>> dp(n + 1, vector<vector<int>>(m + 1, vector<int>(o + 1, 0)));

    // Fill the DP table
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            for (int k = 1; k <= o; k++) {
                if (x[i - 1] == y[j - 1] && y[j - 1] == z[k - 1]) {
                    // If characters of all three strings match
                    dp[i][j][k] = 1 + dp[i - 1][j - 1][k - 1];
                } else {
                    // Otherwise, take the maximum
                    dp[i][j][k] = max({
                        dp[i - 1][j][k],
                        dp[i][j - 1][k],
                        dp[i][j][k - 1]
                    });
                }
            }
        }
    }

    // The value at dp[n][m][o] contains the length of the LCS of three strings
    return dp[n][m][o];
}

int main() {
    string s1 = "geeks";
    string s2 = "geeksfor";
    string s3 = "geeksforgeeks";

    // Compute the LCS of three strings using Top-Down Approach
    cout << "Length of LCS of three strings (Top-Down): " << computeLCS3_TopDown(s1, s2, s3) << endl;

    // Compute the LCS of three strings using Bottom-Up Approach
    cout << "Length of LCS of three strings (Bottom-Up): " << LCS3_BottomUp(s1, s2, s3) << endl;

    return 0;
}
