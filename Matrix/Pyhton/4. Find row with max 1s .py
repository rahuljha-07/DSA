def rowWithMax1s(arr):
    # Get number of rows
    n = len(arr)              # Number of rows
    # Get number of columns
    m = len(arr[0])           # Number of columns

    # Initialize to -1 to indicate no row found
    maxRowIndex = -1          # No row found initially

    # Start from the first row
    i = 0                     # Start from first row
    # Start from the last column
    j = m - 1                 # Start from last column

    # Traverse from the top-right corner
    while i < n and j >= 0:

        if arr[i][j] == 1:
            # Current row has a 1 at this position,
            # so it may have more 1s than previous rows
            maxRowIndex = i
            # Move left
            j -= 1            # Move left

        else:
            # Move down
            i += 1            # Move down

    # Return the row index with the maximum number of 1s found
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
