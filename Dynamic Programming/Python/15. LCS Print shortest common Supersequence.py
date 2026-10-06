# Function to print the Longest Common Supersequence (LCSupersequence)
def printLCSupersequence(x, y, t):
    # Length of string x
    i = len(x)
    # Length of string y
    j = len(y)
    # To store the LCSupersequence characters
    lcsuper = ""
    # Backtrack from t[i][j] to t[0][0]
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            # If characters match, include it in the supersequence
            lcsuper = x[i - 1] + lcsuper
            i -= 1
            j -= 1
        elif t[i - 1][j] > t[i][j - 1]:
            # If the value above is greater, include the character from x
            lcsuper = x[i - 1] + lcsuper
            i -= 1
        else:
            # Otherwise, include the character from y
            lcsuper = y[j - 1] + lcsuper
            j -= 1
    # If one string is exhausted, append the remaining characters of the other string
    while i > 0:
        lcsuper = x[i - 1] + lcsuper
        i -= 1
    while j > 0:
        lcsuper = y[j - 1] + lcsuper
        j -= 1
    # Print the LCSupersequence
    print("Longest Common Supersequence:", lcsuper)


'''
Let n/m be input lengths and L=n+m-LCS(x,y) the supersequence length.
Time: O(n+m+L^2): at most n+m reconstruction steps, but repeated front
concatenation copies prefixes of lengths 1 through L. Computing the
supplied table separately costs O(n*m).
Space: O(L) additional/output string storage, excluding the supplied
O((n+1)*(m+1)) table. Despite the source's printed label, this builds a
SHORTEST common supersequence; the output label is retained.
'''
