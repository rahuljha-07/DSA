#include <iostream>
#include <vector>
using namespace std;

// Global memoization table
vector<vector<int>> t;

// Unbounded Knapsack: Top-Down Approach
int unboundedKnapsack(int wt[], int val[], int W, int n) {
    // Base case: if no items are left or capacity is 0
    if (n == 0 || W == 0)
        return 0;

    // Check if the result is already computed
    if (t[n][W] != -1)
        return t[n][W];

    // If the weight of the nth item is less than or equal to the remaining capacity
    if (wt[n - 1] <= W) {
        // Include the nth item (reuse it) or exclude it
        t[n][W] = max(
            val[n - 1] + unboundedKnapsack(wt, val, W - wt[n - 1], n), // Include the item (reuse it)
            unboundedKnapsack(wt, val, W, n - 1)                      // Exclude the item
        );
    } else {
        // If the weight of the nth item exceeds the remaining capacity, exclude it
        t[n][W] = unboundedKnapsack(wt, val, W, n - 1);
    }

    return t[n][W];
}

int main() {
    // Sample inputs
    int wt[] = {1, 3, 4, 5};  // Weights of the items
    int val[] = {10, 40, 50, 70}; // Values of the items
    int W = 8;                // Maximum capacity of the knapsack
    int n = sizeof(wt) / sizeof(wt[0]); // Number of items

    // Resize the global table to (n+1) x (W+1)
    t.resize(n + 1, vector<int>(W + 1, -1));

    // Solve the problem and print the result
    cout << "Maximum value in the knapsack (Top-Down) = " << unboundedKnapsack(wt, val, W, n) << endl;

    return 0;
}

// Unbounded Knapsack: Bottom-Up Approach
int unboundedKnapsack(int wt[], int val[], int W, int n) {
    // Create a DP table to store results of subproblems
    int t[n + 1][W + 1];

    // Initialize the table for base cases:
    // When either the number of items (n) or capacity (W) is 0, the maximum value is 0
    for (int i = 0; i < n + 1; i++) 
        t[i][0] = 0; // Zero capacity => zero value
    for (int j = 0; j < W + 1; j++) 
        t[0][j] = 0; // No items => zero value

    // Fill the table iteratively
    for (int i = 1; i < n + 1; i++) {         // Loop through items
        for (int j = 1; j < W + 1; j++) {     // Loop through capacities
            if (wt[i - 1] <= j) {
                // Include the item (reuse it) or exclude it
                t[i][j] = max(
                    val[i - 1] + t[i][j - wt[i - 1]], // Include the item (reuse it)
                    t[i - 1][j]                       // Exclude the item
                );
            } else {
                // If the weight of the item exceeds the current capacity, exclude it
                t[i][j] = t[i - 1][j];
            }
        }
    }

    // Return the maximum value for the given weight capacity and all items
    return t[n][W];
}