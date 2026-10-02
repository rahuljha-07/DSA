def countRev(s):
    if len(s) & 1:
        return -1

    st = []
    unmatchedClosing = 0
    unmatchedOpening = 0

    for ch in s:
        if ch == '{':
            st.append(ch)
            unmatchedOpening += 1
        elif ch == '}' and len(st) != 0 and st[-1] == '{':
            st.pop()
            unmatchedOpening -= 1
        else:
            unmatchedClosing += 1

    reversalsForClosing = unmatchedClosing // 2 if unmatchedClosing % 2 == 0 else unmatchedClosing // 2 + 1
    reversalsForOpening = unmatchedOpening // 2 if unmatchedOpening % 2 == 0 else unmatchedOpening // 2 + 1

    return reversalsForClosing + reversalsForOpening


s = "{{{{}}"
print("Minimum reversals needed:", countRev(s))


'''
Time Complexity: O(n), where n is the string length.

Reason:
The string is traversed once.
Each bracket is either pushed, popped, or counted, and each stack
operation takes O(1).

Space Complexity: O(n)

Reason:
In the worst case, all brackets can be opening brackets,
so the stack may store up to n characters.
'''
