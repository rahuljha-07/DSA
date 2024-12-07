#include <iostream>
#include <vector>
#include <algorithm> // for std::max
using namespace std;

// Function to get the maximum amount of gold
int getMaxGold(vector<vector<int>> &mine) {
    int n = mine.size();    // Number of rows
    int m = mine[0].size(); // Number of columns

    // Create a table to store the maximum gold collected up to each cell
    vector<vector<int>> dp(n, vector<int>(m, 0));

    // Copy the last column as the base case
    for (int i = 0; i < n; i++) {
        dp[i][m - 1] = mine[i][m - 1];
    }

    // Fill the DP table column by column from right to left
    for (int col = m - 2; col >= 0; col--) {
        for (int row = 0; row < n; row++) {
            // Check the three possible directions from the current cell
            int right = dp[row][col + 1]; // Right
            int right_up = (row - 1 >= 0) ? dp[row - 1][col + 1] : 0; // Diagonally up-right
            int right_down = (row + 1 < n) ? dp[row + 1][col + 1] : 0; // Diagonally down-right

            // Update the DP table with the maximum gold collected
            dp[row][col] = mine[row][col] + max({right, right_up, right_down});
        }
    }

    // Find the maximum gold in the first column
    int maxGold = 0;
    for (int i = 0; i < n; i++) {
        maxGold = max(maxGold, dp[i][0]);
    }

    return maxGold;
}

int main() {
    // Example 1
    vector<vector<int>> mine1 = {{1, 3, 3},
                                 {2, 1, 4},
                                 {0, 6, 4}};
    cout << "Maximum gold collected (Example 1): " << getMaxGold(mine1) << endl;

    // Example 2
    vector<vector<int>> mine2 = {{1, 3, 1, 5},
                                 {2, 2, 4, 1},
                                 {5, 0, 2, 3},
                                 {0, 6, 1, 2}};
    cout << "Maximum gold collected (Example 2): " << getMaxGold(mine2) << endl;

    return 0;
}
