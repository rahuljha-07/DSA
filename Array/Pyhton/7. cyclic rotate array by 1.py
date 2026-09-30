def rotate(arr):
    # An empty list or a single-element list needs no rotation.
    n = len(arr)
    if n <= 1:
        return

    # Save the last element before shifting overwrites it.
    last = arr[n - 1]

    # Shift each remaining element one position to the right.
    # Move backward to avoid overwriting values we still need.
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    # Move the original last element to the beginning.
    arr[0] = last


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]

    rotate(arr)
    print("Rotated array:", *arr)

    # Output: Rotated array: 5 1 2 3 4


# ---------------------------------------------------------------------------
# HOW IT WORKS: ROTATE RIGHT BY ONE POSITION
# ---------------------------------------------------------------------------
# The last element moves to the beginning.
# Every other element moves one position to the right.
#
# Initial:       [1, 2, 3, 4, 5]
# Save last = 5
#
# i = 4:         [1, 2, 3, 4, 4]
# i = 3:         [1, 2, 3, 3, 4]
# i = 2:         [1, 2, 2, 3, 4]
# i = 1:         [1, 1, 2, 3, 4]
# arr[0] = last: [5, 1, 2, 3, 4]
#
# range(n - 1, 0, -1) starts at n - 1 and decreases by 1,
# stopping BEFORE 0. For n = 5, it produces 4, 3, 2, 1.
#
# Why move backward?
# Moving forward would overwrite the next element before we could
# copy its original value. Moving backward keeps those values available.
#
# The original list is modified directly.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n)
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with the number of elements n.
#
# - Saving the last element takes O(1).
# - The loop performs n - 1 assignments, each taking O(1).
# - Placing the saved element at index 0 takes O(1).
#
# Total work grows linearly with n:
# O(1) + O(n - 1) + O(1) = O(n).
#
# For n >= 2, best, average, and worst-case time are all O(n),
# because the same number of shifts occurs regardless of the values.
# Empty and single-element lists return in O(1) time.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(1)
# ---------------------------------------------------------------------------
# Extra space measures additional memory beyond the input list.
#
# We use only a fixed number of variables: n, last, and i.
# No additional list is created; range generates indices as needed.
#
# Extra memory does not grow with n, so it is O(1).