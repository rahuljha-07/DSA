#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

// Helper function for recursion + memoization
int editDistanceMemoHelper(string &s1, string &s2, int i, int j, vector<vector<int>> &dp) {
    // Base cases
    if (i == s1.length()) return s2.length() - j; // Insert remaining characters of s2
    if (j == s2.length()) return s1.length() - i; // Remove remaining characters of s1

    // If already computed, return the stored result
    if (dp[i][j] != -1) return dp[i][j];

    // If characters are the same, no operation is needed
    if (s1[i] == s2[j]) {
        return dp[i][j] = editDistanceMemoHelper(s1, s2, i + 1, j + 1, dp);
    }

    // Try all three operations and take the minimum
    int insertOp = 1 + editDistanceMemoHelper(s1, s2, i, j + 1, dp); // Insert
    int removeOp = 1 + editDistanceMemoHelper(s1, s2, i + 1, j, dp); // Remove
    int replaceOp = 1 + editDistanceMemoHelper(s1, s2, i + 1, j + 1, dp); // Replace

    return dp[i][j] = min({insertOp, removeOp, replaceOp});
}

// Main function
int editDistanceMemo(string s1, string s2) {
    int m = s1.length();
    int n = s2.length();

    // Initialize DP table with -1
    vector<vector<int>> dp(m, vector<int>(n, -1));

    return editDistanceMemoHelper(s1, s2, 0, 0, dp);
}

int main() {
    string s1 = "geek", s2 = "gesek";
    cout << "Edit Distance (Memoization): " << editDistanceMemo(s1, s2) << endl;
    return 0;
}
