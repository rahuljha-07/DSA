# Study note: rod cutting is the same unbounded-knapsack recurrence.
# Rename wt to length, val to price, and capacity W to rod length N.
# No executable implementation was present in the C++ file.


'''
Let n be piece types, N the rod length, and a the smallest positive piece.
Time: O((n+1)*(N+1)): each type/remaining-length DP state combines
including the same type again with excluding it, in O(1) work.
Space: O((n+1)*(N+1)) full table; memoized recursion would add
O(n+N/a) stack depth. Bounds describe the approach suggested by the note.
'''
