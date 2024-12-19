#include <iostream>
#include <vector>

using namespace std;

long long merge(vector<int>& arr, int left, int mid, int right) {
    long long inv = 0;

    // Create temporary vectors for the two halves
    vector<int> leftVec(arr.begin() + left, arr.begin() + mid + 1); // Left half
    vector<int> rightVec(arr.begin() + mid + 1, arr.begin() + right + 1); // Right half

    int i = 0, j = 0, k = left;

    // Merge the two halves and count inversions
    while (i < leftVec.size() && j < rightVec.size()) {
        if (leftVec[i] <= rightVec[j]) {
            arr[k] = leftVec[i];
            i++;
        } else {
            arr[k] = rightVec[j];
            inv += leftVec.size() - i; // Count inversions
            j++;
        }
        k++;
    }

    // Copy the remaining elements of leftVec, if any
    while (i < leftVec.size()) {
        arr[k] = leftVec[i];
        k++;
        i++;
    }

    // Copy the remaining elements of rightVec, if any
    while (j < rightVec.size()) {
        arr[k] = rightVec[j];
        k++;
        j++;
    }

    return inv;
}

long long mergeSort(vector<int>& arr, int left, int right) {
    long long inv = 0;
    if (left < right) {
        int mid = left + (right - left) / 2; // Calculate mid to avoid overflow
        inv += mergeSort(arr, left, mid); // Sort left half
        inv += mergeSort(arr, mid + 1, right); // Sort right half
        inv += merge(arr, left, mid, right); // Merge sorted halves
    }
    return inv;
}

int main() {
    vector<int> arr = {3, 1, 2, 5, 4}; // Sample array
    int n = arr.size();

    long long inversions = mergeSort(arr, 0, n - 1);

    // Output the sorted array and the number of inversions
    cout << "Sorted array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << "\nNumber of inversions: " << inversions << endl;

    return 0;
}
