# Study note: use the LCS table but reset a cell to 0 on mismatched
# characters, because a substring cannot continue across a mismatch.
# No executable implementation was present in the C++ file.


'''
Let n/m be the two sequence lengths.
Time: O((n+1)*(m+1)): each prefix pair is a DP state with one character
comparison and at most two neighboring table lookups.
Space: O((n+1)*(m+1)) for the full 2D table; no row compression is used.
Bounds describe the suggested substring DP. The answer is the maximum
over all cells, not necessarily the bottom-right cell: a matching
substring can end before the ends of either string.
'''
