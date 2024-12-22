// Function to find the next greater element for each element in the array
// same for NGL reverse the loop
vector<long long> nextLargerElement(vector<long long> arr, int n) {
    vector<long long> v;     // Vector to store the result (next greater elements)
    stack<long long> st;     // Stack to keep track of the next greater elements

    // Traverse the array from the end to the beginning
    for (int i = n - 1; i >= 0; i--) {
        // If the stack is empty, there is no greater element on the right
        if (st.size() == 0) {
            v.push_back(-1); // No greater element found, push -1 to result
        }
        // If the stack is not empty and the top element is greater than arr[i]
        else if (st.size() > 0 && arr[i] < st.top()) {
            v.push_back(st.top()); // Top element is the next greater, push it to result
        }
        // If the stack is not empty and the top element is not greater than arr[i]
        else if (st.size() > 0 && arr[i] >= st.top()) {
            // Pop elements from the stack until finding a greater element or the stack is empty
            while (st.size() > 0 && arr[i] >= st.top()) {
                st.pop();
            }
            // If stack is empty, no greater element found
            if (st.size() == 0) {
                v.push_back(-1);
            } else {
                // Found a greater element, push it to result
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
