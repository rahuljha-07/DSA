#include <iostream>
#include <vector>
#include <climits>
#include <cstring>

using namespace std;

class Solution {
public:
    // Memoization table to store results of subproblems using dynamic vector
    vector<vector<int>> dp;

    /**
     * Function to solve the egg dropping problem recursively with memoization.
     * 
     * Parameters:
     * e: Number of eggs available.
     * f: Number of floors to test.
     * 
     * Steps:
     * 1. Base Cases:
     *    - If there is only 1 egg, we must test all floors (return f).
     *    - If there are 0 floors, no tests are needed (return 0).
     * 2. Recursive Case:
     *    - For each floor, calculate the result for:
     *      a) Egg breaks: Solve for (n-1) eggs and (k-1) floors below.
     *      b) Egg does not break: Solve for n eggs and (f-k) floors above.
     *    - Take the maximum of these two cases, as we need the worst-case scenario.
     *    - Keep track of the minimum attempts across all floor splits.
     * 3. Memoization:
     *    - Use the `dp` table to store results of subproblems to avoid redundant calculations.
     * 
     * Time Complexity: O(n * f^2) (n eggs and k floors, with nested loops for floor splits).
     * Space Complexity: O(n * f) (for the memoization table).
     */
    int solve(int e, int f) {
        // Base Cases
        if (e == 1) return f; // If we have only one egg, test all floors
        if (f == 0) return 0; // If there are no floors, no tests are needed

        // Check if result is already computed
        if (dp[e][f] != -1) return dp[e][f];

        int ans = INT_MAX; // Initialize the minimum attempts to a large value

        // Try dropping an egg from each floor and calculate the worst-case scenario
        for (int k = 1; k <= f; k++) {
            // Egg breaks: Check floors below
            int broken = solve(e - 1, k- 1);

            // Egg does not break: Check floors above
            int not_broken = solve(e, f - k);

            // Take the worst-case scenario of these two
            int maxval = max(broken, not_broken);

            // Update the minimum attempts
            ans = min(ans, maxval + 1);
        }

        // Store the result in the memoization table
        return dp[e][f] = ans;
    }

    /**
     * Main function to find the minimum number of attempts needed to find the critical floor.
     * 
     * Parameters:
     * e: Number of eggs.
     * f: Number of floors.
     */
    int eggDrop(int e, int f) {
        // Initialize the memoization table with -1 using vector
        dp = vector<vector<int>>(e + 1, vector<int>(f + 1, -1));

        // Solve the problem using the helper function
        return solve(e, f);
    }
};

// Example usage
int main() {
    Solution sol;

    int e = 2; // Number of eggs
    int f = 10; // Number of floors

    cout << "Minimum number of attempts needed: " << sol.eggDrop(e, f) << endl;

    return 0;
}
