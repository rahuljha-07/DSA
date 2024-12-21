#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

// Function to find and print all subarrays with sum zero
void printAllSubarraysWithZeroSum(int arr[], int n) {
    // Map to store the cumulative sum and the indices where it appears
    unordered_map<int, vector<int>> sumMap;

    // Initialize the cumulative sum and add a base case for sum = 0
    int sum = 0;
    sumMap[0].push_back(-1);  // For subarrays starting from index 0

    // Iterate over the array
    for (int i = 0; i < n; ++i) {
        // Add the current element to the cumulative sum
        sum += arr[i];

        // Check if this sum has been seen before
        if (sumMap.find(sum) != sumMap.end()) {
            // If found, it means there's a subarray with a sum of zero
            for (int startIdx : sumMap[sum]) {
                cout << "Subarray with zero sum found from index "
                     << (startIdx + 1) << " to " << i << endl;
            }
        }

        // Store the current index in the sum map
        sumMap[sum].push_back(i);
    }
}

int main() {
    int arr[] = {3, 4, -7, 1, 3, 3, 1, -4};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "All subarrays with zero sum are:" << endl;
    printAllSubarraysWithZeroSum(arr, n);

    return 0;
}
