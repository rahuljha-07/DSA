# =========================================================
# 1. USING SWAPPING + BACKTRACKING
# =========================================================

def permute(s, start, end, ans):
    # Base case: permutation is complete
    if start == end:
        # Store the current permutation in the list
        ans.append("".join(s))

    else:
        # Try every character at current position
        for i in range(start, end + 1):

            # Swap current character with start
            s[i], s[start] = s[start], s[i]

            # Recur for remaining characters
            permute(s, start + 1, end, ans)

            # Backtrack
            s[i], s[start] = s[start], s[i]


# Function to find all permutations of a string
def find_permutation_swap(s):
    # list to store all permutations
    ans = []

    # Get the length of the string
    n = len(s)

    # Return an empty list if the string is empty
    if n == 0:
        return ans

    # Convert string to list because Python strings are immutable
    s = list(s)

    # Call the permute function to generate permutations
    permute(s, 0, n - 1, ans)

    # Sort in lexicographical order
    ans.sort()

    # Return the list containing all permutations
    return ans


'''
Time Complexity:
O(n * n!)

Reason:

There are n! possible permutations.

For each completed permutation, we convert the character list
into a string using:

"".join(s)

which takes O(n).

Therefore:

O(n * n!)

Sorting the n! permutations can additionally take approximately:

O(n! * log(n!) * n)

because string comparisons may take O(n).


Space Complexity:
O(n * n!)

Reason:

There are n! permutations stored in ans.

Each permutation has length n.

Therefore:

O(n * n!)

Ignoring the output list, recursion depth is O(n).
'''



# =========================================================
# 2. USING INPUT / OUTPUT METHOD
# =========================================================

def solve(input, output, ans):
    # Base case: input is empty
    if len(input) == 0:
        ans.append(output)
        return

    # Choose each character as next character
    for i in range(len(input)):

        # Remove current character from input
        remaining = input[:i] + input[i + 1:]

        # Include current character in output
        solve(
            remaining,
            output + input[i],
            ans
        )


# Function to find all unique permutations of a given string
def find_permutation_ip_op(S):
    # Initialize a list to store the permutations
    ans = []

    solve(S, "", ans)

    # Return the list containing all unique permutations
    return ans


'''
Time Complexity:
O(n * n!)

Reason:

There are n! permutations.

For every recursive call, Python creates new strings using:

input[:i]
input[i + 1:]
output + input[i]

String creation can take O(n).

Therefore:

O(n * n!)


Space Complexity:
O(n * n!)

Reason:

We store n! permutations.

Each permutation has length n.

Therefore:

O(n * n!)

Ignoring output storage, recursion depth is O(n),
although temporary strings are also created during recursion.
'''



# =========================================================
# EXAMPLE
# =========================================================

s = "abc"

print("Using Swap + Backtracking:")

permutations = find_permutation_swap(s)

for permutation in permutations:
    print(permutation)


print("\nUsing Input / Output Method:")

permutations = find_permutation_ip_op(s)

for permutation in permutations:
    print(permutation)
