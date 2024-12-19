#include <iostream>
#include <algorithm>
using namespace std;

int trappingWater(int arr[], int n) {
    // Arrays to store the maximum height to the left and right of each index
    int maxLeft[n], maxRight[n];

    // Fill maxLeft array
    maxLeft[0] = arr[0];
    for (int i = 1; i < n; i++) {
        maxLeft[i] = max(maxLeft[i - 1], arr[i]);
    }

    // Fill maxRight array
    maxRight[n - 1] = arr[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        maxRight[i] = max(maxRight[i + 1], arr[i]);
    }

    // Calculate the total trapped water
    int totalWater = 0;
    for (int i = 0; i < n; i++) {
        // Water trapped at index i = min(maxLeft[i], maxRight[i]) - arr[i]
        totalWater += min(maxLeft[i], maxRight[i]) - arr[i];
    }

    return totalWater;
}
