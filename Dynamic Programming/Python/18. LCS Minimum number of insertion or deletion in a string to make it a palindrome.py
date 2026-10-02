# Study note: minimum insertions alone and minimum deletions alone
# both equal len(s)-LCS(s, reverse(s)).
# No executable implementation was present in the C++ file.


'''
Let n be the string length.
Time: O((n+1)^2) to compute LCS against the reverse; subtracting that
length from n is O(1). Reversing the string adds O(n) work.
Space: O((n+1)^2) full LCS table plus O(n) reverse string.
Bounds describe the suggested approach, not an implemented function.
'''
