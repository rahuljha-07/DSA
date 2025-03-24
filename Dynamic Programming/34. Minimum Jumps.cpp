#include <iostream>
#include <vector>
#include <climits>
using namespace std;

// Helper function for recursion with memoization
int minJumpsHelper(vector<int> &arr, int index, int n, vector<int> &dp) {
    // Base case: If we are at or beyond the last index, no more jumps are needed
    if (index >= n - 1) return 0;

    // If the current position is 0, we can't move forward
    if (arr[index] == 0) return INT_MAX;

    // If already computed, return the stored value
    if (dp[index] != -1) return dp[index];

    // Initialize the minimum jumps to a large value
    int minJumps = INT_MAX;

    // Try all possible jumps from the current index
    for (int step = 1; step <= arr[index]; step++) {
        int nextJumps = minJumpsHelper(arr, index + step, n, dp);
        if (nextJumps != INT_MAX) { // Ensure the subproblem is solvable
            minJumps = min(minJumps, 1 + nextJumps);
        }
    }

    // Store the result in dp
    return dp[index] = minJumps;
}

int minJumps(vector<int> &arr) {
    int n = arr.size();
    vector<int> dp(n, -1); // Initialize memoization table with -1
    int result = minJumpsHelper(arr, 0, n, dp);

    // If the result is INT_MAX, it means the end is not reachable
    return (result == INT_MAX) ? -1 : result;
}

int main() {
    vector<int> arr1 = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9};
    cout << "Minimum jumps: " << minJumps(arr1) << endl;

    vector<int> arr2 = {1, 0, 3, 2};
    cout << "Minimum jumps: " << minJumps(arr2) << endl;

    vector<int> arr3 = {0};
    cout << "Minimum jumps: " << minJumps(arr3) << endl;

    return 0;
}
