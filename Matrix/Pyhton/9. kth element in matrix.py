from bisect import bisect_right
import heapq


# =========================================================
# 1. BINARY SEARCH APPROACH
# Same idea as median in a sorted matrix
# Replace desired_element with k
# =========================================================

def kthSmallest(A, n, k):
    # Your code here
    m = n

    mini = A[0][0]
    maxi = A[n - 1][m - 1]

    desired_element = k

    while mini < maxi:

        mid = mini + (maxi - mini) // 2

        count = 0

        # Count elements <= mid in each row
        for i in range(n):
            count += bisect_right(A[i], mid)

        if count < desired_element:
            mini = mid + 1

        else:
            maxi = mid

    return mini


'''
Time Complexity:
O(n * log(n) * log(maxi - mini))

Reason:

We perform binary search on the value range
from mini to maxi.

For every mid value, we go through all n rows.

For each row, bisect_right performs binary search
in O(log(n)) time.

Therefore:

O(n * log(n) * log(maxi - mini))


Space Complexity:
O(1)

Reason:

We only use variables like mini, maxi, mid,
count, and desired_element.

No extra data structure is used.
'''



# =========================================================
# 2. MIN-HEAP APPROACH
# =========================================================

def kthsmallest(mat, N, K):

    # Min-heap storing:
    # (value, row, col)
    minHeap = []

    # Push first element of each row
    for i in range(N):
        heapq.heappush(
            minHeap,
            (mat[i][0], i, 0)
        )

    count = 0
    result = -1

    while minHeap:

        # Extract smallest element
        val, row, col = heapq.heappop(minHeap)

        result = val
        count += 1

        # Stop when K-th smallest element is found
        if count == K:
            break

        # Push next element from the same row
        if col + 1 < N:
            heapq.heappush(
                minHeap,
                (mat[row][col + 1], row, col + 1)
            )

    return result


'''
Time Complexity:
O(K * log(N))

Reason:

Initially, we insert the first element of each row
into the heap.

The heap contains at most N elements.

We remove elements from the heap until we reach
the K-th smallest element.

For each extracted element, we may insert the next
element from the same row.

Each heap push/pop operation takes O(log(N)).

We perform this K times.

Therefore:

O(K * log(N))


Space Complexity:
O(N)

Reason:

The min-heap stores at most one element
from each row at a time.

Therefore:

O(N)
'''
