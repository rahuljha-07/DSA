#include <iostream>
#include <stack>
#include <string>

using namespace std;

// Function to evaluate a prefix expression
int prefixEvaluation(const string &expression) {
    stack<int> st;  // Stack to hold operands

    // Loop through the expression from right to left
    for (int i = expression.length() - 1; i >= 0; i--) {
        char currentChar = expression[i];

        // If the character is a digit, convert it to an integer and push onto the stack
        if (currentChar >= '0' && currentChar <= '9') {
            st.push(currentChar - '0');  // Convert char to int
        } 
        // If the character is an operator
        else {
            // Pop two operands from the stack
            int operand1 = st.top();  // First operand
            st.pop();
            int operand2 = st.top();  // Second operand
            st.pop();

            // Perform the operation based on the operator
            switch (currentChar) {
                case '+':
                    st.push(operand1 + operand2);  // Addition
                    break;
                case '-':
                    st.push(operand1 - operand2);  // Subtraction
                    break;
                case '*':
                    st.push(operand1 * operand2);  // Multiplication
                    break;
                case '/':
                    // Ensure not to divide by zero
                    if (operand2 != 0) {
                        st.push(operand1 / operand2);  // Division
                    } else {
                        cout << "Error: Division by zero!" << endl;
                        return 0; // Return 0 for error handling
                    }
                    break;
                default:
                    cout << "Error: Unsupported operator!" << endl;
                    return 0; // Return 0 for error handling
            }
        }
    }

    // The final result will be the only element remaining in the stack
    return st.top();
}

// Example usage
int main() {
    string prefixExpression = "-+7*45+20"; // Example prefix expression
    int result = prefixEvaluation(prefixExpression);
    cout << "Result of prefix expression " << prefixExpression << " is: " << result << endl; // Output result
    return 0;
}
