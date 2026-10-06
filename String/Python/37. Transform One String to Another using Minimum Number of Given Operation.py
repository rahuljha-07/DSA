memo = []


# Helper function to calculate LCS using memoization
def LCS(n, m, str1, str2):
    # Base case: if either string is empty, the LCS is 0
    if n == 0 or m == 0:
        return 0

    # Check if the result is already calculated
    if memo[n][m] != -1:
        return memo[n][m]

    # If the last characters match, add 1 to the result and move both indices
    if str1[n - 1] == str2[m - 1]:
        memo[n][m] = 1 + LCS(n - 1, m - 1, str1, str2)
    else:
        # If last characters don't match, take the max by either moving `n` or `m`
        memo[n][m] = max(LCS(n - 1, m, str1, str2), LCS(n, m - 1, str1, str2))

    return memo[n][m]


def lcs(n, m, str1, str2):
    global memo
    # Initialize the memoization table with -1
    memo = [[-1 for j in range(m + 1)] for i in range(n + 1)]
    # Call the helper LCS function
    return LCS(n, m, str1, str2)


# Function to transform string A into string B
def transform(A, B):
    # Calculate LCS length
    lcsLength = lcs(len(A), len(B), A, B)

    # bascially we will delete char from A to make LCS and add remaining char from B to make
    # B
    # Number of deletions needed to transform A into B
    numDeletions = len(A) - lcsLength
    # Number of insertions needed to transform A into B
    numInsertions = len(B) - lcsLength

    # Return total number of operations (insertions + deletions)
    return numInsertions + numDeletions


A = "heap"
B = "pea"
print(transform(A, B))


'''
Time Complexity: O(n * m), where n and m are lengths of A and B.

Reason:
The transformation is based on LCS.
The LCS recursion has states based on indexes from A and B.
There are n * m such states, and memoization computes each one once.

Space Complexity: O(n * m)

Reason:
The memo table stores one answer for each pair of indexes.
The recursion stack is smaller than the table and does not dominate.
'''
