#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    // Memoization map to store results of subproblems
    unordered_map<string, int> m;

    // Recursive function to solve the Boolean Parenthesization problem
    int solve(int i, int j, string s, bool isTrue) {
        // Base case: if the start index is greater than the end index
        if (i > j) {
            return 0; // No valid expression
        }

        // Base case: if the expression has only one character
        if (i == j) {
            if (isTrue) {
                // If we need the result to be True
                return s[i] == 'T' ? 1 : 0; // 'T' = 1, 'F' = 0
            } else {
                // If we need the result to be False
                return s[i] == 'F' ? 1 : 0; // 'F' = 1, 'T' = 0
            }
        }

        // Create a unique key for the memoization map
        string temp = to_string(i) + " " + to_string(j) + " " + to_string(isTrue);

        // Check if the result is already computed
        if (m.find(temp) != m.end()) {
            return m[temp]; // Return the stored result if exists
        }

        int ans = 0; // Initialize the result

        // Loop through the string to split it at each operator
        for (int k = i + 1; k <= j - 1; k = k + 2) {
            // Recursively calculate the number of True and False values for left and right sub-expressions
            int leftTrue = solve(i, k - 1, s, true);   // Left part of the expression needs to be True
            int leftFalse = solve(i, k - 1, s, false); // Left part of the expression needs to be False
            int rightTrue = solve(k + 1, j, s, true);  // Right part of the expression needs to be True
            int rightFalse = solve(k + 1, j, s, false); // Right part of the expression needs to be False

            // Handle each operator between the two sub-expressions
            if (s[k] == '&') {
                // AND operation
                if (isTrue) {
                    ans += leftTrue * rightTrue; // True if both sides are True
                } else {
                    ans += leftTrue * rightFalse + leftFalse * rightTrue + leftFalse * rightFalse;
                    // False if any one side is False
                }
            }

            if (s[k] == '|') {
                // OR operation
                if (isTrue) {
                    ans += leftTrue * rightTrue + leftFalse * rightTrue + leftTrue * rightFalse;
                    // True if any one side is True
                } else {
                    ans += leftFalse * rightFalse; // False only if both sides are False
                }
            }

            if (s[k] == '^') {
                // XOR operation
                if (isTrue) {
                    ans += leftTrue * rightFalse + leftFalse * rightTrue;
                    // True if one side is True and the other side is False
                } else {
                    ans += leftTrue * rightTrue + leftFalse * rightFalse;
                    // False if both sides are the same
                }
            }
        }

        // Store the result in the memoization map to avoid redundant calculations
        return m[temp] = ans;
    }

    // Function to count the number of ways to parenthesize the expression to get True
    int countWays(int n, string s) {
        int i = 0, j = n - 1;
        // Solve for the full range [i, j] with the result being True
        int ans = solve(i, j, s, true);
        return ans;
    }
};

// Example Usage
int main() {
    Solution sol;
    string s = "T|T&F^T"; // Example input expression
    int n = s.length();

    // Calculate the number of ways to parenthesize the expression to get True
    cout << "Number of ways to evaluate the expression to True: " << sol.countWays(n, s) << endl;

    return 0;
}
