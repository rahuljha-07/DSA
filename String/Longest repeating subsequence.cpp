#include <iostream>
#include <string>
#include <vector>
using namespace std;


#include <iostream>
#include <string>
#include <vector>
#include <cstring> // For memset
using namespace std;

//recursion + memorization[bottom up approach]
// Global memoization table
int t[1001][1001]; // Adjust size as needed

// Helper function to calculate the length of the longest repeating subsequence
int LRSUtil(const string& str, int i, int j) {
    // Base case: if we have reached the end of either string
    if (i == 0 || j == 0) {
        return 0; // No further characters to compare
    }

    // If the result has already been computed, return it
    if (t[i][j] != -1) {
        return t[i][j];
    }

    // If characters match and are not at the same index
    if (str[i - 1] == str[j - 1] && i != j) {
        t[i][j] = 1 + LRSUtil(str, i - 1, j - 1); // Include this character
    } else {
        // Otherwise, take the maximum of excluding either character
        t[i][j] = max(LRSUtil(str, i, j - 1), LRSUtil(str, i - 1, j));
    }

    return t[i][j]; // Return the computed result
}

// Function to find the length of the longest repeating subsequence
int LongestRepeatingSubsequence(string str) {
    int n = str.length(); // Length of the input string

    // Initialize the memoization table with -1
    memset(t, -1, sizeof(t));

    // Call the utility function starting from the full length of the string
    return LRSUtil(str, n, n);
}


// top down approach
int LongestRepeatingSubsequence(string str) {
    int n = str.length(); // Length of the input string
    string str1 = str;    // Create a copy of the input string for comparison
    int m = n;            // Length of the copied string (same as the original)

    // Create a 2D array to store lengths of longest repeating subsequence
    int t[n + 1][m + 1]; 

    // Initialize the first column of the array to 0
    for (int i = 0; i < n + 1; i++) 
        t[i][0] = 0;

    // Initialize the first row of the array to 0
    for (int j = 0; j < m + 1; j++) 
        t[0][j] = 0;

    // Fill the table in a bottom-up manner
    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < m + 1; j++) {
            // If characters match and indices are not the same, it's part of the repeating subsequence
            if (str[i - 1] == str1[j - 1] && i != j) {
                t[i][j] = 1 + t[i - 1][j - 1]; // Increase length by 1
            } else {
                // Otherwise, take the maximum of excluding either character
                t[i][j] = max(t[i][j - 1], t[i - 1][j]);
            }
        }
    }
    
    // The length of the longest repeating subsequence is found in the bottom-right cell
    return t[n][m];
}

int main() {
    string s = "AABEBCDD"; // Example input
    cout << "Length of Longest Repeating Subsequence: " << LongestRepeatingSubsequence(s) << endl;
    return 0;
}
