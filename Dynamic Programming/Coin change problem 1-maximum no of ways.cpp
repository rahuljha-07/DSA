/*
exact same like count subset sum with given sum
coins are unlimited which shows unbounded knapsack
unbounded hai toh i rhega i-1 nhi
*/
// code given below for reference
#include <iostream>
using namespace std;

// Function to calculate the maximum number of ways to make the target sum
int coinChange(int coins[], int n, int sum) {
    // Create a DP table `t` with dimensions (n+1) x (sum+1)
    int t[n + 1][sum + 1];

    // Initialize the DP table
    // If sum is 0, there's one way to achieve it: use no coins
    for (int i = 0; i < n + 1; i++)
        t[i][0] = 1;

    // If no coins are available and sum > 0, there's no way to achieve it
    for (int j = 1; j < sum + 1; j++)
        t[0][j] = 0;

    // Fill the DP table iteratively
    for (int i = 1; i < n + 1; i++) {
        for (int j = 1; j < sum + 1; j++) {
            if (coins[i - 1] <= j) {
                // Include the coin (reuse it) or exclude it
                t[i][j] = t[i][j - coins[i - 1]] + t[i - 1][j];
            } else {
                // Exclude the coin
                t[i][j] = t[i - 1][j];
            }
        }
    }

    // The answer is in the bottom-right corner of the table
    return t[n][sum];
}

int main() {
    int coins[] = {1, 2, 3};
    int n = sizeof(coins) / sizeof(coins[0]);
    int sum = 4;

    cout << "Maximum number of ways to make the sum = " << coinChange(coins, n, sum) << endl;

    return 0;
}
