# Study note: keep LCS(a,b); delete len(a)-LCS characters from a,
# then insert len(b)-LCS characters to form b. Add these two counts.
# Example: heap -> pea keeps ea, deletes 2 characters, and inserts 1.
# No executable implementation was present in the C++ file.


'''
Let n/m be the two sequence lengths.
Time: O((n+1)*(m+1)): each prefix pair is a DP state with one character
comparison and at most two neighboring table lookups.
Space: O((n+1)*(m+1)) for the full 2D table; no row compression is used.
Bounds describe computing the suggested LCS. The deletion/insertion
counts are then calculated in O(1) additional time and space.
'''
