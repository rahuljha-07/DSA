def hasRedundantBrackets(s):
    st = []
    ans = False

    for i in range(len(s)):
        if s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/' or s[i] == '(':
            st.append(s[i])
        elif s[i] == ')':
            if st[-1] == '(':
                ans = True
                break

            while len(st) != 0 and (st[-1] == '+' or st[-1] == '-' or st[-1] == '*' or st[-1] == '/'):
                st.pop()

            if len(st) != 0 and st[-1] == '(':
                st.pop()

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
