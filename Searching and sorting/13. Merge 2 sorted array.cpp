#include <iostream>
#include <vector>

using namespace std;

vector<int> mergeSortedArrays(const vector<int>& arr1, const vector<int>& arr2) {
    vector<int> mergedArray;  // To store the merged result
    int i = 0;                // Pointer for arr1
    int j = 0;                // Pointer for arr2

    // Loop until we reach the end of either array
    while (i < arr1.size() && j < arr2.size()) {
        // Compare elements at both pointers
        if (arr1[i] <= arr2[j]) {
            mergedArray.push_back(arr1[i]); // Add smaller element to mergedArray
            i++;  // Move the pointer in arr1
        } else {
            mergedArray.push_back(arr2[j]); // Add smaller element to mergedArray
            j++;  // Move the pointer in arr2
        }
    }

    // If any elements are left in arr1, add them to mergedArray
    while (i < arr1.size()) {
        mergedArray.push_back(arr1[i]);
        i++;
    }

    // If any elements are left in arr2, add them to mergedArray
    while (j < arr2.size()) {
        mergedArray.push_back(arr2[j]);
        j++;
    }

    return mergedArray; // Return the merged sorted array
}

// Example usage
int main() {
    vector<int> arr1 = {1, 3, 4, 5};
    vector<int> arr2 = {2, 4, 6, 8};

    vector<int> merged = mergeSortedArrays(arr1, arr2);

    cout << "Merged Array: ";
    for (int num : merged) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
