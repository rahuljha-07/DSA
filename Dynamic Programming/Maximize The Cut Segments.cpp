#include <iostream>
#include <vector>
#include <algorithm> // For std::max
using namespace std;

// Helper function to calculate the maximum number of cuts with memoization
int maximizeCutsHelper(int n, int x, int y, int z, vector<int> &dp) {
    // Base case: If the length of the segment becomes zero, return 0
    if (n == 0) return 0;

    // If the length becomes negative, no cuts are possible
    if (n < 0) return -1;

    // If the value is already computed, return it
    if (dp[n] != -1) return dp[n];

    // Recursive calls for each cut length
    int cutX = maximizeCutsHelper(n - x, x, y, z, dp);
    int cutY = maximizeCutsHelper(n - y, x, y, z, dp);
    int cutZ = maximizeCutsHelper(n - z, x, y, z, dp);

    // Take the maximum of all valid cuts
    int maxCuts = max({cutX, cutY, cutZ});

    // If no cuts are possible, store -1; otherwise, add 1 for the current cut
    dp[n] = (maxCuts == -1) ? -1 : 1 + maxCuts;

    return dp[n];
}

// Function to calculate the maximum number of cuts
int maximizeCuts(int n, int x, int y, int z) {
    vector<int> dp(n + 1, -1); // Initialize the memoization table with -1
    int result = maximizeCutsHelper(n, x, y, z, dp);
    return (result == -1) ? 0 : result; // If result is -1, return 0
}

int main() {
    // Input values
    int n = 4, x = 2, y = 1, z = 1;

    // Get the maximum cuts
    int result = maximizeCuts(n, x, y, z);

    cout << "Maximum number of cuts: " << result << endl;

    return 0;
}
