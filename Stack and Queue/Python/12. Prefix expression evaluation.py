def prefixEvaluation(expression):
    st = []

    for i in range(len(expression) - 1, -1, -1):
        currentChar = expression[i]

        if currentChar >= '0' and currentChar <= '9':
            st.append(int(currentChar))
        else:
            operand1 = st[-1]
            st.pop()
            operand2 = st[-1]
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


prefixExpression = "-+7*45+20"
result = prefixEvaluation(prefixExpression)
print("Result of prefix expression", prefixExpression, "is:", result)


'''
Time Complexity: O(n)

Reason:
The expression is scanned once from right to left. Each character causes a
constant-time stack push, pop, or arithmetic operation.

Space Complexity: O(n)

Reason:
The operand stack can store up to n operands in the worst case.
'''
