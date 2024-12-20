
// Recursive helper function to compute the minimum edit distance
int minDistanceHelper(string& word1, string& word2, vector<vector<int>>& dp, int i, int j) {
    // If the value has already been computed, return it
    if (dp[i][j] != -1) {
        return dp[i][j];
    }
    
    // If the first string is empty, the only option is to insert all characters of the second string
    if (i == 0) {
        return dp[i][j] = j; // Cost of inserting all j characters
    }

    // If the second string is empty, the only option is to remove all characters of the first string
    if (j == 0) {
       return dp[i][j] = i; // Cost of deleting all i characters
    }

    // If the last characters of the two strings are the same, no operation is needed
    if (word1[i - 1] == word2[j - 1]) {
       return dp[i][j] = minDistanceHelper(word1, word2, dp, i - 1, j - 1);
    } else {
        // Calculate costs for the three possible operations
        int insertOp = minDistanceHelper(word1, word2, dp, i, j - 1);      // Insert
        int deleteOp = minDistanceHelper(word1, word2, dp, i - 1, j);      // Delete
        int replaceOp = minDistanceHelper(word1, word2, dp, i - 1, j - 1); // Replace

        // Store the minimum cost among the three operations
       return dp[i][j] = 1 + min({insertOp, deleteOp, replaceOp});
    }
    
}

// Main function to calculate the minimum edit distance between two strings
int minDistance(string word1, string word2) {
    int m = word1.size(), n = word2.size(); // Get lengths of both strings

    // Create a memoization table initialized to -1
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
    
    // Call the helper function starting from the end of both strings
    return minDistanceHelper(word1, word2, dp, m, n);
}
