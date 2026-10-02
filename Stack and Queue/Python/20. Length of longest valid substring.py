def findMaxLen(s):
    if len(s) == 0 or len(s) < 2:
        return 0

    st = []

    for i in range(len(s)):
        if s[i] == '(':
            st.append(i)
        else:
            if len(st) != 0 and s[st[-1]] == '(':
                st.pop()
            else:
                st.append(i)

    maxLen = 0
    end = len(s)

    while len(st) != 0:
        ele = st[-1]
        st.pop()
        maxLen = max(maxLen, end - ele - 1)
        end = ele

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
