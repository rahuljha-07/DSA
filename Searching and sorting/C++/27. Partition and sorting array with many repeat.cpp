#include <iostream>
#include <vector>
using namespace std;

// code uses logic of dutch national flag
void threeWayPartition(vector<int>& arr, int pivot) {
    int low = 0; // Pointer for the next position of elements less than pivot
    int mid = 0; // Pointer for the current element being checked
    int high = arr.size() - 1; // Pointer for the next position of elements greater than pivot

    // Iterate until mid pointer crosses high pointer
    while (mid <= high) {
        if (arr[mid] < pivot) {
            // Swap arr[low] and arr[mid], increment both low and mid
            swap(arr[low], arr[mid]);
            low++;
            mid++;
        } else if (arr[mid] > pivot) {
            // Swap arr[mid] and arr[high], decrement high
            swap(arr[mid], arr[high]);
            high--;
        } else { // arr[mid] == pivot
            // Just increment mid
            mid++;
        }
    }
}

int main() {
    vector<int> arr = {3, 5, 2, 3, 7, 3, 1, 4};
    int pivot = 3;

    threeWayPartition(arr, pivot);

    // Output the sorted and partitioned array
    for (int i : arr) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
