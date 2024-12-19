#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int maxSubarraySum(vector<int>& arr) {
    int maxi = INT_MIN;      // Store the maximum sum
    int sum = 0;             // Current subarray sum
    int ansStart = -1;       // Start index of the max subarray
    int ansEnd = -1;         // End index of the max subarray
    int start = 0;           // Temporary start index for the current subarray

    for (int i = 0; i < arr.size(); i++) {
        // Initialize the start of a potential new subarray
        if (sum == 0) start = i;

        // Add the current element to the sum
        sum += arr[i];

        // Update the maximum sum and indices if the current sum exceeds the maximum
        if (sum > maxi) {
            maxi = sum;
            ansStart = start;
            ansEnd = i;
        }

        // If the sum becomes negative, reset the sum to 0
        if (sum < 0) sum = 0;
    }

    // Optionally, print the indices of the maximum sum subarray
    cout << "Maximum subarray sum is from index " << ansStart << " to " << ansEnd << endl;

    return maxi;
}

int main() {
    vector<int> arr = {-2, 1, -3, 4, -1, 2, 1, -5, 4}; // Example input
    cout << "Maximum subarray sum: " << maxSubarraySum(arr) << endl;
    return 0;
}
