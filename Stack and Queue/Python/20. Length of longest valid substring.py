def findMaxLen(s):
    # Edge case: if the string is empty or has less than 2 characters
    if len(s) == 0 or len(s) < 2:
        return 0

    st = []

    # Traverse the string
    for i in range(len(s)):
        # Push the index of '(' to the stack
        if s[i] == '(':
            st.append(i)
        else:
            # If stack is not empty and top of stack is '(', pop it
            if len(st) != 0 and s[st[-1]] == '(':
                st.pop()
            else:
                # Otherwise, push the index of ')'
                st.append(i)

    maxLen = 0
    end = len(s)

    # Process indices left in the stack
    while len(st) != 0:
        ele = st[-1]
        st.pop()
        maxLen = max(maxLen, end - ele - 1)
        end = ele

    # Handle the case where entire string is valid
    maxLen = max(maxLen, end)

    return maxLen


s = "((())"
print("Maximum length of valid substring:", findMaxLen(s))


'''
Time Complexity: O(n)

Reason:
The string is scanned once and then the remaining invalid indexes in the
stack are processed once.

Space Complexity: O(n)

Reason:
The stack can store indexes of unmatched parentheses.
'''
