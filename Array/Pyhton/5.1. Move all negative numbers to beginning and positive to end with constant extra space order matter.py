def rearrange_array(arr):
    # Next position where a negative number should be placed.
    negative_index = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            # Save the negative number before shifting overwrites its position.
            temp = arr[i]

            # Shift the nonnegative elements before it one position right.
            # Move backward so we do not overwrite values still needed.
            for j in range(i, negative_index, -1):
                arr[j] = arr[j - 1]

            # Insert the negative number after the previous negatives.
            arr[negative_index] = temp
            negative_index += 1


if __name__ == "__main__":
    arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]

    rearrange_array(arr)
    print("Rearranged array (order preserved):", *arr)

    # Output:
    # Rearranged array (order preserved): -12 -13 -5 -7 -3 -6 11 6 5


# ---------------------------------------------------------------------------
# HOW IT WORKS: MOVE NEGATIVES FIRST WHILE PRESERVING ORDER
# ---------------------------------------------------------------------------
# We rearrange the original list so that:
# - Negative numbers come first, in their original relative order.
# - Nonnegative numbers (including 0) follow, in their original relative order.
#
# negative_index marks the next position for a negative number.
# When we find a negative number, we save it, shift the intervening
# nonnegative elements right, and insert it at negative_index.
#
# Example:
# [4, 2, -3, -1]
#
# Find -3:
#   Save -3, shift 2 and 4 right, then insert -3 at index 0.
#   Result: [-3, 4, 2, -1]
#
# Find -1:
#   Save -1, shift 2 and 4 right, then insert -1 at index 1.
#   Result: [-3, -1, 4, 2]
#
# Shifting instead of directly swapping preserves the order of both groups.
#
# range(i, negative_index, -1):
# - Starts at i.
# - Decreases by 1 each step.
# - Stops BEFORE negative_index.
# Example: range(4, 1, -1) produces 4, 3, 2.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY
# ---------------------------------------------------------------------------
# Time complexity describes how the work grows with input size n.
#
# The outer loop always runs n times.
# The inner loop performs i - negative_index shifts for each negative number.
# Its cost depends on how many nonnegative elements precede that negative.
#
# WORST CASE: O(n²)
# Consider half nonnegative numbers followed by half negative numbers:
#
#   [1, 2, 3, -1, -2, -3]
#
# Each of the 3 negative numbers requires shifting 3 nonnegative numbers.
# Total shifts = 3 × 3 = 9.
#
# In general:
#   (n/2) negatives × (n/2) shifts each = n²/4 shifts.
#
# Including the outer loop gives O(n + n²/4), which simplifies to O(n²).
# Big O ignores constant factors and lower-order terms.
#
# BEST CASE: O(n)
# If all negatives already precede all nonnegative elements,
# no shifting is necessary. Only the n outer-loop iterations remain.
#
# Unlike Quickselect's shrinking search portion, this algorithm can shift
# the same nonnegative elements repeatedly for different negative numbers.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(1)
# ---------------------------------------------------------------------------
# Extra space measures additional memory beyond the input list.
#
# Only a fixed number of variables are used: negative_index, i, j, and temp.
# We modify the original list without creating another list.
# Python's range also does not store a full list of indices.
#
# Therefore, extra memory remains constant: O(1).