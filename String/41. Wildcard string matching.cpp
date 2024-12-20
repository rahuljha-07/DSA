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

    // Case where pattern character is '?', matches any single character
    if (pattern[patternIdx] == '?') {
        return matchPatternUtil(patternIdx + 1, strIdx + 1, patternLen, strLen, pattern, str);
    }

    // Case where pattern character is '*', matches any sequence of characters (including an empty sequence)
    if (pattern[patternIdx] == '*') {
        // Try matching '*' with an empty sequence or advancing the string index
        return matchPatternUtil(patternIdx + 1, strIdx, patternLen, strLen, pattern, str) || 
               matchPatternUtil(patternIdx, strIdx + 1, patternLen, strLen, pattern, str);
    }

    // Case where pattern character is a regular character that doesn't match the string character
    if (pattern[patternIdx] != str[strIdx]) {
        return false;
    }

    // Regular character match, move to the next character in both pattern and string
    return matchPatternUtil(patternIdx + 1, strIdx + 1, patternLen, strLen, pattern, str);
}

// Main function to check if the pattern matches the string
int isPatternMatch(string pattern, string str) {
    int patternLen = pattern.length();
    int strLen = str.length();
    return matchPatternUtil(0, 0, patternLen, strLen, pattern, str);
}