def ispar(x):
    s = []

    for i in range(len(x)):
        ch = x[i]

        # If opening bracket, push onto stack
        if ch == '(' or ch == '{' or ch == '[':
            s.append(ch)

        else:
            # If stack is empty and closing bracket appears
            if len(s) == 0:
                return False

            # Get top element of stack
            top = s[-1]

            # Check matching pairs
            if (
                (ch == ')' and top != '(') or
                (ch == '}' and top != '{') or
                (ch == ']' and top != '[')
            ):
                return False

            # Pop matched opening bracket
            s.pop()

    # Balanced only if stack is empty
    return len(s) == 0


'''
Time Complexity:
O(n)

Reason:

We traverse the string once.

Each character is pushed onto or popped from the stack
at most once.

Therefore:
O(n)


Space Complexity:
O(n)

Reason:

In the worst case, all characters are opening brackets.

Example:
"(((([[{{"

Then all of them are stored in the stack.

Therefore:
O(n)
'''