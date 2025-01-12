#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to calculate the minimum sum of absolute differences
int minimumSumOfDifferences(vector<int>& a, vector<int>& b) {
    int n = a.size();

    // Step 1: Sort both arrays
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    // Step 2: Calculate the sum of absolute differences
    int minSum = 0;
    for (int i = 0; i < n; i++) {
        minSum += abs(a[i] - b[i]);
    }

    return minSum;
}

// Driver code
int main() {
    vector<int> a = {4, 1, 8, 7};
    vector<int> b = {2, 3, 6, 5};

    cout << "Minimum Sum of Absolute Differences: " << minimumSumOfDifferences(a, b) << endl;

    return 0;
}
