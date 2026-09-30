// Global memoization array
#include <vector>
using namespace std;

vector<int> t; // Global variable for memoization

int recursiveMinJumps(int currentIndex, const vector<int>& arr, int n) {
    // Base case: If we reach the last element
    if (currentIndex >= n - 1) return 0; // No more jumps needed
    
    // If the current position is 0, we can't move
    if (arr[currentIndex] == 0) return INT_MAX; // Return a large number to indicate failure
    
    // If we already computed the result for this index, return it
    if (t[currentIndex] != -1) return t[currentIndex];
    
    int jumps = INT_MAX;
    int maxJump = arr[currentIndex]; // Maximum jump length from current position
    
    // Try all possible jumps from current index
    for (int i = 1; i <= maxJump && currentIndex + i < n; i++) {
        int nextJumps = recursiveMinJumps(currentIndex + i, arr, n);
        if (nextJumps != INT_MAX) {
            jumps = min(jumps, 1 + nextJumps); // Add one for the current jump
        }
    }
    
    // Store the result in the memoization array
    return t[currentIndex] = jumps;
}

int minJumps(vector<int>& arr) {
    int n = arr.size(); // Get the size of the array
    t.assign(n, -1); // Initialize memoization array with -1

    int result = recursiveMinJumps(0, arr, n);
    return (result == INT_MAX) ? -1 : result; // Return -1 if end is not reachable
}