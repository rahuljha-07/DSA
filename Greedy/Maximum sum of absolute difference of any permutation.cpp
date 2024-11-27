#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to calculate the maximum sum of absolute differences
int maxAbsoluteDifferenceSum(vector<int>& arr) {
    // Step 1: Sort the array
    sort(arr.begin(), arr.end());

    // Step 2: Create the new sequence by alternating smallest and largest elements
    vector<int> result;
    int n = arr.size();
    int left = 0, right = n - 1;

    while (left <= right) {
        if (left == right) {
            result.push_back(arr[left]); // Add the last remaining element if odd-sized
        } else {
            result.push_back(arr[left]); // Add smallest element
            result.push_back(arr[right]); // Add largest element
        }
        left++;
        right--;
    }

    // Step 3: Calculate the sum of absolute differences
    int maxSum = 0;
    for (int i = 0; i < n - 1; i++) {
        maxSum += abs(result[i] - result[i + 1]);
    }
    maxSum += abs(result[n - 1] - result[0]); // Include the circular difference

    return maxSum;
}

// Driver code
int main() {
    vector<int> arr = {1, 2, 4, 8};

    // Function call
    cout << "Maximum Sum of Absolute Differences: " << maxAbsoluteDifferenceSum(arr) << endl;

    return 0;
}
