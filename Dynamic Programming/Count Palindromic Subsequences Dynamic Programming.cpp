#include <iostream>
#include <cstring> // For memset
#include <string>
using namespace std;

// DP array for memoization
int dp[1001][1001];

// Helper function using recursion and memoization
int func(int i, int j, string &s) {
    if (i > j) return 0; // Base case: invalid range
    if (i == j) return 1; // Base case: single character is a palindrome

    if (dp[i][j] != -1) return dp[i][j]; // Return cached result if already computed

    if (s[i] == s[j]) {
        // Characters match
        return dp[i][j] = func(i + 1, j, s) + func(i, j - 1, s) + 1;
    } else {
        // Characters don't match
        return dp[i][j] = func(i + 1, j, s) + func(i, j - 1, s) - func(i + 1, j - 1, s);
    }
}

// Main function to count palindromic subsequences
int countPS(string str) {
    int n = str.length();
    memset(dp, -1, sizeof(dp)); // Initialize the DP array with -1
    return func(0, n - 1, str); // Call the recursive function for the entire string
}

int main() {
    string str;
    cout << "Enter the string: ";
    cin >> str;

    cout << "Number of Palindromic Subsequences: " << countPS(str) << endl;

    return 0;
}
