// Global DP table
vector<vector<int>> t;

int LRS(string x) {
    int n = x.length();
    string y = x; // Copy x into y

    // Initialize the global DP table with size (n+1) x (n+1)
    t = vector<vector<int>>(n + 1, vector<int>(n + 1, 0));

    // Fill the DP table
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (x[i - 1] == y[j - 1] && i != j) {
                // If characters match and indices are different
                t[i][j] = 1 + t[i - 1][j - 1];
            } else {
                // If characters don't match, take the maximum of left and top
                t[i][j] = max(t[i - 1][j], t[i][j - 1]);
            }
        }
    }

    // The value at t[n][n] contains the length of the LRS
    return t[n][n];
}