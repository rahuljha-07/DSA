#include <iostream>
#include <vector>
using namespace std;

int countWaysHelper(int n, vector<int> &dp) {
    // Base cases
    if (n == 0) return 1; // One way to achieve 0 score
    if (n < 0) return 0;  // No way to achieve negative score

    // If already computed, return the stored value
    if (dp[n] != -1) return dp[n];

    // Recursive calls for the three moves
    return dp[n] = countWaysHelper(n - 3, dp) + countWaysHelper(n - 5, dp) + countWaysHelper(n - 10, dp);
}

int count(int n) {
    // Create a memoization table initialized to -1
    vector<int> dp(n + 1, -1);

    // Call the helper function
    return countWaysHelper(n, dp);
}

int main() {
    int n1 = 10;
    cout << "Number of ways to reach score " << n1 << ": " << count(n1) << endl;

    int n2 = 20;
    cout << "Number of ways to reach score " << n2 << ": " << count(n2) << endl;

    return 0;
}
