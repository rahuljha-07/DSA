/*
LCS dp code is exactly same , just we have to write one func which will iterate on the dp table to print
*/
#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Function to print LCS by backtracking the DP table
void printLCS(string x, string y, vector<vector<int>> &t) {
    int i = x.length(); // Length of string x
    int j = y.length(); // Length of string y

    string lcs = ""; // To store the LCS characters

    // Backtrack from t[i][j] to t[0][0]
    while (i > 0 && j > 0) {
        if (x[i - 1] == y[j - 1]) {
            // If characters match, add it to the LCS and move diagonally
            lcs = x[i - 1] + lcs;
            i--;
            j--;
        } else if (t[i - 1][j] > t[i][j - 1]) {
            // If the value above is greater, move up
            i--;
        } else {
            // Otherwise, move left
            j--;
        }
    }

    // Print the LCS
    cout << "LCS: " << lcs << endl;
}
