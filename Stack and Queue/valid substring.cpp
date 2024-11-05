#include <iostream>
#include <stack>
#include <string>
#include <algorithm>
using namespace std;

int findMaxLen(string s) {
    // Edge case: if the string is empty or has less than 2 characters
    if (s.empty() || s.length() < 2) {
        return 0;
    }

    stack<int> st;

    // Traverse the string
    for (int i = 0; i < s.length(); i++) {
        // Push the index of '(' to the stack
        if (s[i] == '(') {
            st.push(i);
        } else {
            // If stack is not empty and top of stack is '(', pop it
            if (!st.empty() && s[st.top()] == '(') {
                st.pop();
            } else {
                // Otherwise, push the index of ')'
                st.push(i);
            }
        }
    }

    int maxLen = 0;
    int end = s.length();

    // Process indices left in the stack
    while (!st.empty()) {
        int ele = st.top();
        st.pop();
        maxLen = max(maxLen, end - ele - 1);
        end = ele;
    }

    // Handle the case where entire string is valid
    maxLen = max(maxLen, end);

    return maxLen;
}

int main() {
    string s = "((())";
    cout << "Maximum length of valid substring: " << findMaxLen(s) << endl;
    return 0;
}
