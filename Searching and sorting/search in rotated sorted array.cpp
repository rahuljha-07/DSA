#include <iostream>
#include <vector>
using namespace std;

// Function to find the pivot (smallest element) in the rotated sorted array
int findPivotInRotatedArray(const vector<int>& arr) {
    int n = arr.size();
    int start = 0, end = n - 1;

    while (start <= end) {
        int mid = start + (end - start) / 2;
        int next = (mid + 1) % n;
        int prev = (mid + n - 1) % n;

        if (arr[mid] <= arr[next] && arr[mid] <= arr[prev]) {
            return mid;
        }

        if (arr[start] <= arr[mid]) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    return -1;
}

// Standard binary search function
int binarySearch(const vector<int>& arr, int start, int end, int target) {
    while (start <= end) {
        int mid = start + (end - start) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    return -1;
}

// Function to search an element in a rotated sorted array
int searchInRotatedArray(const vector<int>& arr, int target) {
    int n = arr.size();
    
    // Find the pivot in the rotated sorted array
    int pivot = findPivotInRotatedArray(arr);

    // If pivot is -1, it means the array is not rotated, so we can perform a binary search on the entire array
    if (pivot == -1) {
        return binarySearch(arr, 0, n - 1, target);
    }

    // If the target is equal to the pivot element, return pivot
    if (arr[pivot] == target) {
        return pivot;
    }

    // Determine which side to search based on the pivot and target
    if (target >= arr[0] && target <= arr[pivot - 1]) {
        // Target is in the left half
        return binarySearch(arr, 0, pivot - 1, target);
    } else {
        // Target is in the right half
        return binarySearch(arr, pivot, n - 1, target);
    }
}

int main() {
    vector<int> arr = {15, 18, 2, 3, 6, 12};
    int target = 3;

    int index = searchInRotatedArray(arr, target);
    if (index != -1) {
        cout << "Element found at index: " << index << endl;
    } else {
        cout << "Element not found in the array." << endl;
    }

    return 0;
}
