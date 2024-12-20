#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<vector<int>> memo; // Memoization table

// Helper function to calculate LCS using memoization
int LCS(int n, int m, const string &str1, const string &str2) {
    // Base case: if either string is empty, the LCS is 0
    if (n == 0 || m == 0)
        return 0;

    // Check if the result is already calculated
    if (memo[n][m] != -1)
        return memo[n][m];

    // If the last characters match, add 1 to the result and move both indices
    if (str1[n - 1] == str2[m - 1])
        memo[n][m] = 1 + LCS(n - 1, m - 1, str1, str2);
    else
        // If last characters don't match, take the max by either moving `n` or `m`
        memo[n][m] = max(LCS(n - 1, m, str1, str2), LCS(n, m - 1, str1, str2));

    return memo[n][m];
}

// Main function to initialize memoization table and call LCS
int lcs(int n, int m, const string &str1, const string &str2) {
    // Initialize the memoization table with -1
    memo = vector<vector<int>>(n + 1, vector<int>(m + 1, -1));
    
    // Call the helper LCS function
    return LCS(n, m, str1, str2);
}

// Function to transform string A into string B
int transform(string A, string B) {
    // Calculate LCS length
    int lcsLength = lcs(A.length(), B.length(), A, B);
    
    // bascially we will delete char from A to make LCS and add remaining char from B to make B
    // Number of deletions needed to transform A into B
    int numDeletions = A.length() - lcsLength;
    // Number of insertions needed to transform A into B
    int numInsertions = B.length() - lcsLength;


    // Return total number of operations (insertions + deletions)
    return numInsertions + numDeletions;
}
