#include <iostream>
#include <vector>
using namespace std;

// Helper function with recursion + memoization
int countWaysHelper(int n, vector<int> &dp) {
    // Base cases
    if (n == 0) return 1; // One way to achieve 0 score (do nothing)
    if (n < 0) return 0;   // No way to achieve a negative score

    // If already computed, return the stored value
    if (dp[n] != -1) return dp[n];

    // Recursive calls for the three possible moves (3, 5, 10 points)
    return dp[n] = countWaysHelper(n - 3, dp) 
                 + countWaysHelper(n - 5, dp) 
                 + countWaysHelper(n - 10, dp);
}

// Function to initialize the dp array and call the helper function
int count(int n) {
    // Create a memoization table initialized to -1
    vector<int> dp(n + 1, -1);

    // Call the recursive helper function
    return countWaysHelper(n, dp);
}

int main() {
    int n1 = 10;
    cout << "Number of ways to reach score " << n1 << ": " << count(n1) << endl;

    int n2 = 20;
    cout << "Number of ways to reach score " << n2 << ": " << count(n2) << endl;

    return 0;
}
