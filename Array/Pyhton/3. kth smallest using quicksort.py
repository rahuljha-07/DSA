def partition(arr, low, high):
    # Choose the middle element as the pivot.
    pivot_index = (low + high) // 2
    pivot = arr[pivot_index]

    # Move the pivot to the end while arranging the other elements.
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    left = low
    right = high - 1

    while True:
        # Find an element on the left that is >= pivot.
        while left <= right and arr[left] < pivot:
            left += 1

        # Find an element on the right that is <= pivot.
        while left <= right and arr[right] > pivot:
            right -= 1

        if left < right:
            # Swap these elements to put them on the correct sides.
            arr[left], arr[right] = arr[right], arr[left]
            # Advance even when both swapped values equal the pivot.
            left += 1
            right -= 1
        else:
            # Pointers have met or crossed. Put the pivot in its final position.
            # Values on its left are <= pivot; values on its right are >= pivot.
            arr[left], arr[high] = arr[high], arr[left]
            return left


def kth_smallest(arr, k):
    # k is 1-based: k=1 means the smallest element.
    # Duplicates count separately: [2, 2, 5] has 2 as its second smallest.
    if k < 1 or k > len(arr):
        return -1

    arr = list(arr)
    low = 0
    high = len(arr) - 1
    target = k - 1  # Convert the rank to a 0-based index.

    while low <= high:
        pivot_index = partition(arr, low, high)

        if pivot_index == target:
            return arr[pivot_index]
        elif pivot_index > target:
            # Search only the portion to the left of the pivot.
            high = pivot_index - 1
        else:
            # Search only the portion to the right of the pivot.
            low = pivot_index + 1

    return -1


if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 3

    # This function partitions a copy, leaving the original list unchanged.
    result = kth_smallest(arr, k)
    print(f"Smallest element at rank {k}: {result}")

    # Output: Smallest element at rank 3: 7


# ---------------------------------------------------------------------------
# HOW THE ALGORITHM WORKS: QUICKSELECT
# ---------------------------------------------------------------------------
# 1. Pick a pivot and partition the current portion of the list around it.
# 2. The pivot is now at an index it could occupy in the fully sorted list.
# 3. If that index equals k - 1, we have found the answer.
# 4. Otherwise, search only the side containing index k - 1.
#
# Unlike Quicksort, Quickselect does not sort both sides.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY
# ---------------------------------------------------------------------------
# Time complexity describes how the amount of work grows with input size.
# Let n be the number of elements in the list.
# Big O describes the growth rate, ignoring constant factors and smaller terms.
#
# ONE PARTITION CALL: O(m), where m is the current portion's size.
# - The left pointer moves forward; the right pointer moves backward.
# - Together, they scan the current portion once.
# - Each comparison and swap takes O(1), meaning constant time.
# - Nested loops do not make this O(m²), because the pointers never restart.
#
# AVERAGE TOTAL TIME: O(n)
# - We keep searching only one side after each partition.
# - For balanced partitions, the work looks like:
#
#       n + n/2 + n/4 + n/8 + ... < 2n
#
# - Ignoring the constant factor 2 gives O(n).
# - This illustrates the linear average behavior; individual splits can vary.
#
# WORST-CASE TOTAL TIME: O(n²)
# - A poor pivot may eliminate only one element per partition.
# - If this keeps happening, the work is:
#
#       n + (n - 1) + (n - 2) + ... + 1 = n(n + 1)/2
#
# - The dominant term is n², so the complexity is O(n²).
# - Choosing the middle INDEX does not guarantee the middle VALUE.


# ---------------------------------------------------------------------------
# SPACE COMPLEXITY
# ---------------------------------------------------------------------------
# Space complexity describes how memory usage grows with input size.
# Here we measure EXTRA memory, excluding the existing input list.
#
# EXTRA SPACE: O(n)
# - We copy the input list to preserve C++'s pass-by-value behavior.
# - We use a fixed number of variables regardless of input size.
# - The algorithm is iterative, so there is no recursive call stack.
#
# SUMMARY:
# Average time: O(n)
# Worst time:   O(n²)
# Extra space:  O(n)


'''
Time Complexity: O(n) average case, O(n^2) worst case

Reason:
Each partition scans the current range once. On average, the pivot removes
a good portion of the array, so the total work is n + n/2 + n/4 ... = O(n).
If the pivot keeps removing only one element, partitioning costs become
n + (n - 1) + ... + 1 = O(n^2).

Space Complexity: O(n)

Reason:
Copying the input takes O(n) space. Partitioning that copy is iterative and
uses only O(1) additional variables; there is no recursive call stack.
'''
