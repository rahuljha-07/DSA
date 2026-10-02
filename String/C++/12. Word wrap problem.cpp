#include <bits/stdc++.h>
using namespace std;

// Global memoization table to store results of subproblems
vector<vector<int>> dp;

// Helper function that calculates the minimum cost to arrange words
int findMinCost(int wordIndex, int currentLineWidth, vector<int>& wordLengths, int &maxLineWidth) {
    // Base case: if we have processed all words, return 0 cost
    if (wordIndex == wordLengths.size()) {
        return 0;
    }

    // If the result is already computed for this subproblem, return it
    if (dp[wordIndex][currentLineWidth] != -1) {
        return dp[wordIndex][currentLineWidth];
    }

    int costIfSameLine = INT_MAX;  // Cost if we include the current word in the same line
    int newLineWidth = currentLineWidth + 1 + wordLengths[wordIndex]; // Calculate new space if we add this word

    // Continue on the same line if space allows
    if (newLineWidth <= maxLineWidth) {
        costIfSameLine = findMinCost(wordIndex + 1, newLineWidth, wordLengths, maxLineWidth);
    }

    // Start a new line with the current word and add cost of extra spaces in the previous line
    int costIfNewLine = findMinCost(wordIndex + 1, wordLengths[wordIndex], wordLengths, maxLineWidth) + 
                        (maxLineWidth - currentLineWidth) * (maxLineWidth - currentLineWidth);

    // Store and return the minimum of the two choices
    return dp[wordIndex][currentLineWidth] = min(costIfSameLine, costIfNewLine);
}

// Main function that initializes memoization and calls the helper function
int solveWordWrap(vector<int> wordLengths, int maxLineWidth) { 
    int totalWords = wordLengths.size();
    dp.resize(totalWords + 1, vector<int>(maxLineWidth + 1, -1));
    return findMinCost(1, wordLengths[0], wordLengths, maxLineWidth);
}

// Main function
int main() {
    int totalWords;
    cin >> totalWords;
    vector<int> wordLengths(totalWords);
    
    for (int i = 0; i < totalWords; i++) {
        cin >> wordLengths[i];
    }
    
    int maxLineWidth;
    cin >> maxLineWidth;
    
    cout << solveWordWrap(wordLengths, maxLineWidth) << endl;
    return 0;
}
