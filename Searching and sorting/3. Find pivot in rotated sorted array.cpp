#include <iostream>
#include <vector>
using namespace std;

int findPivotInRotatedArray(const vector<int>& arr) {
    int n = arr.size();
    int start = 0, end = n - 1;

    // Loop until the start pointer crosses the end pointer
    while (start <= end) {
        // Calculate mid-point of the current segment
        int mid = start + (end - start) / 2;
        
        // Calculate the indices for the next and previous elements in a circular manner
        int next = (mid == n - 1) ? 0 : mid + 1;
        int prev = (mid == 0) ? n - 1 : mid - 1;
        
        // Check if the mid element is less than or equal to both its next and previous elements
        // If true, mid is the pivot (minimum element) in the rotated array
        if (arr[mid] <= arr[next] && arr[mid] <= arr[prev]) {
            return mid;  // Pivot found at index 'mid'
        }

        // If the left part of the array is sorted, move to the right part
        if (arr[start] <= arr[mid]) {
            start = mid + 1;
        } else {
            // If the right part of the array is sorted, move to the left part
            end = mid - 1;
        }
    }

    return -1; // Pivot not found, though it should exist in a rotated sorted array
}

int main() {
    vector<int> arr = {15, 18, 2, 3, 6, 12};
    int pivotIndex = findPivotInRotatedArray(arr);
    
    if (pivotIndex != -1) {
        cout << "Pivot found at index: " << pivotIndex << ", value: " << arr[pivotIndex] << endl;
    } else {
        cout << "Pivot not found." << endl;
    }

    return 0;
}
