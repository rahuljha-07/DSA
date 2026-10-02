# Study note: the shortest common supersequence contains each shared
# LCS character once instead of twice, so its length is n+m-LCS(x,y).
# Example: abcd and def can share d.
# No executable implementation was present in the C++ file.


'''
Let n/m be the two sequence lengths.
Time: O((n+1)*(m+1)): each prefix pair is a DP state with one character
comparison and at most two neighboring table lookups.
Space: O((n+1)*(m+1)) for the full 2D table; no row compression is used.
Bounds describe computing the LCS suggested by the note; subtracting
its length from n+m takes O(1) additional time and space.
'''
