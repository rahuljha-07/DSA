'''
Replace 1 with -1.
Replace 0 with +1.
Then apply Kadane's algorithm to find the maximum subarray sum.
This gives the maximum difference: number of 0s - number of 1s.

Example: 1100001
Modified array: [-1, -1, 1, 1, 1, 1, -1]

Kadane returns 4, not 2, for the subarray "0000".
Maximum difference = 4 - 0 = 4.
'''