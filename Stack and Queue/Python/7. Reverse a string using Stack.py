# Function to reverse a string using a stack
def reverseString(S):
    # Stack to store characters temporarily
    st = []

    # Push each character of the string onto the stack
    for c in S:
        st.append(c)

    # Variable to store the reversed string
    reversedStr = ""

    # Pop characters from the stack and append to the result
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
