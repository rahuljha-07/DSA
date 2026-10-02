#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    // Memoization table: idx -> {current_subsequence, count of palindromic subsequences}
    unordered_map<int, pair<string, int>> dp;

    bool isPalindrome(const string& str) {
        int l = 0, r = str.size() - 1;
        while (l < r) {
            if (str[l++] != str[r--]) return false;
        }
        return true;
    }

    int solve(int idx, string current, string s) {
        // Base case: When we reach the end of the string
        if (idx == s.size()) {
            if (!current.empty() && isPalindrome(current)) {
                cout << "Palindrome Subsequence: " << current << endl;
                return 1;
            }
            return 0;
        }

        // Memoization check: if the current state is already computed
        if (dp.find(idx) != dp.end() && dp[idx].first == current) {
            return dp[idx].second;
        }

        // Choice 1: Include the current character
        int pick = solve(idx + 1, current + s[idx], s);

        // Choice 2: Exclude the current character
        int notPick = solve(idx + 1, current, s);

        // Store the result in the memoization table
        dp[idx] = {current, pick + notPick};

        return dp[idx].second;
    }

    int countPalindromicSubsequences(string s) {
        dp.clear(); // Clear the memoization table
        return solve(0, "", s);
    }

};

// Example usage
int main() {
    Solution sol;

    string s1 = "abcd";
    cout << "Input: " << s1 << endl;
    cout << "Total Palindromic Subsequences: " 
         << sol.countPalindromicSubsequences(s1) << endl << endl;

    string s2 = "aab";
    cout << "Input: " << s2 << endl;
    cout << "Total Palindromic Subsequences: " 
         << sol.countPalindromicSubsequences(s2) << endl << endl;

    string s3 = "b";
    cout << "Input: " << s3 << endl;
    cout << "Total Palindromic Subsequences: " 
         << sol.countPalindromicSubsequences(s3) << endl;

    return 0;
}
