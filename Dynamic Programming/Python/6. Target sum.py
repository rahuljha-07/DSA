# Study note: split values into positively and negatively signed groups.
# If their magnitudes sum to S1 and S2, then S1-S2=k and S1+S2=total.
# This reduces to counting subsets with sum (total+k)/2.
# No executable implementation was present in the C++ file.


'''
Let n be the number of elements and S the target sum.
Time: O((n+1)*(S+1)): the table has (n+1)*(S+1) states and each state
uses at most two already-computed states in O(1) arithmetic work.
Space: O((n+1)*(S+1)) for the full 2D table; it is not compressed.
Assumes nonnegative array values and target. Arithmetic costs treat
stored counts/values as machine-sized; Python big integers can add cost.
Here S=(total+k)//2 for nonnegative original values. Reject targets
with |k|>total or odd total+k. Bounds describe the suggested DP;
the O(n) total-sum pass does not dominate table construction.
'''
