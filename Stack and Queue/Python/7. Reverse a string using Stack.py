def reverseString(S):
    st = []

    for c in S:
        st.append(c)

    reversedStr = ""

    while len(st) != 0:
        reversedStr += st[-1]
        st.pop()

    return reversedStr


S = "GeeksforGeeks"
print(reverseString(S))


'''
Time Complexity: O(n)

Reason:
All n characters are pushed once and popped once from the stack.

Space Complexity: O(n)

Reason:
The stack stores all characters of the string before they are popped.
'''
