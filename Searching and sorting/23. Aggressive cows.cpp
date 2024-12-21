#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Function to check if it's possible to place cows in the stalls such that the minimum distance is at least minDist
bool canPlaceCows(const vector<int>& stalls, int numCows, int minDist) {
    int countCows = 1; // Start by placing the first cow in the first stall
    int lastPlaced = stalls[0]; // Position of the last placed cow

    // Iterate through the stalls to try placing the remaining cows
    for (int i = 1; i < stalls.size(); i++) {
        // If the current stall is far enough from the last placed cow
        if (stalls[i] - lastPlaced >= minDist) {
            countCows++; // Place a cow in the current stall
            lastPlaced = stalls[i]; // Update the last placed position

            // If all cows have been placed successfully, return true
            if (countCows == numCows) {
                return true;
            }
        }
    }

    return false; // Not all cows could be placed with the required minimum distance
}

// Function to find the largest minimum distance between cows
int largestMinDistance(vector<int>& stalls, int numCows) {
    sort(stalls.begin(), stalls.end()); // Sort stall positions

    int low = 1; // Minimum possible distance
    int high = stalls.back() - stalls.front(); // Maximum possible distance
    int result = 0; // To store the largest minimum distance found

    // Perform binary search to find the largest minimum distance
    while (low <= high) {
        int mid = low + (high - low) / 2; // Calculate the mid distance

        // Check if cows can be placed with at least mid distance apart
        if (canPlaceCows(stalls, numCows, mid)) {
            result = mid; // Update result with current mid distance
            low = mid + 1; // Try for a larger distance
        } else {
            high = mid - 1; // Reduce the distance
        }
    }

    return result; // Return the largest minimum distance found
}

int main() {
    int t; // Number of test cases
    cin >> t; // Input number of test cases
    while (t--) {
        int N, C; // Number of stalls and cows
        cin >> N >> C; // Input N and C
        vector<int> stalls(N); // Vector to store stall positions

        // Input stall positions
        for (int i = 0; i < N; i++) {
            cin >> stalls[i]; // Read stall position
        }

        // Output the result for the current test case
        cout << largestMinDistance(stalls, C) << endl; // Find and print the largest minimum distance
    }

    return 0; // Exit the program
}
