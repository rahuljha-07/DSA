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


# Function to check if the character is an operator
def isOperator(c):
    return c == '+' or c == '-' or c == '*' or c == '/' or c == '^'


# Function to convert infix expression to postfix expression
def infixToPostfix(s):
    # Stack to hold operators
    st = []
    # Resulting postfix expression
    res = ""

    for currentChar in s:
        # If the character is an operand (alphabetical)
        if (currentChar >= 'a' and currentChar <= 'z') or (currentChar >= 'A' and currentChar <= 'Z'):
            # Append operand to result
            res += currentChar
        # If the character is '('
        elif currentChar == '(':
            # Push '(' to stack
            st.append(currentChar)
        elif currentChar == ')':
            # Pop from stack to result until '(' is found
            while len(st) != 0 and st[-1] != '(':
                # Append operator to result
                res += st[-1]
                st.pop()
            # Pop '(' from the stack
            if len(st) != 0:
                st.pop()
        # If the character is an operator
        elif isOperator(currentChar):
            while len(st) != 0 and prec(st[-1]) >= prec(currentChar):
                res += st[-1]
                st.pop()
            # Push current operator to stack
            st.append(currentChar)

    # Pop all the remaining operators from the stack
    while len(st) != 0:
        res += st[-1]
        st.pop()

    # Return the resulting postfix expression
    return res


# Function to convert infix to prefix expression
def infixToPrefix(infix):
    # Create a copy of the infix expression
    reversedInfix = infix[::-1]

    chars = list(reversedInfix)
    # Swap '(' with ')' and vice versa
    for i in range(len(chars)):
        if chars[i] == '(':
            chars[i] = ')'
        elif chars[i] == ')':
            chars[i] = '('
    reversedInfix = "".join(chars)

    # Get the postfix expression of the modified reversed infix
    postfix = infixToPostfix(reversedInfix)

    postfix = postfix[::-1]
    # Return the resulting prefix expression
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
