#include <iostream>
#include <stack>
#include <string>
#include <algorithm> // for reverse

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

// Function to check if the character is an operator
bool isOperator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/' || c == '^');
}

// Function to convert infix expression to postfix expression
string infixToPostfix(const string &s) {
    stack<char> st; // Stack to hold operators
    string res;     // Resulting postfix expression

    for (char currentChar : s) {
        // If the character is an operand (alphabetical)
        if ((currentChar >= 'a' && currentChar <= 'z') || (currentChar >= 'A' && currentChar <= 'Z')) {
            res += currentChar; // Append operand to result
        } 
        // If the character is '('
        else if (currentChar == '(') {
            st.push(currentChar); // Push '(' to stack
        } 
        // If the character is ')'
        else if (currentChar == ')') {
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
        else if (isOperator(currentChar)) {
            while (!st.empty() && prec(st.top()) >= prec(currentChar)) {
                res += st.top(); // Append operator to result
                st.pop();
            }
            st.push(currentChar); // Push current operator to stack
        }
    }

    // Pop all the remaining operators from the stack
    while (!st.empty()) {
        res += st.top(); // Append operator to result
        st.pop();
    }

    return res; // Return the resulting postfix expression
}

// Function to convert infix to prefix expression
string infixToPrefix(const string &infix) {
    string reversedInfix = infix; // Create a copy of the infix expression
    reverse(reversedInfix.begin(), reversedInfix.end()); // Reverse the infix expression

    // Swap '(' with ')' and vice versa
    for (int i = 0; i < reversedInfix.length(); i++) {
        if (reversedInfix[i] == '(') {
            reversedInfix[i] = ')';
        } else if (reversedInfix[i] == ')') {
            reversedInfix[i] = '(';
        }
    }

    // Get the postfix expression of the modified reversed infix
    string postfix = infixToPostfix(reversedInfix);

    reverse(postfix.begin(), postfix.end());
    return postfix; // Return the resulting prefix expression
}

// Example usage
int main() {
    string infixExpression = "(A+B)*C-D"; // Example infix expression
    string prefixExpression = infixToPrefix(infixExpression);
    cout << "Infix expression: " << infixExpression << endl;
    cout << "Prefix expression: " << prefixExpression << endl; // Output result
    return 0;
}
