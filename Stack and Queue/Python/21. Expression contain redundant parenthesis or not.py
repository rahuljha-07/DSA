def hasRedundantBrackets(s):
    # Stack to hold operators and brackets
    st = []
    # Flag to check for redundant brackets
    ans = False

    # Traverse each character in the string
    for i in range(len(s)):
        # If current character is an operator or an opening bracket, push it onto the stack
        if s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/' or s[i] == '(':
            st.append(s[i])
        # If current character is a closing bracket, check for redundancy
        elif s[i] == ')':
            # If the top element is an opening bracket without any operator, mark as
            # redundant
            if st[-1] == '(':
                ans = True
                break

            # Remove elements from stack until an opening bracket '(' is found
            while len(st) != 0 and (st[-1] == '+' or st[-1] == '-' or st[-1] == '*' or st[-1] == '/'):
                st.pop()

            # Pop the opening bracket '(' from the stack
            if len(st) != 0 and st[-1] == '(':
                st.pop()

    # Return true if redundant brackets are found, otherwise false
    return ans


s = "((a+b))"
if hasRedundantBrackets(s):
    print("The expression contains redundant brackets.")
else:
    print("The expression does not contain redundant brackets.")


'''
Time Complexity: O(n)

Reason:
The expression is scanned once. Every pushed operator or bracket is popped
at most once.

Space Complexity: O(n)

Reason:
The stack can store operators and opening brackets from the expression.
'''
