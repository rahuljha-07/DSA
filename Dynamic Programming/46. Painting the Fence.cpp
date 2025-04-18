#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int totalWays = 0; // To count the total valid ways
    vector<vector<vector<int>>> dp; // Memoization table

    int solve(int idx, string str, int n, int k, int lastColor, int count) {
        // Base case: If all posts are painted
        if (idx == n) {
            cout << str << endl; // Print the valid pattern
            return 1; // Valid pattern found
        }

        // Check if the result is already computed
        if (dp[idx][lastColor][count] != -1) {
            return dp[idx][lastColor][count];
        }

        int ways = 0; // To accumulate valid ways from this state

        // Iterate through all possible colors
        for (int i = 1; i <= k; i++) {
            if (i == lastColor) {
                // If the same color as last, ensure not more than 2 consecutively
                if (count < 2) {
                    ways += solve(idx + 1, str + to_string(i), n, k, i, count + 1);
                }
            } else {
                // Different color, reset consecutive count
                ways += solve(idx + 1, str + to_string(i), n, k, i, 1);
            }
        }

        // Store the result in the memoization table and return
        return dp[idx][lastColor][count] = ways;
    }

    int countWays(int n, int k) {

        // Initialize the memoization table with -1
        dp = vector<vector<vector<int>>>(n, vector<vector<int>>(k + 1, vector<int>(3, -1)));

        // Start the recursive process
        return solve(0, "", n, k, 0, 0);
    }
};

// Example usage
int main() {
    Solution sol;

    int n = 3; // Number of posts
    int k = 4; // Number of colors

    cout << "Valid ways to paint the fence:\n";
    int total = sol.countWays(n, k);
    cout << "Total valid ways: " << total << endl;

    return 0;
}
