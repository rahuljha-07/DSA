#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to maximize the sum of the array after K negations
long long maximizeSum(vector<int>& arr, int n, int k) {
    // Step 1: Sort the array to prioritize negations on smallest (negative) elements
    sort(arr.begin(), arr.end());

    // Step 2: Negate the smallest elements (negative ones) k times
    for (int i = 0; i < n && k > 0; i++) {
        if (arr[i] < 0) {
            arr[i] = -arr[i];
            k--;
        }
    }

    // Step 3: If k is still greater than 0, and it's odd, negate the smallest element
    if (k % 2 != 0) {
        sort(arr.begin(), arr.end()); // Re-sort to ensure the smallest element is at the beginning
        arr[0] = -arr[0];
    }

    // Step 4: Calculate and return the sum of the array
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }

    return sum;
}

// Driver code
int main() {
    int n = 5, k = 1;
    vector<int> arr = {1, 2, -3, 4, 5};

    cout << "Maximum sum after " << k << " negations: " << maximizeSum(arr, n, k) << endl;

    return 0;
}
