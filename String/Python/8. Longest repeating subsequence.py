# =========================================================
# 1. RECURSION + MEMOIZATION
# TOP-DOWN APPROACH
# =========================================================

def LRSUtil(str, i, j, t):

    # Base case
    if i == 0 or j == 0:
        # No further characters to compare
        return 0

    # If already calculated
    if t[i][j] != -1:
        return t[i][j]

    # If characters match and indices are different
    if str[i - 1] == str[j - 1] and i != j:

        # Otherwise, take the maximum of excluding either character
        t[i][j] = 1 + LRSUtil(
            str,
            i - 1,
            j - 1,
            t
        )

    else:

        t[i][j] = max(
            LRSUtil(str, i, j - 1, t),
            LRSUtil(str, i - 1, j, t)
        )

    # Return the computed result
    return t[i][j]


# Function to find the length of the longest repeating subsequence
def LongestRepeatingSubsequence_memo(str):

    # Length of the input string
    n = len(str)

    # Initialize memoization table with -1
    t = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    # Call the utility function starting from the full length of the string
    return LRSUtil(str, n, n, t)


'''
Time Complexity:
O(n^2)

Reason:

There are n * n possible states:

t[i][j]

Each state is calculated only once because of memoization.

Therefore:
O(n^2)


Space Complexity:
O(n^2)

Reason:

The memoization table contains:

(n + 1) * (n + 1)

entries.

Therefore:
O(n^2)

There is also recursion stack space of O(n),
but O(n^2) dominates it.
'''



# =========================================================
# 2. ITERATIVE DP
# BOTTOM-UP APPROACH
# =========================================================

def LongestRepeatingSubsequence_dp(str):

    n = len(str)

    # Copy of input string
    str1 = str

    m = n

    # Create 2D DP table initialized with 0
    t = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # First column is already initialized to 0
    for i in range(n + 1):
        t[i][0] = 0

    # First row is already initialized to 0
    for j in range(m + 1):
        t[0][j] = 0

    # Fill the table
    for i in range(1, n + 1):

        for j in range(1, m + 1):

            # Characters match but indices must be different
            if str[i - 1] == str1[j - 1] and i != j:

                t[i][j] = 1 + t[i - 1][j - 1]

            else:

                t[i][j] = max(
                    t[i][j - 1],
                    t[i - 1][j]
                )

    return t[n][m]


# =========================================================
# EXAMPLE
# =========================================================

s = "AABEBCDD"

print(
    "Using Recursion + Memoization:",
    LongestRepeatingSubsequence_memo(s)
)

print(
    "Using Bottom-Up DP:",
    LongestRepeatingSubsequence_dp(s)
)


'''
Time Complexity:
O(n^2)

Reason:

We fill a DP table of size:

(n + 1) x (n + 1)

Each cell takes O(1) time to calculate.

Therefore:
O(n^2)


Space Complexity:
O(n^2)

Reason:

We create a 2D DP table of size:

(n + 1) x (n + 1)

Therefore:
O(n^2)
'''
