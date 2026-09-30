def merge(arr, left, mid, right):
    inversions = 0

    # Python slices exclude the ending index.
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    # Merge the sorted halves and count inversions between them.
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            # Equal values do not form an inversion.
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]

            # All remaining left-side values are greater than right_part[j].
            inversions += len(left_part) - i
            j += 1

        k += 1

    # Copy any remaining elements from the left half.
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right half.
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

    return inversions


def merge_sort(arr, left, right):
    inversions = 0

    if left < right:
        mid = left + (right - left) // 2

        # Count inversions within each half, then between the halves.
        inversions += merge_sort(arr, left, mid)
        inversions += merge_sort(arr, mid + 1, right)
        inversions += merge(arr, left, mid, right)

    return inversions


if __name__ == "__main__":
    arr = [3, 1, 2, 5, 4]

    inversions = merge_sort(arr, 0, len(arr) - 1)

    print("Sorted array:", *arr)
    print("Number of inversions:", inversions)

    # Output:
    # Sorted array: 1 2 3 4 5
    # Number of inversions: 3


# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
# An inversion means a larger element appears before a smaller element.
#
# For [3, 1, 2, 5, 4], the inversion value pairs are:
# (3, 1), (3, 2), and (5, 4).
# Answer: 3.
#
# Merge sort counts three groups:
# 1. Inversions entirely within the left half.
# 2. Inversions entirely within the right half.
# 3. Inversions crossing from the left half to the right half.
#
# Why add len(left_part) - i?
#
# Suppose the sorted halves are:
# left_part  = [3, 5, 7]
# right_part = [2, 6]
#
# When comparing 3 and 2, we know:
# - 3 > 2.
# - Since the left half is sorted, 5 and 7 are also > 2.
# - All these left-half elements originally precede this right-half element.
#
# Therefore, 2 forms THREE inversions: (3, 2), (5, 2), (7, 2).
# We count them together instead of checking each one separately.
#
# This function also sorts the original array.
# Empty and single-element arrays return 0 inversions.
# Python's int handles large counts without a separate long long type.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n log n)
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with input size n.
#
# Each recursive call splits its portion roughly in half.
# This creates O(log n) levels.
#
# Unlike Quickselect, merge sort processes BOTH halves.
# At each merging level, the total work across all portions is O(n):
#
# One merge of size n:          n work.
# Two merges of size n/2:       2 × n/2 = n work.
# Four merges of size n/4:      4 × n/4 = n work.
#
# Slicing and merging each portion both take linear time in its size.
#
# Total: O(n) work per level × O(log n) levels = O(n log n).
# Best, average, and worst-case time are all O(n log n).


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(n)
# ---------------------------------------------------------------------------
# Space complexity measures additional memory beyond the input array.
#
# Temporary lists during a merge: O(n) at the largest merge.
# Recursive call stack: O(log n).
#
# Total peak extra space: O(n) + O(log n) = O(n).
#
# We do NOT multiply temporary space by the number of recursion levels:
# child merges finish and release their temporary lists before the
# parent merge creates its own lists.