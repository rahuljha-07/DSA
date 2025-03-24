#include <iostream>
#include <vector>
using namespace std;

/*
Explanation of the Code:
Base Cases:

D(0) = 1: There’s one way to derange 0 items (do nothing).
D(1) = 0: No way to derange 1 item (it would always remain in its position).
Recursive Relation:

The number of derangements for n items is given by: D(n)=(n−1)×(D(n−1)+D(n−2))
This accounts for the two scenarios:
Swap the first element with another and recurse on the remaining  n−1 elements.
Fix the first element in its swapped position and derange the remaining  n−2 elements.
Memoization:

A vector memo is used to store precomputed results of D(n) to avoid redundant calculations.
If memo[n] != -1, the result is already computed, and we return it directly.
Wrapper Function:

The countDerangements function initializes the memoization table and calls the recursive helper.
Complexity:
Time Complexity: 𝑂(𝑛)
Each D(n) is computed at most once due to memoization.
Space Complexity: O(n)
For the memoization table and recursion stack.
*/

// Recursive function to calculate derangements
int countDerangementsHelper(int n, vector<int>& memo) {
    // Base cases
    if (n == 0) return 1; // One way to arrange 0 items (do nothing)
    if (n == 1) return 0; // No way to derange 1 item

    // If the value is already calculated, return it
    if (memo[n] != -1) return memo[n];

    // Recursive formula: D(n) = (n-1) * (D(n-1) + D(n-2))
    return memo[n] = (n - 1) * (countDerangementsHelper(n - 1, memo) + countDerangementsHelper(n - 2, memo));
}

// Wrapper function for memoization
int countDerangements(int n) {
    // Memoization table initialized with -1
    vector<int> memo(n + 1, -1);
    return countDerangementsHelper(n, memo);
}

// Main function to test the solution
int main() {
    int n = 3; // Example input
    cout << "Number of derangements for " << n << ": " << countDerangements(n) << endl;
    return 0;
}
