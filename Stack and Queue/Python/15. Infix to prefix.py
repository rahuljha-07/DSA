def prec(c):
    if c == '^':
        return 3
    elif c == '*' or c == '/':
        return 2
    elif c == '+' or c == '-':
        return 1
    return -1


def isOperator(c):
    return c == '+' or c == '-' or c == '*' or c == '/' or c == '^'


def infixToPostfix(s):
    st = []
    res = ""

    for currentChar in s:
        if (currentChar >= 'a' and currentChar <= 'z') or (currentChar >= 'A' and currentChar <= 'Z'):
            res += currentChar
        elif currentChar == '(':
            st.append(currentChar)
        elif currentChar == ')':
            while len(st) != 0 and st[-1] != '(':
                res += st[-1]
                st.pop()
            if len(st) != 0:
                st.pop()
        elif isOperator(currentChar):
            while len(st) != 0 and prec(st[-1]) >= prec(currentChar):
                res += st[-1]
                st.pop()
            st.append(currentChar)

    while len(st) != 0:
        res += st[-1]
        st.pop()

    return res


def infixToPrefix(infix):
    reversedInfix = infix[::-1]

    chars = list(reversedInfix)
    for i in range(len(chars)):
        if chars[i] == '(':
            chars[i] = ')'
        elif chars[i] == ')':
            chars[i] = '('
    reversedInfix = "".join(chars)

    postfix = infixToPostfix(reversedInfix)

    postfix = postfix[::-1]
    return postfix


infixExpression = "(A+B)*C-D"
prefixExpression = infixToPrefix(infixExpression)
print("Infix expression:", infixExpression)
print("Prefix expression:", prefixExpression)


'''
Time Complexity: O(n)

Reason:
The infix string is reversed, parentheses are swapped, postfix conversion
scans once, and the final postfix is reversed. These linear steps add to O(n).

Space Complexity: O(n)

Reason:
The reversed string, operator stack, and output string can each grow with n.
'''
