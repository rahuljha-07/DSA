#include <iostream>
#include <vector>
using namespace std;

void dutchNationalFlag(vector<int>& arr) {
    int low = 0;      // Pointer for the next position of the first value
    int mid = 0;      // Pointer for the current element being checked
    int high = arr.size() - 1; // Pointer for the next position of the third value

    // Iterate until mid pointer crosses high pointer
    while (mid <= high) {
        if (arr[mid] == 0) {
            // Swap arr[low] and arr[mid], increment both low and mid
            swap(arr[low], arr[mid]);
            low++;
            mid++;
        } else if (arr[mid] == 1) {
            // Just increment mid
            mid++;
        } else { // arr[mid] == 2
            // Swap arr[mid] and arr[high], decrement high
            swap(arr[mid], arr[high]);
            high--;
        }
    }
}

int main() {
    vector<int> arr = {2, 0, 2, 1, 1, 0};

    dutchNationalFlag(arr);

    // Output the sorted array
    for (int i : arr) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
