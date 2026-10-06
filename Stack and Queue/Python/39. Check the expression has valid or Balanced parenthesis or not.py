# Function to check if the brackets in a given string are balanced
def ispar(x):
    # Stack to keep track of opening brackets
    s = []

    # Loop through each character in the string
    for i in range(len(x)):
        # If the character is an opening bracket, push it onto the stack
        if x[i] == '(' or x[i] == '{' or x[i] == '[':
            s.append(x[i])
        # If the character is a closing bracket
        else:
            # If the stack is empty, there's no matching opening bracket
            if len(s) == 0:
                return False

            # Get the top element of the stack (the most recent opening bracket)
            c = s[-1]

            # Check if the closing bracket matches the top opening bracket
            if (x[i] == ')' and c != '(') or (x[i] == '}' and c != '{') or (x[i] == ']' and c != '['):
                # Mismatch found
                return False

            # Pop the matching opening bracket from the stack
            s.pop()

    # If the stack is empty, all brackets were balanced; otherwise, return false
    return len(s) == 0


x = "{([])}"
print(ispar(x))


'''
Time Complexity: O(n)

Reason:
The expression is scanned once. Each opening bracket is pushed once and
popped once when a matching closing bracket is found.

Space Complexity: O(n)

Reason:
The stack can store all opening brackets in the worst case.
'''
