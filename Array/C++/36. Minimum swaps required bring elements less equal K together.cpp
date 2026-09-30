#include <iostream>
#include <algorithm>
using namespace std;

int minSwap(int arr[], int n, int k) {
    // Step 1: Count elements less than or equal to k
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] <= k) count++;
    }

    // Step 2: Find the number of "bad" elements in the first window of size `count`
    int bad = 0;
    for (int i = 0; i < count; i++) {
        if (arr[i] > k) bad++;
    }

    // Step 3: Use sliding window to find the minimum number of "bad" elements
    int ans = bad;
    for (int i = 0, j = count; j < n; i++, j++) {
        // Remove the effect of the element leaving the window
        if (arr[i] > k) bad--;

        // Add the effect of the new element entering the window
        if (arr[j] > k) bad++;

        // Update the answer with the minimum "bad" count
        ans = min(ans, bad);
    }

    return ans;
}

int main() {
    int arr[] = {2, 1, 5, 6, 3}; // Example input
    int n = sizeof(arr) / sizeof(arr[0]);
    int k = 3;

    cout << "Minimum swaps required: " << minSwap(arr, n, k) << endl;
    return 0;
}
