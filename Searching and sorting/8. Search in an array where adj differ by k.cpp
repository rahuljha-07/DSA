#include <vector>
#include <iostream>
using namespace std;

int searchInStepArray(const vector<int>& arr, int k, int x) {
    int n = arr.size();
    int i = 0;

    // Iterate through the array
    while (i < n) {
        // Check if the current element is equal to the key
        if (arr[i] == x) {
            return i; // Return the index if found
        }

        // Calculate the difference between the current element and the key
        int diff = abs(arr[i] - x);
        
        // Move to the next index based on the step property
        // We can skip ahead by the difference divided by k
        // and move to the right index without skipping possible matches
        i += max(1, diff / k); // Ensure we move at least on e step forward
    }

    // If the key is not found, return -1
    return -1;
}

int main() {
    // Test cases
    vector<int> arr1 = {4, 5, 6, 7, 6};
    int k1 = 1;
    int x1 = 6;
    cout << "Index of " << x1 << " in arr1: " << searchInStepArray(arr1, k1, x1) << endl;

    vector<int> arr2 = {20, 40, 50, 70, 70, 60};
    int k2 = 20;
    int x2 = 60;
    cout << "Index of " << x2 << " in arr2: " << searchInStepArray(arr2, k2, x2) << endl;

    return 0;
}
