def sort012(arr):
    # Assumption: arr contains only 0, 1, and 2.
    low = 0
    mid = 0
    high = len(arr) - 1

    # We maintain four regions:
    # arr[:low]          -> all 0s
    # arr[low:mid]       -> all 1s
    # arr[mid:high + 1]  -> unknown elements still to inspect
    # arr[high + 1:]     -> all 2s
    # These slices describe the regions; we do not create them.

    while mid <= high:
        if arr[mid] == 0:
            # Move 0 into the left region.
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

            # Advancing mid is safe:
            # If low and mid were different, the swapped-in value was 1.
            # If they were equal, we simply swapped the element with itself.

        elif arr[mid] == 1:
            # The 1 already belongs in the middle region.
            mid += 1

        elif arr[mid] == 2:
            # Move 2 into the right region.
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

            # Do NOT advance mid here!
            # The element brought from high has not been checked yet.
            # It could be 0, 1, or 2, so inspect it next.

        else:
            raise ValueError("The list must contain only 0, 1, and 2.")


if __name__ == "__main__":
    arr = [0, 2, 1, 2, 0, 1, 0]

    sort012(arr)
    print(arr)

    # Output: [0, 0, 0, 1, 1, 2, 2]


# ---------------------------------------------------------------------------
# HOW IT WORKS: DUTCH NATIONAL FLAG ALGORITHM
# ---------------------------------------------------------------------------
# low  -> next position for a 0
# mid  -> current element being inspected
# high -> next position for a 2
#
# Inspect arr[mid]:
# - 0: swap with low, then advance low and mid.
# - 1: advance mid.
# - 2: swap with high, then decrease high without advancing mid.
#
# Stop when mid > high: no unknown elements remain.
# The original list is sorted directly.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n)
# ---------------------------------------------------------------------------
# Time complexity describes how the work grows with the input size n.
#
# The unknown region initially contains n elements.
# Every iteration reduces its size by exactly 1:
# - For 0 or 1, mid increases by 1.
# - For 2, high decreases by 1.
#
# Therefore, for valid input, there are exactly n iterations.
# Each iteration performs a constant amount of work: comparisons,
# at most one swap, and pointer updates.
#
# Total work = n × O(1) = O(n).
#
# Even when mid stays in place after finding a 2, high decreases,
# so the algorithm still makes progress.
#
# Best, average, and worst-case time are all O(n).


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(1)
# ---------------------------------------------------------------------------
# Extra space describes additional memory beyond the input list.
#
# We use only three index variables and swap elements in the existing list.
# No additional list or recursive calls are needed.
#
# The extra memory does not grow with n, so it is O(1).