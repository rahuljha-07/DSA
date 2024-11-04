// Function to reverse a string using a stack
string reverseString(const string &S) {
    // Stack to store characters temporarily
    stack<char> st;

    // Push each character of the string onto the stack
    for (char c : S) {
        st.push(c);
    }

    // Variable to store the reversed string
    string reversedStr;

    // Pop characters from the stack and append to the result
    while (!st.empty()) {
        reversedStr += st.top();
        st.pop();
    }

    return reversedStr;
}
