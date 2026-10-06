# Function to evaluate a postfix expression
def postfixEvaluation(expression):
    # Stack to hold operands
    st = []

    # Loop through the expression from left to right
    for i in range(len(expression)):
        currentChar = expression[i]

        # If the character is a digit, convert it to an integer and push onto the stack
        if currentChar >= '0' and currentChar <= '9':
            # Convert char to int
            st.append(int(currentChar))
        # If the character is an operator
        else:
            # Pop two operands from the stack
            # Second operand (top of the stack)
            operand2 = st[-1]
            st.pop()
            # First operand (next on the stack)
            operand1 = st[-1]
            st.pop()

            if currentChar == '+':
                # Addition
                # Subtraction
                st.append(operand1 + operand2)
            elif currentChar == '-':
                # Multiplication
                st.append(operand1 - operand2)
            elif currentChar == '*':
                st.append(operand1 * operand2)
            elif currentChar == '/':
                # Ensure not to divide by zero
                if operand2 != 0:
                    # Division
                    st.append(int(operand1 / operand2))
                else:
                    print("Error: Division by zero!")
                    # Return 0 for error handling
                    return 0
            else:
                print("Error: Unsupported operator!")
                return 0

    # The final result will be the only element remaining in the stack
    return st[-1]


postfixExpression = "234*+82/-"
result = postfixEvaluation(postfixExpression)
print("Result of postfix expression", postfixExpression, "is:", result)


'''
Time Complexity: O(n)

Reason:
The expression is scanned once from left to right. Each character performs
constant stack or arithmetic work.

Space Complexity: O(n)

Reason:
The operand stack can hold up to n operands in the worst case.
'''
