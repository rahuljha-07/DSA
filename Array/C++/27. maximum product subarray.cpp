#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int subarrayWithMaxProduct(vector<int>& arr) {
    int pre = 1, suff = 1; // Variables to track forward and backward products
    int ans = INT_MIN;    // To store the maximum product
    int n = arr.size();   // Size of the array

    // Traverse the array from both ends
    for (int i = 0; i < n; i++) {
        // Reset `pre` and `suff` if they encounter 0
        if (pre == 0) pre = 1;
        if (suff == 0) suff = 1;

        // Update the forward product
        pre *= arr[i];
        // Update the backward product
        suff *= arr[n - i - 1];

        // Update the maximum product
        ans = max(ans, max(pre, suff));
    }

    return ans;
}

int main() {
    vector<int> arr = {2, 3, -2, 4}; // Example input
    cout << "Maximum product of subarray: " << subarrayWithMaxProduct(arr) << endl;
    return 0;
}
 