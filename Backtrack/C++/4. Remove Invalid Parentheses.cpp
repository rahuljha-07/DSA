#include <iostream>
#include <vector>
#include <unordered_map>
#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> validResults; // To store all valid results
    unordered_map<string, int> processedStrings; // Memoization to avoid reprocessing the same string

    // Function to calculate the minimum number of invalid parentheses
    int calculateMinInvalid(string s) {
        stack<char> parenthesesStack; // Stack to track unmatched parentheses
        for (char c : s) {
            if (c == '(') {
                parenthesesStack.push('('); // Push open parentheses onto the stack
            } else if (c == ')') {
                if (!parenthesesStack.empty() && parenthesesStack.top() == '(') {
                    parenthesesStack.pop(); // Balanced pair found, remove from stack
                } else {
                    parenthesesStack.push(')'); // Unmatched closing parentheses
                }
            }
        }
        return parenthesesStack.size(); // Remaining stack size is the count of invalid parentheses
    }

    // Recursive function to solve the problem
    void backtrack(string currentString, int remainingInvalid) {
        // Check if this string has already been processed
        if (processedStrings[currentString] != 0) {
            return;
        }
        // Mark this string as processed
        processedStrings[currentString]++;

        // Base case: If no invalid parentheses remain
        if (remainingInvalid == 0) {
            // Check if the current string is valid
            if (calculateMinInvalid(currentString) == 0) {
                validResults.push_back(currentString); // Add to results if valid
            }
            return;
        }

        // Try removing each character in the string
        for (int i = 0; i < currentString.size(); i++) {
            // Skip removing non-parentheses characters
            if (currentString[i] != '(' && currentString[i] != ')') {
                continue;
            }

            // Create a new string by excluding the current character
            string newString = currentString.substr(0, i) + currentString.substr(i + 1);

            // Recurse with the new string and decrement the remaining invalid count
            backtrack(newString, remainingInvalid - 1);
        }
    }

    // Main function to remove invalid parentheses
    vector<string> removeInvalidParentheses(string s) {
        // Calculate the minimum number of invalid parentheses
        int minInvalidCount = calculateMinInvalid(s);

        // Start backtracking to generate all valid strings
        backtrack(s, minInvalidCount);

        return validResults; // Return the list of valid results
    }
};

int main() {
    // Example usage
    Solution solution;
    string input = "(a)())()";

    vector<string> results = solution.removeInvalidParentheses(input);

    cout << "Valid strings after removing invalid parentheses:\n";
    for (const string& result : results) {
        cout << result << endl;
    }

    return 0;
}
