#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int MOD = 1e9 + 7;

// Function to calculate the maximum value of ∑arr[i]*i
long long maximizeValuePermutation(vector<int>& arr) {
    // Step 1: Sort the array in ascending order
    sort(arr.begin(), arr.end());

    // Step 2: Calculate the sum of arr[i] * i
    long long result = 0;
    for (int i = 0; i < arr.size(); i++) {
        result = (result + (long long)arr[i] * i) % MOD; // Add product modulo MOD
    }

    return result;
}

int main() {
    vector<int> arr = {5, 3, 2, 4, 1};

    // Function call
    cout << "Maximum Value: " << maximizeValuePermutation(arr) << endl;

    return 0;
}
