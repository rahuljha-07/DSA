t = []


# Function to compute LCS
def LCS(x, y, n, m):
    # Base case: If either string is empty, LCS is 0
    if n == 0 or m == 0:
        return 0
    # If the value is already computed, return it
    if t[n][m] != -1:
        return t[n][m]
    # If the last characters match, add 1 to the result of the remaining strings
    if x[n - 1] == y[m - 1]:
        t[n][m] = 1 + LCS(x, y, n - 1, m - 1)
    else:
        # If the last characters do not match, take the maximum LCS by excluding
        # one character from either string
        t[n][m] = max(LCS(x, y, n - 1, m), LCS(x, y, n, m - 1))
    return t[n][m]


# Helper function to initialize the memoization table and compute LCS
def computeLCS(x, y):
    n = len(x)
    m = len(y)
    # Resize and initialize the memoization table with -1
    t[:] = [[-1] * (m + 1) for _ in range(n + 1)]
    return LCS(x, y, n, m)


# bottom up
def LCSBottomUp(x, y):
    n = len(x)
    m = len(y)
    # Create a 2D DP table to store lengths of LCS
    t = [[0] * (m + 1) for _ in range(n + 1)]
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                # If characters match, add 1 to the previous diagonal value
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                # If characters don't match, take the maximum of left and top
                t[i][j] = max(t[i - 1][j], t[i][j - 1])
    # The value at t[n][m] contains the length of the LCS
    return t[n][m]


def main():
    x = "AGGTAB"
    y = "GXTXAYB"
    print("Length of LCS:", computeLCS(x, y))


if __name__ == "__main__":
    main()


'''
Let n/m be the two sequence lengths.
Time: O((n+1)*(m+1)): each prefix pair is a DP state with one character
comparison and at most two neighboring table lookups.
Space: O((n+1)*(m+1)) for the full 2D table; no row compression is used.
Memoized LCS also needs O(n+m) recursive stack; computeLCS resets t.
The iterative overload is exposed as LCSBottomUp.
'''
