#include <iostream>
#include <vector>
using namespace std;

void rearrangeArray(vector<int>& arr) {
    int n = arr.size();
    int negativeIndex = 0; // Pointer for the position to place the next negative number

    // Loop through the array
    for (int i = 0; i < n; i++) {
        // If the current element is negative
        if (arr[i] < 0) {
            // Swap the current element with the element at negativeIndex
            swap(arr[i], arr[negativeIndex]);
            negativeIndex++; // Move the negativeIndex forward
        }
    }
}

int main() {
    vector<int> arr = {-12, 11, -13, -5, 6, -7, 5, -3, -6};
    rearrangeArray(arr);
    
    cout << "Rearranged array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
