def prec(c):
    if c == '^':
        return 3
    elif c == '*' or c == '/':
        return 2
    elif c == '+' or c == '-':
        return 1
    return -1


def infixToPostfix(s):
    st = []
    res = ""

    for i in range(len(s)):
        if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
            res += s[i]
        elif s[i] == '(':
            st.append(s[i])
        elif s[i] == ')':
            while len(st) != 0 and st[-1] != '(':
                res += st[-1]
                st.pop()
            if len(st) != 0:
                st.pop()
        else:
            while len(st) != 0 and prec(st[-1]) >= prec(s[i]):
                res += st[-1]
                st.pop()
            st.append(s[i])

    while len(st) != 0:
        res += st[-1]
        st.pop()

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
