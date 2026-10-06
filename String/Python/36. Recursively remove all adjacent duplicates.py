# Function to remove adjacent duplicates recursively
def removeAdjacentDuplicates(S):
    # Base case: if the string is empty or has one character, return it
    if len(S) == 0 or len(S) == 1:
        return S

    # To store the result after removing duplicates
    result = ""
    # Flag to check if duplicates were found
    hasAdjacentDuplicates = False

    i = 0
    # Iterate through the string to find adjacent duplicates
    while i < len(S):
        # Check if the current character is the same as the next one
        if i < len(S) - 1 and S[i] == S[i + 1]:
            # Set the flag to true
            hasAdjacentDuplicates = True
            # Skip all adjacent duplicates
            while i < len(S) - 1 and S[i] == S[i + 1]:
                # Move the index forward to skip duplicates
                i += 1
        else:
            # Add non-duplicate characters to result
            result += S[i]
        i += 1

    # If adjacent duplicates were found, call the function recursively
    return removeAdjacentDuplicates(result) if hasAdjacentDuplicates else result


input1 = "geeksforgeek"
input2 = "abccbccba"

print("Input:", input1, "-> Output:", removeAdjacentDuplicates(input1))
print("Input:", input2, "-> Output:", removeAdjacentDuplicates(input2))


'''
Time Complexity: O(n^2) in the worst case.

Reason:
Each recursive call scans the current string once.
In the worst case, only a small part is removed per call,
so there can be multiple scans of strings close to length n.
That makes the worst-case work O(n^2).

Space Complexity: O(n)

Reason:
Each call builds a temporary result string.
The recursion stack can also grow with the number of passes.
'''
