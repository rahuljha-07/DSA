#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    // Memoization map to store results of subproblems
    unordered_map<string, bool> m;

    /**
     * Function to check if one string is a scrambled version of another.
     *
     * Steps:
     * 1. Base Case:
     *    - If the two strings are equal, return true.
     *    - If the length of the string is 1 and not equal, return false.
     * 2. Recursive Case:
     *    - Split the string into two parts at every possible index.
     *    - Check both conditions:
     *      a) Without swapping: First part of s1 matches the first part of s2,
     *         and the second part of s1 matches the second part of s2.
     *      b) With swapping: First part of s1 matches the last part of s2,
     *         and the second part of s1 matches the first part of s2.
     * 3. Memoization:
     *    - Use a map with keys as concatenated strings `s1 + " " + s2`
     *      to store and reuse results of subproblems.
     *
     * Time Complexity: O(n^4) (due to substring operations and recursive calls)
     * Space Complexity: O(n^2) (for memoization map)
     */
    bool isScramble(string s1, string s2) {
        // Create a unique key for memoization
        string key = s1 + " " + s2;

        // Check if the result is already computed
        if (m.find(key) != m.end()) {
            return m[key]; // Return the stored result if it exists
        }

        // Base Case: If the strings are identical, they are scrambled versions
        if (s1 == s2) {
            return m[key] = true;
        }

        // Base Case: If the length of the strings is 1 and they are not equal
        if (s1.length() <= 1) {
            return m[key] = false;
        }

        int n = s1.length(); // Length of the strings
        bool flag = false;   // Initialize result to false

        // Try splitting the string at every possible index
        for (int i = 1; i <= n - 1; i++) {
            // Without swapping:
            // Check if the first part of s1 matches the first part of s2
            // AND the second part of s1 matches the second part of s2
            if (isScramble(s1.substr(0, i), s2.substr(0, i)) &&
                isScramble(s1.substr(i), s2.substr(i))) {
                flag = true; // The strings are scrambled versions
                break;
            }

            // With swapping:
            // Check if the first part of s1 matches the last part of s2
            // AND the second part of s1 matches the first part of s2
            if (isScramble(s1.substr(0, i), s2.substr(n - i, i)) &&
                isScramble(s1.substr(i), s2.substr(0, n - i))) {
                flag = true; // The strings are scrambled versions
                break;
            }
        }

        // Store the result in the memoization map
        return m[key] = flag;
    }
};

// Example usage
int main() {
    Solution sol;

    // Example input
    string s1 = "great";
    string s2 = "rgeat";

    // Check if s2 is a scrambled version of s1
    if (sol.isScramble(s1, s2)) {
        cout << "Yes, " << s2 << " is a scrambled version of " << s1 << endl;
    } else {
        cout << "No, " << s2 << " is not a scrambled version of " << s1 << endl;
    }

    return 0;
}
