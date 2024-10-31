#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Function to build the prefix table (longest prefix suffix array) for the pattern
vector<int> buildPrefixTable(const string& pattern) {
    int patternLength = pattern.size();
    vector<int> prefixTable(patternLength, 0);
    int j = 0;  // Length of previous longest prefix suffix

    // Build the prefix table
    for (int i = 1; i < patternLength; i++) {
        while (j > 0 && pattern[i] != pattern[j]) {
            j = prefixTable[j - 1];  // Fallback in the prefix table
        }
        if (pattern[i] == pattern[j]) {
            j++;
        }
        prefixTable[i] = j;
    }
    return prefixTable;
}

// KMP search function to find all occurrences of the pattern in the text
vector<int> kmpSearch(const string& text, const string& pattern) {
    vector<int> prefixTable = buildPrefixTable(pattern);
    vector<int> matchIndices;  // To store the starting indices of all matches
    int j = 0;  // Index for pattern

    // Traverse the text
    for (int i = 0; i < text.size(); i++) {
        while (j > 0 && text[i] != pattern[j]) {
            j = prefixTable[j - 1];  // Fallback in the prefix table
        }
        if (text[i] == pattern[j]) {
            j++;
        }
        if (j == pattern.size()) {
            matchIndices.push_back(i - j + 1);  // Match found; store index
            j = prefixTable[j - 1];  // Reset j based on prefix table
        }
    }
    return matchIndices;
}

int main() {
    string text = "ABABDABACDABABCABAB";
    string pattern = "ABABCABAB";

    vector<int> result = kmpSearch(text, pattern);

    // Output the result
    cout << "Pattern found at indices: ";
    for (int index : result) {
        cout << index << " ";
    }
    cout << endl;

    return 0;
}
