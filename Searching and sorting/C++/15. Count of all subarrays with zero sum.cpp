#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int countZeroSumSubarrays(int arr[], int n) {
    unordered_map<int, vector<int>> sumMap; // Map to store cumulative sums and their indices
    int sum = 0;                            // Cumulative sum
    int count = 0;                          // Count of zero-sum subarrays

    // Initialize map with sum 0 at index -1 (to handle subarrays starting at index 0)
    sumMap[0].push_back(-1);

    // Traverse the array
    for (int i = 0; i < n; i++) {
        // Add current element to cumulative sum
        sum += arr[i];

        // Check if this cumulative sum has been seen before
        if (sumMap.find(sum) != sumMap.end()) {
            // If found, the number of zero-sum subarrays ending at i is the number of times this sum has appeared before
            count += sumMap[sum].size();
        }

        // Add the current index to the list of indices for this cumulative sum
        sumMap[sum].push_back(i);
    }

    return count;
}

int main() {
    int arr[] = {0, 0, 5, 5, 0, 0};
    int n = sizeof(arr) / sizeof(arr[0]);

    int result = countZeroSumSubarrays(arr, n);
    cout << "Total zero-sum subarrays: " << result << endl;

    return 0;
}
