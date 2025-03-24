#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Helper function to check if interleaving is possible
bool isInterleave_helper(string s1, string s2, string s3, int i, int j, int k, vector<vector<int>> &m) {

    // If we have reached the end of both s1 and s2 and s3, return true
    if (i == s1.length() && j == s2.length() && k == s3.length()) {
        return true;
    }
    
    // If we have already computed this state, return the result
    if (m[i][j] != -1) {
        return m[i][j];
    }

    bool x = false, y = false;

    // If we have not reached the end of s1, check if we can take a character from s1
    if (i < s1.length() && s1[i] == s3[k]) {
        x = isInterleave_helper(s1, s2, s3, i + 1, j, k + 1, m);
    }

    // If we have not reached the end of s2, check if we can take a character from s2
    if (j < s2.length() && s2[j] == s3[k]) {
        y = isInterleave_helper(s1, s2, s3, i, j + 1, k + 1, m);
    }

    // Save the result of the current state and return it (Memoization)
    return m[i][j] = x || y;
}

// Main function to check if s3 is an interleaving of s1 and s2
bool isInterleave(string s1, string s2, string s3) {
    int a = s1.length(), b = s2.length();
    
    // Create a memoization table initialized to -1 (indicating not yet computed)
    vector<vector<int>> m(a + 1, vector<int>(b + 1, -1));
    
    // Start from the beginning of both strings and s3
    return isInterleave_helper(s1, s2, s3, 0, 0, 0, m);
}

int main() {
    string s1, s2, s3;
    cin >> s1 >> s2 >> s3;
    
    if (isInterleave(s1, s2, s3)) {
        cout << 1 << endl;  // Interleave possible
    } else {
        cout << 0 << endl;  // Interleave not possible
    }

    return 0;
}
