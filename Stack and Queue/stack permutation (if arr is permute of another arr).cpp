#include <iostream>
#include <stack>
#include <vector>

using namespace std;

// Function to check if arr2 is a stack permutation of arr1
bool isStackPermutation(const vector<int>& arr1, const vector<int>& arr2) {
    stack<int> s; // Stack to hold elements temporarily
    int n = arr1.size();
    
    int j = 0; // Pointer for output array (arr2)
    
    // Iterate through each element in arr1
    for (int i = 0; i < n; ++i) {
        s.push(arr1[i]); // Push current element onto the stack

        // While the stack is not empty and the top of the stack matches arr2[j]
        while (!s.empty() && s.top() == arr2[j]) {
            s.pop(); // Pop from the stack
            j++; // Move to the next element in arr2
        }
    }

    // If we've matched all elements in arr2, then it's a valid permutation
    return j == n;
}

// Example usage
int main() {
    vector<int> arr1 = {1, 2, 3};
    vector<int> arr2 = {2, 1, 3};

    if (isStackPermutation(arr1, arr2)) {
        cout << "YES" << endl; // Output: YES
    } else {
        cout << "Not Possible" << endl;
    }

    arr1 = {1, 2, 3};
    arr2 = {3, 1, 2};

    if (isStackPermutation(arr1, arr2)) {
        cout << "YES" << endl; // Output: YES
    } else {
        cout << "Not Possible" << endl; // Output: Not Possible
    }

    return 0;
}
