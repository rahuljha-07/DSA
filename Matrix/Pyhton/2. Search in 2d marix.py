def searchMatrix(matrix, target):
    m = len(matrix)          # Number of rows in the matrix
    n = len(matrix[0])       # Number of columns in the matrix

    low = 0
    high = m * n - 1         # Search range for the virtual 1D array

    # Binary search on the virtual 1D array
    while low <= high:
        mid = (low + high) // 2

        row = mid // n       # Row index in the 2D matrix
        col = mid % n        # Column index in the 2D matrix

        if matrix[row][col] == target:
            return True

        elif matrix[row][col] < target:
            low = mid + 1

        else:
            high = mid - 1

    return False


'''
Time Complexity:
O(log(rows * cols))

Reason:
We perform binary search over all rows * cols elements.
At every step, the search space is reduced by half.


Space Complexity:
O(1)

Reason:
We only use a few variables such as low, high, mid, row, and col.
No extra data structure is used.
'''

def searchMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    # Start from the top-right corner
    row = 0
    col = cols - 1

    while row < rows and col >= 0:

        if matrix[row][col] == target:
            return True

        elif matrix[row][col] > target:
            col -= 1         # Move left

        else:
            row += 1         # Move down

    return False


'''
Time Complexity:
O(rows + cols)

Reason:
We start from the top-right corner.

At every step, we either:
1. Move one column left, or
2. Move one row down.

So we can move at most rows times downward
and cols times toward the left.

Therefore, the time complexity is O(rows + cols).


Space Complexity:
O(1)

Reason:
We only use variables rows, cols, row, and col.
No extra data structure is used.
'''