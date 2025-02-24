#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Global memoization table
vector<vector<int>> t;

// Function to compute LCS
int LCS(string &x, string &y, int n, int m) {
    // Base case: If either string is empty, LCS is 0
    if (n == 0 || m == 0) {
        return 0;
    }

    // If the value is already computed, return it
    if (t[n][m] != -1) {
        return t[n][m];
    }

    // If the last characters match, add 1 to the result of the remaining strings
    if (x[n - 1] == y[m - 1]) {
        t[n][m] = 1 + LCS(x, y, n - 1, m - 1);
    } else {
        // If the last characters do not match, take the maximum LCS by excluding
        // one character from either string
        t[n][m] = max(LCS(x, y, n - 1, m), LCS(x, y, n, m - 1));
    }

    return t[n][m];
}

// Helper function to initialize the memoization table and compute LCS
int computeLCS(string x, string y) {
    int n = x.length();
    int m = y.length();

    // Resize and initialize the memoization table with -1
    t.resize(n + 1, vector<int>(m + 1, -1));

    return LCS(x, y, n, m);
}

int main() {
    string x = "AGGTAB";
    string y = "GXTXAYB";

    // Compute the LCS
    cout << "Length of LCS: " << computeLCS(x, y) << endl;

    return 0;
}

//bottom up
int LCS(string x, string y) {
    int n = x.length();
    int m = y.length();

    // Create a 2D DP table to store lengths of LCS
    vector<vector<int>> t(n + 1, vector<int>(m + 1, 0));

    // Fill the DP table
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (x[i - 1] == y[j - 1]) {
                // If characters match, add 1 to the previous diagonal value
                t[i][j] = 1 + t[i - 1][j - 1];
            } else {
                // If characters don't match, take the maximum of left and top
                t[i][j] = max(t[i - 1][j], t[i][j - 1]);
            }
        }
    }

    // The value at t[n][m] contains the length of the LCS
    return t[n][m];
}