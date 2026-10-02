# Study note: use the subset-sum DP, replacing OR with addition and
# True/False with 1/0. Include and exclude counts are added, not maximized.
# No executable implementation was present in the C++ file.


'''
Let n be the number of elements and S the target sum.
Time: O((n+1)*(S+1)): the table has (n+1)*(S+1) states and each state
uses at most two already-computed states in O(1) arithmetic work.
Space: O((n+1)*(S+1)) for the full 2D table; it is not compressed.
Assumes nonnegative array values and target. Arithmetic costs treat
stored counts/values as machine-sized; Python big integers can add cost.
These bounds describe the suggested subset-count DP, not executable code.
If zeros are allowed, count them even at target 0; n=0 has one empty subset.
'''
