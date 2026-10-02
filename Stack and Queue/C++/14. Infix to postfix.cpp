#include <iostream>
#include <stack>
#include <string>

using namespace std;

// Function to determine the precedence of operators
int prec(char c) {
    if (c == '^') {
        return 3; // Highest precedence for exponentiation
    } else if (c == '*' || c == '/') {
        return 2; // Medium precedence for multiplication and division
    } else if (c == '+' || c == '-') {
        return 1; // Lowest precedence for addition and subtraction
    }
    return -1; // Non-operator
}

// Function to convert infix expression to postfix expression
string infixToPostfix(const string &s) {
    stack<char> st; // Stack to hold operators
    string res;     // Resulting postfix expression

    for (int i = 0; i < s.length(); i++) {
        // If the character is an operand (alphabetical)
        if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z')) {
            res += s[i]; // Append operand to result
        } 
        // If the character is '('
        else if (s[i] == '(') {
            st.push(s[i]); // Push '(' to stack
        } 
        // If the character is ')'
        else if (s[i] == ')') {
            // Pop from stack to result until '(' is found
            while (!st.empty() && st.top() != '(') {
                res += st.top(); // Append operator to result
                st.pop();
            }
            // Pop '(' from the stack
            if (!st.empty()) {
                st.pop();
            }
        } 
        // If the character is an operator
        else {
            while (!st.empty() && prec(st.top()) >= prec(s[i])) {
                res += st.top(); // Append operator to result
                st.pop();
            }
            st.push(s[i]); // Push current operator to stack
        }
    }

    // Pop all the remaining operators from the stack
    while (!st.empty()) {
        res += st.top(); // Append operator to result
        st.pop();
    }

    return res; // Return the resulting postfix expression
}

// Example usage
int main() {
    string infixExpression = "A+B*(C^D-E)^(F+G*H)"; // Example infix expression
    string postfixExpression = infixToPostfix(infixExpression);
    cout << "Infix expression: " << infixExpression << endl;
    cout << "Postfix expression: " << postfixExpression << endl; // Output result
    return 0;
}
