# Function to count the minimum number of reversals to balance a given string of brackets
def countRev(s):
    # If the length of the string is odd, it can't be balanced
    if len(s) & 1:
        return -1

    # Stack to store unmatched opening brackets
    st = []
    # Count of unmatched closing brackets
    unmatchedClosing = 0
    # Count of unmatched opening brackets
    unmatchedOpening = 0

    # Traverse each character in the string
    for ch in s:
        # If it's an opening bracket, push it to the stack and increment unmatched opening
        # count
        if ch == '{':
            st.append(ch)
            unmatchedOpening += 1
        # If it's a closing bracket
        elif ch == '}' and len(st) != 0 and st[-1] == '{':
            # If it matches with the top of the stack, pop the stack and decrement unmatched
            # opening count
            st.pop()
            unmatchedOpening -= 1
        # If there's no matching opening bracket, increment unmatched closing count
        else:
            unmatchedClosing += 1

    # Calculate the minimum reversals for unmatched closing brackets
    reversalsForClosing = unmatchedClosing // 2 if unmatchedClosing % 2 == 0 else unmatchedClosing // 2 + 1
    # Calculate the minimum reversals for unmatched opening brackets
    reversalsForOpening = unmatchedOpening // 2 if unmatchedOpening % 2 == 0 else unmatchedOpening // 2 + 1

    # Return the total reversals required
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
