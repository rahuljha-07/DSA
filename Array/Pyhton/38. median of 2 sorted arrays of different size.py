def findMedian(a, b):
    # Both arrays must already be sorted.
    n1 = len(a)
    n2 = len(b)

    if n1 + n2 == 0:
        raise ValueError("Both arrays cannot be empty.")

    # Ensure a is the smaller array.
    if n1 > n2:
        return findMedian(b, a)

    low = 0
    high = n1
    total = (n1 + n2 + 1) // 2

    while low <= high:
        mid1 = (low + high) // 2
        mid2 = total - mid1

        # Handle partitions at the start or end of either array.
        leftA = float("-inf") if mid1 == 0 else a[mid1 - 1]
        leftB = float("-inf") if mid2 == 0 else b[mid2 - 1]
        rightA = float("inf") if mid1 == n1 else a[mid1]
        rightB = float("inf") if mid2 == n2 else b[mid2]

        # Correct partition: every left-side value <= every right-side value.
        if leftA <= rightB and leftB <= rightA:
            if (n1 + n2) % 2 == 1:
                return max(leftA, leftB)

            return (max(leftA, leftB) + min(rightA, rightB)) / 2.0

        elif leftA > rightB:
            high = mid1 - 1
        else:
            low = mid1 + 1

    return 0.0  # Unreachable for valid sorted inputs.


a = [1, 3, 8]
b = [7, 9, 10, 11]
print("Median:", findMedian(a, b))  # Median: 8


# TIME: O(log(min(n1, n2) + 1))
# Binary search halves the partition range in the smaller array.
# Each iteration performs O(1) work.
# If the smaller array is empty, the calculation takes O(1).
#
# EXTRA SPACE: O(1)
# Only a fixed number of variables are used.
# The recursive swap happens at most once; no arrays are copied.

'''
Time Complexity: O(log(min(n1, n2)))

Reason:
Binary search is done only on the smaller array. Each iteration halves the
partition search range and does constant work.

Space Complexity: O(1)

Reason:
Only partition indexes and boundary values are stored. The recursive swap
of array order happens at most once.
'''
