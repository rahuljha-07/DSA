# Function to solve and store all substrings in a list
def solve(input, output, ans):
    # Base case: if input string is empty
    if len(input) == 0:
        # Store the current substring in the list
        if len(output) > 0:
            ans.append(output)
        return

    # Exclude the first character
    excludeFirstChar = output

    # Include the first character
    includeFirstChar = output
    # Append the first character
    includeFirstChar += input[0]

    # Remove the first character from input
    input = input[1:]

    # Recur for both choices
    solve(input, excludeFirstChar, ans)

    # Call with including the character
    solve(input, includeFirstChar, ans)


# Example
s = "abc"

ans = []

solve(s, "", ans)

print("All Subsequences of", s, ":")

for subsequence in ans:
    print(subsequence)


'''
Time Complexity:
O(n * 2^n)

Reason:

For every character, we have 2 choices:

1. Exclude the character
2. Include the character

So there are:

2^n

recursive possibilities.

Also, in Python, string operations such as:

input[1:]
includeFirstChar += input[0]

can involve copying strings.

Therefore, a practical bound is:

O(n * 2^n)


Space Complexity:
O(n * 2^n)

Reason:

The recursion depth is O(n).

But we also store all non-empty subsequences in ans.

There are:

2^n - 1

non-empty subsequences.

Each subsequence can have length up to n.

Therefore, including the output storage:

O(n * 2^n)

If we ignore the output list ans,
the recursive auxiliary space is O(n).
'''
