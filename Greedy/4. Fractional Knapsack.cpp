#include <bits/stdc++.h>
using namespace std;

const int D = 1000; // DP matrix dimension
double t[D][D];     // DP matrix for fractional knapsack

// Function to solve the fractional knapsack problem
double Knapsack(int wt[], int val[], int W, int n) {
    // Base case: No items left or knapsack capacity is zero
    if (n == 0 || W == 0)
        return 0.0;

    // If already calculated, return the cached value
    if (t[n][W] != -1)
        return t[n][W];

    // Else calculate
    else {
        // If the current item can fully fit in the knapsack
        if (wt[n - 1] <= W) {
            // Option 1: Include the entire item
            double includeFull = val[n - 1] + Knapsack(wt, val, W - wt[n - 1], n - 1);

            // Option 2: Exclude the current item
            double excludeItem = Knapsack(wt, val, W, n - 1);

            // Store the maximum of including the item or excluding it
            t[n][W] = max(includeFull, excludeItem);
        } else {
            // Option 3: Include a fractional part of the item
            double includeFraction = (double)val[n - 1] * ((double)W / wt[n - 1]);
            // Option 2: Exclude the current item
            double exclude = Knapsack(wt, val, W, n - 1);

            // Store the maximum value when taking the fraction
            t[n][W] = max(includeFraction, exclude);
        }

        return t[n][W];
    }
}

// Example usage
int main() {
    memset(t, -1, sizeof(t)); // Initialize DP table with -1

    int wt[] = {10, 20, 30};   // Weights of items
    int val[] = {60, 100, 120}; // Values of items
    int W = 50;                // Capacity of the knapsack
    int n = sizeof(wt) / sizeof(wt[0]);

    double maxValue = Knapsack(wt, val, W, n);
    cout << "Maximum value in Knapsack = " << maxValue << endl;

    return 0;
}
