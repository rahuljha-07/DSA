# Function to determine the precedence of operators
def prec(c):
    if c == '^':
        # Highest precedence for exponentiation
        return 3
    elif c == '*' or c == '/':
        # Medium precedence for multiplication and division
        return 2
    elif c == '+' or c == '-':
        # Lowest precedence for addition and subtraction
        # Non-operator
        return 1
    return -1


# Function to convert infix expression to postfix expression
def infixToPostfix(s):
    # Stack to hold operators
    st = []
    # Resulting postfix expression
    res = ""

    for i in range(len(s)):
        # If the character is an operand (alphabetical)
        if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
            # Append operand to result
            res += s[i]
        # If the character is '('
        elif s[i] == '(':
            # Push '(' to stack
            st.append(s[i])
        elif s[i] == ')':
            # Pop from stack to result until '(' is found
            while len(st) != 0 and st[-1] != '(':
                # Append operator to result
                res += st[-1]
                st.pop()
            # Pop '(' from the stack
            if len(st) != 0:
                st.pop()
        # If the character is an operator
        else:
            while len(st) != 0 and prec(st[-1]) >= prec(s[i]):
                res += st[-1]
                st.pop()
            # Push current operator to stack
            st.append(s[i])

    # Pop all the remaining operators from the stack
    while len(st) != 0:
        res += st[-1]
        st.pop()

    # Return the resulting postfix expression
    return res


infixExpression = "A+B*(C^D-E)^(F+G*H)"
postfixExpression = infixToPostfix(infixExpression)
print("Infix expression:", infixExpression)
print("Postfix expression:", postfixExpression)


'''
Time Complexity: O(n)

Reason:
Each character is processed once. Operators may be popped in while loops,
but every operator is pushed and popped at most once.

Space Complexity: O(n)

Reason:
The operator stack and result string can grow with the expression length.
'''
