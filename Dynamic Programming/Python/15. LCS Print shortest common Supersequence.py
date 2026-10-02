def printLCSupersequence(x, y, t):
    i = len(x)
    j = len(y)
    lcsuper = ""
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            lcsuper = x[i - 1] + lcsuper
            i -= 1
            j -= 1
        elif t[i - 1][j] > t[i][j - 1]:
            lcsuper = x[i - 1] + lcsuper
            i -= 1
        else:
            lcsuper = y[j - 1] + lcsuper
            j -= 1
    while i > 0:
        lcsuper = x[i - 1] + lcsuper
        i -= 1
    while j > 0:
        lcsuper = y[j - 1] + lcsuper
        j -= 1
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
