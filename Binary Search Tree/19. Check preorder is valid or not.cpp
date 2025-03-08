#include <climits>

class Solution {
public:
    int index = 0;  // Track the current index in the preorder array

    // Recursive helper function to verify BST preorder condition
    void solve(int arr[], int& N, int minVal, int maxVal) {
        // If all elements are processed, return
        if (index >= N) return;

        // Check if the current element falls within the allowed range
        if (arr[index] < minVal || arr[index] > maxVal) return;

        // Set current element as root for this subtree
        int curr = arr[index];
        index++;  // Move to the next element

        // Recursively check left subtree with updated max bound
        solve(arr, N, minVal, curr);

        // Recursively check right subtree with updated min bound
        solve(arr, N, curr, maxVal);
    }

    // Main function to verify if array represents a valid BST preorder traversal
    int canRepresentBST(int arr[], int N) {
        int minVal = INT_MIN;  // Initial minimum boundary
        int maxVal = INT_MAX;  // Initial maximum boundary

        // Begin recursive validation of BST conditions
        solve(arr, N, minVal, maxVal);

        // Check if all elements in the array were processed correctly
        return (index == N) ? 1 : 0;
    }
};
// kashish mahendatta video
#include <iostream>
#include <stack>
using namespace std;

int canRepresentBST(int arr[], int n) {
    stack<int> s;  // Stack to track nodes while constructing BST
    int parent = 0; // Keeps track of the last removed node (lower bound for the right subtree)

    // Iterate through the given preorder array
    for (int i = 0; i < n; i++) {
        // If stack is empty OR current element is smaller than stack top, it belongs to the left subtree
        if (s.empty() || arr[i] < s.top()) {
            // If current element is smaller than the last removed element (parent), return false
            // (Right subtree elements must be larger than their ancestors)
            if (parent > arr[i]) {
                return 0; // Invalid BST Preorder
            }
            s.push(arr[i]); // Push the element into the stack (part of left subtree)
        } 
        else {
            // If current element is greater than stack top, we are in the right subtree
            while (!s.empty() && s.top() < arr[i]) {
                parent = s.top(); // Update parent (last popped element)
                s.pop(); // Remove elements that are smaller than the current element
            }
            s.push(arr[i]); // Push the current element as a new node
        }
    }
    return 1; // If all elements are processed without issue, it's a valid BST preorder
}

// Driver Code to test the function
int main() {
    int arr1[] = {40, 30, 35, 80, 100}; // Valid BST Preorder
    int n1 = sizeof(arr1) / sizeof(arr1[0]);

    int arr2[] = {40, 30, 35, 20, 80}; // Invalid BST Preorder
    int n2 = sizeof(arr2) / sizeof(arr2[0]);

    cout << "Test 1 (Valid BST): " << (canRepresentBST(arr1, n1) ? "YES" : "NO") << endl;
    cout << "Test 2 (Invalid BST): " << (canRepresentBST(arr2, n2) ? "YES" : "NO") << endl;

    return 0;
}
