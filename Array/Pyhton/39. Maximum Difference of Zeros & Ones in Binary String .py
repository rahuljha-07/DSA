'''
Replace 1 with -1.
Replace 0 with +1.
Then apply Kadane's algorithm to find the maximum subarray sum.
This gives the maximum difference: number of 0s - number of 1s.

Example: 1100001
Modified array: [-1, -1, 1, 1, 1, 1, -1]

Kadane returns 4, not 2, for the subarray "0000".
Maximum difference = 4 - 0 = 4.

Time Complexity: O(n)

Reason:
The binary string is scanned once to convert characters conceptually
and apply Kadane's running maximum logic. Each character contributes
constant work.

Space Complexity: O(1)

Reason:
Kadane's algorithm only needs current sum and best sum variables.
No extra array is required if conversion is handled while scanning.
'''
