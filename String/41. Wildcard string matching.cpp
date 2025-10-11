#include <iostream>
#include <vector>
using namespace std;

// Memoization table
vector<vector<int>> memo;

// Helper function to perform recursive pattern matching with wildcards
bool matchPatternUtil(int patternIdx, int strIdx, int patternLen, int strLen, const string& pattern, const string& str) {
    if (patternIdx == patternLen && strIdx == strLen) {
        return true;
    }
    else if (strIdx == strLen) {
        for (int k = patternIdx; k < patternLen; k++) {
            if (pattern[k] != '*') {
                return false;
            }
        }
        return true;
    }
    else if (patternIdx == patternLen) {
        return false;
    }
    else if (memo[patternIdx][strIdx] != -1) {
        return memo[patternIdx][strIdx];
    }

    bool result = false;

    if (pattern[patternIdx] == str[strIdx]) {
        result = matchPatternUtil(patternIdx + 1, strIdx + 1, patternLen, strLen, pattern, str);
    }
    else if (pattern[patternIdx] == '?') {
        result = matchPatternUtil(patternIdx + 1, strIdx + 1, patternLen, strLen, pattern, str);
    }
    else if (pattern[patternIdx] == '*') {
        result = matchPatternUtil(patternIdx + 1, strIdx, patternLen, strLen, pattern, str) ||
                 matchPatternUtil(patternIdx, strIdx + 1, patternLen, strLen, pattern, str);
    }
    else {
        result = false;
    }

    return memo[patternIdx][strIdx] = result;
}

// Main function to check if the pattern matches the string
int isPatternMatch(string pattern, string str) {
    int patternLen = pattern.length();
    int strLen = str.length();
    memo.resize(patternLen + 1, vector<int>(strLen + 1, -1)); // Resize and initialize memo table
    return matchPatternUtil(0, 0, patternLen, strLen, pattern, str);
}