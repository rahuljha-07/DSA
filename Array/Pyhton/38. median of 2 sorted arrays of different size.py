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
    # Total elements in the left partition
    total = (n1 + n2 + 1) // 2

    while low <= high:
        # Partition index for `a`
        mid1 = (low + high) // 2
        # Partition index for `b` (remaining elements)
        mid2 = total - mid1

        # Handle partitions at the start or end of either array.
        leftA = float("-inf") if mid1 == 0 else a[mid1 - 1]
        # Last element in left half of `b`
        leftB = float("-inf") if mid2 == 0 else b[mid2 - 1]
        # First element in right half of `a`
        rightA = float("inf") if mid1 == n1 else a[mid1]
        # First element in right half of `b`
        rightB = float("inf") if mid2 == n2 else b[mid2]

        # Correct partition: every left-side value <= every right-side value.
        if leftA <= rightB and leftB <= rightA:
            # If total size is odd, median is the max of the left partition
            if (n1 + n2) % 2 == 1:
                return max(leftA, leftB)

            # If total size is even, median is the average of max left and min right
            return (max(leftA, leftB) + min(rightA, rightB)) / 2.0

        # If leftA is greater, move left in `a`
        elif leftA > rightB:
            high = mid1 - 1
        # If leftB is greater, move right in `a`
        else:
            low = mid1 + 1

    # Should never reach here
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
