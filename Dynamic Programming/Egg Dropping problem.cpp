#include <iostream>
#include <climits>
#include <cstring>
using namespace std;

class Solution {
public:
    // Memoization table to store results of subproblems
    int dp[201][201];

    /**
     * Function to solve the egg dropping problem recursively with memoization.
     * 
     * Parameters:
     * n: Number of eggs available.
     * k: Number of floors to test.
     * 
     * Steps:
     * 1. Base Cases:
     *    - If there is only 1 egg, we must test all floors (return k).
     *    - If there are 0 floors, no tests are needed (return 0).
     * 2. Recursive Case:
     *    - For each floor, calculate the result for:
     *      a) Egg breaks: Solve for (n-1) eggs and (i-1) floors below.
     *      b) Egg does not break: Solve for n eggs and (k-i) floors above.
     *    - Take the maximum of these two cases, as we need the worst-case scenario.
     *    - Keep track of the minimum attempts across all floor splits.
     * 3. Memoization:
     *    - Use the `dp` table to store results of subproblems to avoid redundant calculations.
     * 
     * Time Complexity: O(n * k^2) (n eggs and k floors, with nested loops for floor splits).
     * Space Complexity: O(n * k) (for the memoization table).
     */
    int solve(int n, int k) {
        // Base Cases
        if (n == 1) return k; // If we have only one egg, test all floors
        if (k == 0) return 0; // If there are no floors, no tests are needed

        // Check if result is already computed
        if (dp[n][k] != -1) return dp[n][k];

        int ans = INT_MAX; // Initialize the minimum attempts to a large value

        // Try dropping an egg from each floor and calculate the worst-case scenario
        for (int i = 1; i <= k; i++) {
            // Egg breaks: Check floors below
            int broken = solve(n - 1, i - 1);

            // Egg does not break: Check floors above
            int not_broken = solve(n, k - i);

            // Take the worst-case scenario of these two
            int maxval = max(broken, not_broken);

            // Update the minimum attempts
            ans = min(ans, maxval + 1);
        }

        // Store the result in the memoization table
        return dp[n][k] = ans;
    }

    /**
     * Main function to find the minimum number of attempts needed to find the critical floor.
     * 
     * Parameters:
     * n: Number of eggs.
     * k: Number of floors.
     */
    int eggDrop(int n, int k) {
        // Initialize the memoization table with -1
        memset(dp, -1, sizeof(dp));

        // Solve the problem using the helper function
        return solve(n, k);
    }
};

// Example usage
int main() {
    Solution sol;

    int n = 2; // Number of eggs
    int k = 10; // Number of floors

    cout << "Minimum number of attempts needed: " << sol.eggDrop(n, k) << endl;

    return 0;
}
