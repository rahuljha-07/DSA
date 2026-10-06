t = []


def LRS(x):
    n = len(x)
    # Copy x into y
    y = x
    t[:] = [[0] * (n + 1) for _ in range(n + 1)]
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1] and i != j:
                # If characters match and indices are different
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                # If characters don't match, take the maximum of left and top
                t[i][j] = max(t[i - 1][j], t[i][j - 1])
    # The value at t[n][n] contains the length of the LRS
    return t[n][n]


'''
Let n be the string length.
Time: O((n+1)^2): compare all n*n position pairs, allowing matches only
at different indices so a character cannot match itself.
Space: O((n+1)^2) global DP table; y references the same immutable
string, so it does not copy n characters. LRS resets t on each call.
'''
