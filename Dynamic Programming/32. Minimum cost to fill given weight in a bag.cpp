#include <iostream>
#include <vector>
#include <climits>
using namespace std;

// Helper function for recursion with memoization
int minimumCostHelper(int w, int cost[], int n, vector<vector<int>> &dp) {
    // Base cases
    if (w == 0) return 0;          // No weight to fill, cost is 0
    if (n == 0 || w < 0) return INT_MAX; // No items left or invalid weight

    // If already computed, return the stored value
    if (dp[n][w] != -1) return dp[n][w];

    // Exclude the current packet
    int exclude = minimumCostHelper(w, cost, n - 1, dp);

    // Include the current packet if it's available
    int include = INT_MAX;
    if (cost[n - 1] != -1 && w >= n) { // Only include if cost is valid and weight is sufficient
        int subProblem = minimumCostHelper(w - n, cost, n, dp);
        if (subProblem != INT_MAX) { // Ensure the subproblem is solvable
            include = cost[n - 1] + subProblem;
        }
    }

    // Store the result in dp
    return dp[n][w] = min(include, exclude);
}

int minimumCost(int w, int cost[], int n) {
    // Create a memoization table initialized to -1
    vector<vector<int>> dp(n + 1, vector<int>(w + 1, -1));

    int result = minimumCostHelper(w, cost, n, dp);

    // If the result is INT_MAX, it means the weight cannot be achieved
    return (result == INT_MAX) ? -1 : result;
}

int main() {
    int cost1[] = {20, 10, 4, 50, 100};
    int n1 = 5, w1 = 5;
    cout << "Minimum cost: " << minimumCost(w1, cost1, n1) << endl;

    int cost2[] = {-1, -1, 4, 3, -1};
    int n2 = 5, w2 = 5;
    cout << "Minimum cost: " << minimumCost(w2, cost2, n2) << endl;

    return 0;
}
