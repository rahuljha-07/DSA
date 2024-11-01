#include <iostream>
#include <vector>

using namespace std;

// Function to merge two sorted halves of the array in place
void mergeInPlace(vector<int>& arr, int left, int mid, int right) {
    int start1 = left;
    int start2 = mid + 1;

    // Iterate through both halves
    while (start1 <= mid && start2 <= right) {
        // If the current element in the first half is in the correct position
        if (arr[start1] <= arr[start2]) {
            start1++;
        } else {
            // Element in the second half is smaller, shift the first half
            int value = arr[start2];
            int index = start2;

            // Shift all elements in the first half to the right
            while (index != start1) {
                arr[index] = arr[index - 1];
                index--;
            }
            arr[start1] = value;

            // Update all pointers
            start1++;
            mid++;
            start2++;
        }
    }
}

// In-place merge sort function
void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        // Recursively sort the first half
        mergeSort(arr, left, mid);
        // Recursively sort the second half
        mergeSort(arr, mid + 1, right);
        // Merge the two halves in place
        mergeInPlace(arr, left, mid, right);
    }
}

int main() {
    vector<int> arr = {56, 2, 45};

    cout << "Original array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    mergeSort(arr, 0, arr.size() - 1);

    cout << "Sorted array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
