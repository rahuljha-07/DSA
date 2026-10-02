#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to find the smallest subset with a sum greater than the rest
int smallestSubset(vector<int>& arr) {
    // Step 1: Sort the array in descending order
    sort(arr.begin(), arr.end(), greater<int>());

    // Step 2: Calculate the total sum of the array
    int totalSum = 0;
    for (int num : arr) {
        totalSum += num;
    }

    // Step 3: Find the smallest subset
    int subsetSum = 0;
    int count = 0;
    for (int num : arr) {
        subsetSum += num;
        count++;
        if (subsetSum > totalSum - subsetSum) {
            break;
        }
    }

    return count;
}

// Driver code
int main() {
    vector<int> arr1 = {3, 1, 7, 1};
    vector<int> arr2 = {2, 1, 2};

    cout << "Minimum elements in subset for arr1: " << smallestSubset(arr1) << endl;
    cout << "Minimum elements in subset for arr2: " << smallestSubset(arr2) << endl;

    return 0;
}
