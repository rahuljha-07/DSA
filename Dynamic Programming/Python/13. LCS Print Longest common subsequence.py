# Function to print LCS by backtracking the DP table
def printLCS(x, y, t):
    # Length of string x
    i = len(x)
    # Length of string y
    j = len(y)
    # To store the LCS characters
    # Print the LCS
    lcs = ""
    # Backtrack from t[i][j] to t[0][0]
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            # If characters match, add it to the LCS and move diagonally
            lcs = x[i - 1] + lcs
            # If the value above is greater, move up
            i -= 1
            # Otherwise, move left
            j -= 1
        elif t[i - 1][j] > t[i][j - 1]:
            i -= 1
        else:
            j -= 1
    print("LCS:", lcs)


'''
Let n/m be string lengths and L the output LCS length.
Time: O(n+m+L^2) for this reconstruction: each step reduces i or j,
but prepending each matching character copies a growing immutable Python
string, totaling 1+2+...+L characters. Building the supplied LCS table
separately costs O(n*m) time.
Space: O(L) additional/output storage for lcs and temporary copies; the
already-built input table occupies O((n+1)*(m+1)) and is not allocated here.
'''
