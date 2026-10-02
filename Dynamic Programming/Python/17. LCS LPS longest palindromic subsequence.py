# Study note: LPS(s) is LCS(s, reverse(s)).
# No executable implementation was present in the C++ file.


'''
Let n be the string length.
Time: O((n+1)^2): reverse in O(n), then fill a two-string LCS table
with n*n character comparisons and constant work per state.
Space: O((n+1)^2) table plus O(n) reversed string.
Bounds describe the LCS-based approach suggested by the note.
'''
