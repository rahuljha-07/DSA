#include <iostream>
#include <vector>
using namespace std;

// Global memoization table
vector<vector<int>> t;

// bottom up
int knapsack(int wt[], int val[], int W, int n) {
    // Base case: if no items are left or capacity is 0
    if (n == 0 || W == 0)
        return 0;

    // Check if the result is already computed (memoization)
    if (t[n][W] != -1)
        return t[n][W];

    // If the weight of the nth item is less than or equal to the remaining capacity
    if (wt[n - 1] <= W) {
        // Include the nth item in the knapsack or exclude it, take the maximum value
        t[n][W] = max(
            val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1), // Include the item
            knapsack(wt, val, W, n - 1)                          // Exclude the item
        );
    } else {
        // If the weight of the nth item exceeds the remaining capacity, exclude it
        t[n][W] = knapsack(wt, val, W, n - 1);
    }

    return t[n][W];
}


int main() {
    // Sample inputs
    int wt[] = {1, 3, 4, 5};  // Weights of the items
    int val[] = {1, 4, 5, 7}; // Values of the items
    int W = 7;                // Maximum capacity of the knapsack
    int n = sizeof(wt) / sizeof(wt[0]); // Number of items

    // Resize the global table to (n+1) x (W+1)
    t.resize(n + 1, vector<int>(W + 1, -1));

    // Solve the problem and print the result
    cout << "Maximum value in the knapsack = " << knapsack(wt, val, W, n) << endl;

    return 0;
}

// top down
int knapSack(int w, int wt[], int val[], int n) {
    // Create a DP table to store results of subproblems
    int t[n + 1][w + 1];

    // Initialize the table for base cases:
    // When either the number of items (n) or capacity (w) is 0, the maximum value is 0
    for (int i = 0; i < n + 1; i++) 
        t[i][0] = 0; // Zero capacity => zero value
    for (int j = 0; j < w + 1; j++) 
        t[0][j] = 0; // No items => zero value

    // Fill the table iteratively
    for (int i = 1; i < n + 1; i++) {         // Loop through items
        for (int j = 1; j < w + 1; j++) {     // Loop through capacities
            if (wt[i - 1] <= j) {
                // If the weight of the current item is less than or equal to capacity
                // Take the maximum of including or excluding the current item
                t[i][j] = max(
                    val[i - 1] + t[i - 1][j - wt[i - 1]], // Include the item
                    t[i - 1][j]                          // Exclude the item
                );
            } else {
                // If the weight of the current item exceeds the current capacity, exclude it
                t[i][j] = t[i - 1][j];
            }
        }
    }

    // Return the maximum value for the given weight capacity and all items
    return t[n][w];
}
