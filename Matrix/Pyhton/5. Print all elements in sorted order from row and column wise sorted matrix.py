import heapq


# =========================================================
# 1. USING TUPLE
# =========================================================

def printSortedMatrix_tuple(matrix):
    n = len(matrix)

    if n == 0:
        return

    m = len(matrix[0])

    # Min-heap
    minHeap = []

    # Push the first element of each row
    for i in range(n):
        heapq.heappush(minHeap, (matrix[i][0], i, 0))
        # (value, row, col)

    # Process the heap
    while minHeap:

        current = heapq.heappop(minHeap)

        # Print smallest element
        print(current[0], end=" ")

        # Push next element from the same row
        if current[2] + 1 < m:
            heapq.heappush(
                minHeap,
                (
                    matrix[current[1]][current[2] + 1],
                    current[1],
                    current[2] + 1
                )
            )


'''
Time Complexity:
O(n * m * log(n))

Reason:
There are n * m elements in the matrix.

The heap contains at most n elements because we keep
one element from each row at a time.

For every matrix element, we perform heap push/pop operations.

Each heap operation takes O(log(n)).

Therefore:
O(n * m * log(n))


Space Complexity:
O(n)

Reason:
The heap stores at most one element from each row.

Therefore:
O(n)
'''



# =========================================================
# 2. USING PAIR-STYLE NESTED TUPLE
# =========================================================

def printSortedMatrix_pair(matrix):
    n = len(matrix)

    if n == 0:
        return

    m = len(matrix[0])

    # Min-heap
    minHeap = []

    # Push the first element of each row
    for i in range(n):
        if m > 0:
            heapq.heappush(
                minHeap,
                (matrix[i][0], (i, 0))
            )
            # (value, (row, col))

    # Process the heap
    while minHeap:

        current = heapq.heappop(minHeap)

        # Print smallest element
        print(current[0], end=" ")

        row = current[1][0]
        col = current[1][1]

        # Push next element from the same row
        if col + 1 < m:
            heapq.heappush(
                minHeap,
                (
                    matrix[row][col + 1],
                    (row, col + 1)
                )
            )


'''
Time Complexity:
O(n * m * log(n))

Reason:
There are n * m total elements.

For every element, heap push/pop operations are performed.

The heap contains at most n elements.

Each heap operation takes O(log(n)).

Therefore:
O(n * m * log(n))


Space Complexity:
O(n)

Reason:
The heap stores at most n elements.

Therefore:
O(n)
'''



# =========================================================
# 3. USING CUSTOM STRUCTURE / CLASS
# =========================================================

class Element:

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col

    # Comparison for min-heap
    def __lt__(self, other):
        return self.value < other.value


def printSortedMatrix_structure(matrix):
    # Get the number of rows and columns
    n = len(matrix)

    if n == 0:
        return

    m = len(matrix[0])

    # Min-heap
    minHeap = []

    # Push the first element of each row
    for i in range(n):
        if m > 0:
            heapq.heappush(
                minHeap,
                Element(matrix[i][0], i, 0)
            )

    # Process the heap
    while minHeap:

        current = heapq.heappop(minHeap)

        # Print smallest element
        print(current.value, end=" ")

        # Push next element from the same row
        if current.col + 1 < m:
            heapq.heappush(
                minHeap,
                Element(
                    matrix[current.row][current.col + 1],
                    current.row,
                    current.col + 1
                )
            )


'''
Time Complexity:
O(n * m * log(n))

Reason:
There are n * m elements in the matrix.

Each element is pushed into and removed from the heap.

The heap contains at most n elements.

Each heap operation takes O(log(n)).

Therefore:
O(n * m * log(n))


Space Complexity:
O(n)

Reason:
The heap stores at most n Element objects.

Therefore:
O(n)
'''



# =========================================================
# EXAMPLE
# =========================================================

matrix = [
    [10, 20, 30],
    [5, 15, 25],
    [1, 2, 3]
]

print("Using Tuple:")
printSortedMatrix_tuple(matrix)

print("\n\nUsing Pair:")
printSortedMatrix_pair(matrix)

print("\n\nUsing Custom Structure:")
printSortedMatrix_structure(matrix)
