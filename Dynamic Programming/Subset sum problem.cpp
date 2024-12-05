#include <iostream>
#include <vector>
using namespace std;

// Global memoization table
vector<vector<int>> t;

// Function to determine if a subset with sum `sum` exists
bool subsetSum(int arr[], int n, int sum) {
    // Base cases
    if (sum == 0) return true;  // Subset with sum 0 always exists (empty subset)
    if (n == 0) return false;  // No elements left, no subset can sum to > 0

    // If already computed, return the stored result
    if (t[n][sum] != -1)
        return t[n][sum];

    // If the current element is smaller than the remaining sum, include or exclude the current element
    if (arr[n - 1] < sum) return t[n][sum] = subsetSum(arr, n - 1, sum - arr[n - 1]) || subsetSum(arr, n - 1, sum);

    // Otherwise, exclude it
     return t[n][sum] = subsetSum(arr, n - 1, sum);
}

int main() {
    int arr[] = {3, 34, 4, 12, 5, 2};
    int n = sizeof(arr) / sizeof(arr[0]);
    int sum = 9;

    // Initialize the memoization table with -1
    t.resize(n + 1, vector<int>(sum + 1, -1));

    if (subsetSum(arr, n, sum))
        cout << "Subset with sum " << sum << " exists." << endl;
    else
        cout << "Subset with sum " << sum << " does not exist." << endl;

    return 0;
}

// bottom up
bool subsetSum(int arr[], int n, int sum) {
    // Create a DP table `t` with dimensions (n+1) x (sum+1)
    bool t[n + 1][sum + 1];

    // Base case: Initialize table
    for (int i = 0; i < sum + 1; i++) 
        t[0][i] = false; // No items => no subset for sum > 0
    for (int i = 0; i < n + 1; i++) 
        t[i][0] = true;  // Subset with sum 0 always exists (empty subset)

    // Fill the table iteratively
    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < sum + 1; j++) {
            if (arr[i - 1] <= j) {
                // Include or exclude the current element
                t[i][j] = t[i - 1][j - arr[i - 1]] || t[i - 1][j];
            } else {
                // Exclude the current element
                t[i][j] = t[i - 1][j];
            }
        }
    }

    // The answer is in the bottom-right corner of the table
    return t[n][sum];
}
