#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

// Function to find the next smaller element for each element in the array
// same for NSL reverse the loop

vector<long long> nextSmallerElement(vector<long long> arr, int n) {
    vector<long long> v;     // Vector to store the result (next smaller elements)
    stack<long long> st;     // Stack to keep track of the next smaller elements

    // Traverse the array from the end to the beginning
    for (int i = n - 1; i >= 0; i--) {
        // If the stack is empty, there is no smaller element on the right
        if (st.empty()) {
            v.push_back(-1); // No smaller element found, push -1 to result
        }
        // If the stack is not empty and the top element is smaller than arr[i]
        else if (st.top() < arr[i]) {
            v.push_back(st.top()); // Top element is the next smaller, push it to result
        }
        // If the stack is not empty and the top element is not smaller than arr[i]
        else {
            // Pop elements from the stack until finding a smaller element or the stack is empty
            while (!st.empty() && arr[i] <= st.top()) {
                st.pop();
            }
            // If stack is empty, no smaller element found
            if (st.empty()) {
                v.push_back(-1);
            } else {
                // Found a smaller element, push it to result
                v.push_back(st.top());
            }
        }

        // Push the current element onto the stack
        st.push(arr[i]);
    }

    // Reverse the result vector to match the original array order
    reverse(v.begin(), v.end());
    
    return v;
}
