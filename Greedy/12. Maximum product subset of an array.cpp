#include <iostream>
#include <vector>
using namespace std;

// Function to find the maximum product subset of an array
long long maxProductSubset(vector<int>& arr) {
    long long positiveProduct = 1; // Product of all positive numbers
    long long negativeProduct = 1; // Product of all negative numbers
    int negativeCount = 0;         // Count of negative numbers
    int zeroCount = 0;             // Count of zeros
    int maxNegative = INT_MIN;     // Largest negative number

    // Traverse the array
    for (int num : arr) {
        if (num == 0) {
            zeroCount++; // Ignore zeros
            continue;
        }
        if (num > 0) {
            positiveProduct *= num; // Multiply positives
        } else {
            negativeCount++;
            maxNegative = max(maxNegative, num); // Track the largest negative
            negativeProduct *= num;             // Multiply negatives
        }
    }

    // If the array only contains zeros, return 0
    if (zeroCount == arr.size()) {
        return 0;
    }

    // If there are no positive numbers and only one negative number, return the single negative
    if (negativeCount == 1 && positiveProduct == 1 && zeroCount > 0) {
        return 0;
    }

    // If there are an odd number of negatives, exclude the largest (closest to 0) negative
    if (negativeCount % 2 != 0) {
        negativeProduct /= maxNegative; // Exclude the largest negative
    }

    // Combine positive and adjusted negative product
    return positiveProduct * (negativeCount > 0 ? negativeProduct : 1);
}

// Driver code
int main() {
    vector<int> arr = {-1, 0, -2, 4, 3};
    cout << "Maximum Product Subset: " << maxProductSubset(arr) << endl;
    return 0;
}
