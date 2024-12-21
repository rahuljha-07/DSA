#include <vector>
#include <algorithm> 
using namespace std;

vector<int> findTwoElement(vector<int> arr, int n) {
    // Create a vector to hold the result
    vector<int> ans(2); // To store the repeating and missing elements

    // Rearrange the array elements to their corresponding indices
    for (int i = 0; i < n;) {
        // Check if the current element is not in the correct position
        if (arr[i] != arr[arr[i] - 1]) {
            // Swap the element with the element at its correct index
            swap(arr[i], arr[arr[i] - 1]);
        } else {
            // Move to the next element if the current one is in the correct position
            i++;
        }
    }

    // Find the repeating and missing elements
    for (int i = 0; i < n; i++) {
        // Check if the current element is not equal to its expected value (i + 1)
        if (arr[i] != (i + 1)) {
            ans[0] = arr[i];    // The repeating element
            ans[1] = i + 1;     // The missing element
            break;               // No need to continue searching
        }
    }

    return ans; // Return the result vector containing the repeating and missing elements
}
