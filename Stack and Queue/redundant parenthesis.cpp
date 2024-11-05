#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool hasRedundantBrackets(const string& s) {
    stack<char> st;  // Stack to hold operators and brackets
    bool ans = false;  // Flag to check for redundant brackets

    // Traverse each character in the string
    for (int i = 0; i < s.size(); i++) {
        // If current character is an operator or an opening bracket, push it onto the stack
        if (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/' || s[i] == '(') {
            st.push(s[i]);
        }
        // If current character is a closing bracket, check for redundancy
        else if (s[i] == ')') {
            // If the top element is an opening bracket without any operator, mark as redundant
            if (st.top() == '(') {
                ans = true;
                break;
            }
            
            // Remove elements from stack until an opening bracket '(' is found
            while (!st.empty() && (st.top() == '+' || st.top() == '-' || st.top() == '*' || st.top() == '/')) {
                st.pop();
            }
            
            // Pop the opening bracket '(' from the stack
            if (!st.empty() && st.top() == '(') {
                st.pop();
            }
        }
    }

    // Return true if redundant brackets are found, otherwise false
    return ans;
}

int main() {
    string s = "((a+b))";  // Example expression
    if (hasRedundantBrackets(s)) {
        cout << "The expression contains redundant brackets." << endl;
    } else {
        cout << "The expression does not contain redundant brackets." << endl;
    }
    return 0;
}
