# Function to find if there is a celebrity in the party or not
# A celebrity is defined as someone who is known by everyone but knows no one else
def celebrity(M, n):
    s = []

    # Push all people onto the stack
    for i in range(n):
        s.append(i)

    # Narrow down to one potential celebrity
    while len(s) >= 2:
        # Get the top person 'a' from the stack
        a = s[-1]
        s.pop()
        # Get the next top person 'b' from the stack
        b = s[-1]
        s.pop()

        # If person 'a' knows person 'b', 'a' cannot be a celebrity
        if M[a][b] == 1:
            s.append(b)
        # If person 'a' does not know person 'b', 'b' cannot be a celebrity
        else:
            s.append(a)

    # Potential candidate for celebrity
    potential = s[-1]
    s.pop()

    # Verify if the potential candidate is a real celebrity
    for i in range(n):
        # Skip self-check for potential
        if potential != i:
            # Check if the potential celebrity knows anyone or if not everyone knows them
            if M[potential][i] != 0 or M[i][potential] != 1:
                # Not a celebrity
                return -1

    # Return the index of the celebrity
    return potential


M = [[0, 1, 0], [0, 0, 0], [0, 1, 0]]
print(celebrity(M, 3))


'''
Time Complexity: O(n)

Reason:
All people are pushed once. The elimination phase removes two candidates and
pushes one back until one remains, and verification scans one row/column.

Space Complexity: O(n)

Reason:
The stack initially stores all n people.
'''
