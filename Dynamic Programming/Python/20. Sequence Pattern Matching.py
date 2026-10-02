# Study note: a is a subsequence of b exactly when LCS(a,b)==len(a).
# Example: axy is present in adxcpy in order, with gaps allowed.
# No executable implementation was present in the C++ file.


'''
Let n/m be the two sequence lengths.
Time: O((n+1)*(m+1)): each prefix pair is a DP state with one character
comparison and at most two neighboring table lookups.
Space: O((n+1)*(m+1)) for the full 2D table; no row compression is used.
Bounds describe the LCS approach specified in the note; comparing
the result with len(a) is O(1). No two-pointer replacement is introduced.
'''
