#include <iostream>
#include <vector>
using namespace std;

// Function to rearrange the array with order preserved
void rearrangeArray(vector<int>& arr) {
    int n = arr.size();
    int negativeIndex = 0; // Pointer for the position to place the next negative number

    // Loop through the array
    for (int i = 0; i < n; i++) {
        // If the current element is negative
        if (arr[i] < 0) {
            int temp = arr[i]; // Store the negative element
            // Shift all positive elements in the range [negativeIndex, i-1] one step to the right
            for (int j = i; j > negativeIndex; j--) {
                arr[j] = arr[j - 1];
            }
            // Place the negative element at the correct position
            arr[negativeIndex] = temp;
            negativeIndex++; // Update the negative pointer
        }
    }
}

int main() {
    vector<int> arr = {-12, 11, -13, -5, 6, -7, 5, -3, -6};
    rearrangeArray(arr);

    cout << "Rearranged array (order preserved): ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
