#include <bits/stdc++.h>
using namespace std;

// Global memoization table to store results of subproblems
vector<vector<int>> dp;

// Helper function that calculates the minimum cost to arrange words
int minCostHelper(int currWord, int remainingSpace, vector<int>& wordLengths, int &lineWidth) {
    // Base case: if we have processed all words, return 0 cost
    if (currWord == wordLengths.size()) {
        return 0;
    }

    // If the result is already computed for this subproblem, return it
    if (dp[currWord][remainingSpace] != -1) {
        return dp[currWord][remainingSpace];
    }

    int includeInSameLine = INT_MAX;  // Cost if we include the current word in the same line
    int spaceUsed = remainingSpace + 1 + wordLengths[currWord]; // Calculate the new space if we add this word

    // Continue on the same line if space allows
    if (spaceUsed <= lineWidth) {
        includeInSameLine = minCostHelper(currWord + 1, spaceUsed, wordLengths, lineWidth);
    }

    // Start a new line with the current word and add cost of extra spaces in the previous line
    int startNewLine = minCostHelper(currWord + 1, wordLengths[currWord], wordLengths, lineWidth) + 
                       (lineWidth - remainingSpace) * (lineWidth - remainingSpace);

    // Store and return the minimum of the two choices
    return dp[currWord][remainingSpace] = min(includeInSameLine, startNewLine);
}

// Main function that initializes memoization and calls the helper function
int solveWordWrap(vector<int> wordLengths, int lineWidth) { 
    int wordCount = wordLengths.size();
    dp.resize(wordCount + 1, vector<int>(lineWidth + 1, -1));
    return minCostHelper(1, wordLengths[0], wordLengths, lineWidth);
}


// Main function
int main() {
     int wordCount;
    cin >> wordCount;
    vector<int> wordLengths(wordCount);
    for (int i = 0; i < wordCount; i++) {
        cin >> wordLengths[i];
    }
    int lineWidth;
    cin >> lineWidth;
    
    cout << solveWordWrap(wordLengths, lineWidth) << endl;
    return 0;
}
