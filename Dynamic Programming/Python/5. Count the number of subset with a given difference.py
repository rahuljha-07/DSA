# Study note: S2-S1=DIFF and S2+S1=RANGE, so S2=(RANGE+DIFF)/2.
# Count subsets with that target using the subset-count DP.
# No executable implementation was present in the C++ file.


'''
Let n be the number of elements and S the target sum.
Time: O((n+1)*(S+1)): the table has (n+1)*(S+1) states and each state
uses at most two already-computed states in O(1) arithmetic work.
Space: O((n+1)*(S+1)) for the full 2D table; it is not compressed.
Assumes nonnegative array values and target. Arithmetic costs treat
stored counts/values as machine-sized; Python big integers can add cost.
Here S=(total+DIFF)//2. The reduction requires nonnegative array values,
an even total+DIFF, and |DIFF|<=total; invalid targets have zero solutions.
Bounds describe the suggested DP. Summing the array adds O(n) work.
'''
