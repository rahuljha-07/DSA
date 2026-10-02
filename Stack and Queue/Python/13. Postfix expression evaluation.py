def postfixEvaluation(expression):
    st = []

    for i in range(len(expression)):
        currentChar = expression[i]

        if currentChar >= '0' and currentChar <= '9':
            st.append(int(currentChar))
        else:
            operand2 = st[-1]
            st.pop()
            operand1 = st[-1]
            st.pop()

            if currentChar == '+':
                st.append(operand1 + operand2)
            elif currentChar == '-':
                st.append(operand1 - operand2)
            elif currentChar == '*':
                st.append(operand1 * operand2)
            elif currentChar == '/':
                if operand2 != 0:
                    st.append(int(operand1 / operand2))
                else:
                    print("Error: Division by zero!")
                    return 0
            else:
                print("Error: Unsupported operator!")
                return 0

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
