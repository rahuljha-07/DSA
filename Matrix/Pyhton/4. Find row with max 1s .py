def rowWithMax1s(arr):
    n = len(arr)              # Number of rows
    m = len(arr[0])           # Number of columns

    maxRowIndex = -1          # No row found initially

    i = 0                     # Start from first row
    j = m - 1                 # Start from last column

    # Traverse from the top-right corner
    while i < n and j >= 0:

        if arr[i][j] == 1:
            # Current row has a 1 at this position,
            # so it may have more 1s than previous rows
            maxRowIndex = i
            j -= 1            # Move left

        else:
            i += 1            # Move down

    return maxRowIndex


'''
Time Complexity:
O(n + m)

Reason:
We start from the top-right corner.

At every step, we either:
1. Move left by decreasing j, or
2. Move down by increasing i.

We can move left at most m times
and move down at most n times.

Therefore, total time complexity is:
O(n + m)


Space Complexity:
O(1)

Reason:
We only use variables n, m, i, j, and maxRowIndex.

No extra data structure is used.
'''