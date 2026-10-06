def spirallyTraverse(matrix, rows, cols):
    result = []

    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1

    # 0: left-to-right
    # 1: top-to-bottom
    # 2: right-to-left
    # 3: bottom-to-top
    dir = 0

    while top <= bottom and left <= right:

        # Traverse left to right
        if dir == 0:  # Traverse left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

        # Traverse top to bottom
        elif dir == 1:  # Traverse top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

        # Traverse right to left
        elif dir == 2:  # Traverse right to left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse bottom to top
        elif dir == 3:  # Traverse bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        # Change direction cyclically
        dir = (dir + 1) % 4

    return result


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

spiralOrder = spirallyTraverse(matrix, rows, cols)

print("Spiral Order Traversal:", end=" ")

for num in spiralOrder:
    print(num, end=" ")

print()


'''
Time Complexity:
O(rows * cols)

Reason:
Every element of the matrix is visited exactly once.
If there are rows * cols elements, the total time taken is O(rows * cols).


Space Complexity:
O(rows * cols)

Reason:
The result list stores all the elements of the matrix.

If we ignore the output/result list, the auxiliary space complexity is O(1),
because we only use variables like top, bottom, left, right, dir, and i.
'''
