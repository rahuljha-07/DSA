#include <iostream>
#include <vector>
using namespace std;

// Memoization table
vector<vector<int>> memo;

// Helper function to perform recursive pattern matching with wildcards
bool matchPatternUtil(int patternIdx, int strIdx, int patternLen, int strLen, string pattern, string str) {
    // If both pattern and string are fully matched
    if (patternIdx == patternLen && strIdx == strLen) {
        return true;
    }

    // If string is fully matched but there are remaining characters in the pattern
    if (strIdx == strLen) {
        // Check if all remaining pattern characters are '*'
        for (int k = patternIdx; k < patternLen; k++) {
            if (pattern[k] != '*')
                return false;
        }
        return true;
    }

    // If pattern is fully matched but string is not
    if (patternIdx == patternLen) {
        return false;
    }
        
    // Check if result is already computed
    if (memo[patternIdx][strIdx] != -1) {
        return memo[patternIdx][strIdx];
    }

    bool result = false;
    
    // Case where pattern character is '?', matches any single character
    if (pattern[patternIdx] == '?') {
        result = matchPatternUtil(patternIdx + 1, strIdx + 1, patternLen, strLen, pattern, str);
    }

    // Case where pattern character is '*', matches any sequence of characters (including an empty sequence)
    if (pattern[patternIdx] == '*') {
        // Try matching '*' with an empty sequence or advancing the string index
        result = matchPatternUtil(patternIdx + 1, strIdx, patternLen, strLen, pattern, str) || 
                 matchPatternUtil(patternIdx, strIdx + 1, patternLen, strLen, pattern, str);
    }

    // Case where characters must match exactly
    else {
        if (pattern[patternIdx] == str[strIdx]) {
            result = matchPatternUtil(patternIdx + 1, strIdx + 1, patternLen, strLen, pattern, str);
        } else {
            result = false;
        }
    }

    // Store result before returning
    return memo[patternIdx][strIdx] = result;
}

// Main function to check if the pattern matches the string
int isPatternMatch(string pattern, string str) {
    int patternLen = pattern.length();
    int strLen = str.length();
    return matchPatternUtil(0, 0, patternLen, strLen, pattern, str);
}