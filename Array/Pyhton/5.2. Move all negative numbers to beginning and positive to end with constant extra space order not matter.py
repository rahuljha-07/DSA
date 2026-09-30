def rearrange_array(arr):
    # Next position where a negative number should be placed.
    negative_index = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            # Move this negative number into the negative section.
            # The displaced nonnegative number moves to index i.
            arr[i], arr[negative_index] = arr[negative_index], arr[i]
            negative_index += 1


if __name__ == "__main__":
    arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]

    rearrange_array(arr)
    print("Rearranged array:", *arr)

    # Output:
    # Rearranged array: -12 -13 -5 -7 -3 -6 5 6 11


# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
# Task: Move negatives first and nonnegative numbers afterward.
# Constant extra space is required; preserving order is NOT required.
# Zero, if present, belongs to the nonnegative group.
#
# negative_index marks the boundary between:
# - Negative numbers already placed on the left.
# - Nonnegative numbers in the inspected portion.
#
# Whenever we find a negative number, swap it into negative_index,
# then advance negative_index.
#
# Example:
# [4, -2, 3, -1]
#
# Find -2: swap with 4 -> [-2, 4, 3, -1]
# Find -1: swap with 4 -> [-2, -1, 3, 4]
#
# Notice that the nonnegative order changed from [4, 3] to [3, 4].
# This is allowed because order does not matter for this task.
#
# Unlike the order-preserving version, we swap instead of shifting.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n)
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with the number of elements n.
#
# - The for loop visits each of the n elements exactly once.
# - Each iteration performs one comparison.
# - For a negative number, it also performs one swap and one index update.
# - Each of these operations takes constant time, O(1).
#
# Total work = n × O(1) = O(n).
#
# Best, average, and worst-case time are all O(n).
# Even if no swaps are needed, every element must still be checked.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(1)
# ---------------------------------------------------------------------------
# Extra space measures additional memory beyond the input list.
#
# We use only a fixed number of variables and modify the list directly.
# Swapping uses constant temporary storage, and range does not create
# a full list of indices.
#
# Extra memory does not grow with n, so it is O(1).