t = []


# Function to compute LCS of three strings using Memoization (Top-Down)
def LCS3_TopDown(x, y, z, n, m, o):
    # Base case: If any string is empty, LCS is 0
    if n == 0 or m == 0 or o == 0:
        return 0
    # If the value is already computed, return it
    if t[n][m][o] != -1:
        return t[n][m][o]
    # If the last characters of all three strings match
    if x[n - 1] == y[m - 1] == z[o - 1]:
        t[n][m][o] = 1 + LCS3_TopDown(x, y, z, n - 1, m - 1, o - 1)
    else:
        # Otherwise, consider all possible cases and take the maximum
        t[n][m][o] = max(
            LCS3_TopDown(x, y, z, n - 1, m, o),
            LCS3_TopDown(x, y, z, n, m - 1, o),
            LCS3_TopDown(x, y, z, n, m, o - 1),
        )
    return t[n][m][o]


# Helper function to initialize memoization table and compute LCS of three strings
def computeLCS3_TopDown(x, y, z):
    n = len(x)
    m = len(y)
    o = len(z)
    # Resize and initialize the memoization table with -1
    t[:] = [[[-1] * (o + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    return LCS3_TopDown(x, y, z, n, m, o)


# Function to compute LCS of three strings using Tabulation (Bottom-Up)
def LCS3_BottomUp(x, y, z):
    n = len(x)
    m = len(y)
    o = len(z)
    # Create a 3D DP table
    dp = [[[0] * (o + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, o + 1):
                if x[i - 1] == y[j - 1] == z[k - 1]:
                    # If characters of all three strings match
                    dp[i][j][k] = 1 + dp[i - 1][j - 1][k - 1]
                else:
                    # Otherwise, take the maximum
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    # The value at dp[n][m][o] contains the length of the LCS of three strings
    return dp[n][m][o]


def main():
    s1 = "geeks"
    s2 = "geeksfor"
    s3 = "geeksforgeeks"
    print("Length of LCS of three strings (Top-Down):", computeLCS3_TopDown(s1, s2, s3))
    print("Length of LCS of three strings (Bottom-Up):", LCS3_BottomUp(s1, s2, s3))


if __name__ == "__main__":
    main()


'''
Let n/m/o be the three string lengths.
Time: O((n+1)*(m+1)*(o+1)) for either method: each prefix triple is a
state with constant character comparisons and at most three transitions.
Space: O((n+1)*(m+1)*(o+1)) full 3D table; top-down adds O(n+m+o)
stack depth. computeLCS3_TopDown resets global t on every call.
'''
