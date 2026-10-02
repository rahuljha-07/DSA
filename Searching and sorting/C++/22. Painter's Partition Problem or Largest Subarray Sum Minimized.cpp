#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

// Function to check if it is possible to paint all boards with the given maximum time
bool canPaint(const vector<int>& boards, int k, long long maxTime) {
    int painterCount = 1;         // Start with one painter
    long long currentTime = 0;    // Time used by current painter

    // Iterate through each board
    for (int i = 0; i < boards.size(); i++) {
        currentTime += boards[i]; // Add current board's length to current painter's time

        // If total time exceeds allowed maxTime
        if (currentTime > maxTime) {
            painterCount++;              // Allocate to a new painter
            currentTime = boards[i];     // Start with current board for new painter

            // If painters used exceed allowed limit, return false
            if (painterCount > k) {
                return false;
            }
        }
    }

    // All boards can be painted within maxTime using k painters
    return true;
}


// Function to find the minimum time required to paint all boards with k painters
long long findMinimumTime(vector<int>& boards, int k) {
    long long low = *max_element(boards.begin(), boards.end()); // At least one painter must paint the largest board
    long long high = accumulate(boards.begin(), boards.end(), 0LL); // All boards painted by one painter
    long long result = high; // Initialize result to the maximum possible time

    // Perform binary search to find the minimum time
    while (low <= high) {
        long long mid = low + (high - low) / 2; // Calculate mid point

        // Check if it's possible to paint all boards within mid time
        if (canPaint(boards, k, mid)) {
            result = mid; // Update result with the current mid time
            high = mid - 1; // Try for a smaller time
        } else {
            low = mid + 1; // Increase time limit to try again
        }
    }
    return result; // Return the minimum time
}

int main() {
    // Example usage
    int n, k;
    cout << "Enter number of boards and number of painters: ";
    cin >> n >> k;
    vector<int> boards(n);
    cout << "Enter lengths of the boards: ";
    for (int i = 0; i < n; i++) {
        cin >> boards[i];
    }

    long long minimumTime = findMinimumTime(boards, k);
    cout << "Minimum time to paint all boards: " << minimumTime << endl;

    return 0;
}
