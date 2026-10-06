# Recursive helper function to compute minimum edit distance
def minDistanceHelper(word1, word2, dp, i, j):

    # If already computed, return it
    if dp[i][j] != -1:
        return dp[i][j]

    # If first string is empty,
    # insert all characters of second string
    if i == 0:
        dp[i][j] = j
        return dp[i][j]

    # If second string is empty,
    # delete all characters of first string
    if j == 0:
        dp[i][j] = i
        return dp[i][j]

    # If last characters match,
    # no operation is needed
    if word1[i - 1] == word2[j - 1]:

        dp[i][j] = minDistanceHelper(
            word1,
            word2,
            dp,
            i - 1,
            j - 1
        )

        return dp[i][j]

    else:
        # Insert operation
        insertOp = minDistanceHelper(
            word1,
            word2,
            dp,
            i,
            j - 1
        )

        # Delete operation
        deleteOp = minDistanceHelper(
            word1,
            word2,
            dp,
            i - 1,
            j
        )

        # Replace operation
        replaceOp = minDistanceHelper(
            word1,
            word2,
            dp,
            i - 1,
            j - 1
        )

        # Minimum of all three operations
        dp[i][j] = 1 + min(
            insertOp,
            deleteOp,
            replaceOp
        )

        return dp[i][j]


# Main function
def minDistance(word1, word2):

    # Get lengths of both strings
    m = len(word1)
    n = len(word2)

    # Memoization table initialized with -1
    dp = [
        [-1 for _ in range(n + 1)]
        for _ in range(m + 1)
    ]

    # Start from full lengths of both strings
    return minDistanceHelper(
        word1,
        word2,
        dp,
        m,
        n
    )


'''
Time Complexity:
O(m * n)

Reason:

The state is defined by:

dp[i][j]

where:
i can range from 0 to m
j can range from 0 to n

So there are at most:

(m + 1) * (n + 1)

different states.

Because of memoization, each state is calculated only once.

Therefore:
O(m * n)


Space Complexity:
O(m * n)

Reason:

The memoization table dp has size:

(m + 1) x (n + 1)

Therefore:
O(m * n)

There is also recursion stack space of up to O(m + n),
but O(m * n) dominates it.
'''
