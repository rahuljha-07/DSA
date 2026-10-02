def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]

    # Python has no do-while loop.
    # while True + break ensures we move at least once before checking.
    while True:
        slow = nums[slow]        # Move one step.
        fast = nums[nums[fast]]  # Move two steps.

        if slow == fast:
            break

    # Reset one pointer to the starting point.
    fast = nums[0]

    # Move both one step at a time to find the cycle's entrance.
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow  # The cycle entrance is the duplicate number.


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]

    print("Duplicate number:", find_duplicate(nums))
    # Output: Duplicate number: 2


# HOW IT WORKS
# Treat each value as the index of the next position:
#   next position = nums[current position].
#
# For [1, 3, 4, 2, 2], starting at index 0:
#   0 -> 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> ...
#
# The repeated value creates a cycle whose entrance is the duplicate.
#
# Phase 1:
# slow moves one step and fast moves two steps.
# Once inside the cycle, fast catches slow.
# Their meeting point is not necessarily the cycle entrance.
#
# Phase 2:
# Reset fast to nums[0], then move both pointers one step at a time.
# Floyd's algorithm guarantees they meet at the cycle entrance.
#
# Why not start with "while slow != fast" in phase 1?
# Both pointers initially equal nums[0], so that loop would never run.
# We must move them BEFORE checking, just like C++ do-while.
#
# The input array is not modified.


# TIME COMPLEXITY: O(n)
# Time complexity describes how work grows with input size.
#
# Phase 1 takes O(n):
# slow reaches the cycle in at most O(n) steps.
# Inside it, fast gains one step per iteration and catches slow
# within at most one cycle length, also O(n).
#
# Phase 2 takes O(n):
# Both pointers reach the cycle entrance within O(n) steps.
#
# The phases run sequentially:
# O(n) + O(n) = O(n).
#
# The nested indexing nums[nums[fast]] is just two lookups: O(1).


# EXTRA SPACE COMPLEXITY: O(1)
# Only two pointer variables are used.
# No additional array, set, or recursion is needed.
# Extra memory stays constant as the input grows.

'''
Time Complexity: O(n)

Reason:
Floyd's cycle detection has two phases. The slow and fast pointers meet
inside the cycle in O(n), then move to the duplicate entrance in O(n).

Space Complexity: O(1)

Reason:
Only slow and fast pointers are used. The input array is not modified.
'''
