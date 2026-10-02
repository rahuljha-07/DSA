def next_permutation(nums):
    n = len(nums)
    k = -1

    # Step 1: Find the rightmost position where nums[i] < nums[i + 1].
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            k = i
            break

    # Step 2: No such position means the array is non-increasing.
    # Reverse it to get the smallest permutation.
    if k == -1:
        nums.reverse()
        return

    # Step 3: Find the rightmost element greater than nums[k].
    for l in range(n - 1, k, -1):
        if nums[l] > nums[k]:
            break

    # Step 4: Replace the pivot with the next suitable larger value.
    nums[k], nums[l] = nums[l], nums[k]

    # Step 5: Reverse the suffix to make it as small as possible.
    left = k + 1
    right = n - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    nums = [1, 2, 3]
    next_permutation(nums)
    print(nums)  # [1, 3, 2]

    nums = [3, 2, 1]
    next_permutation(nums)
    print(nums)  # [1, 2, 3]

    nums = [1, 1, 5]
    next_permutation(nums)
    print(nums)  # [1, 5, 1]


# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
# Lexicographical order compares arrays from left to right.
# At the first differing position, the smaller value comes first.
#
# Example order:
# [1, 2, 3] -> [1, 3, 2] -> [2, 1, 3] ->
# [2, 3, 1] -> [3, 1, 2] -> [3, 2, 1]
#
# We want the NEXT arrangement, so make the smallest possible increase.
#
# Example: [1, 3, 5, 4, 2]
#
# 1. Scan from the right to find the pivot:
#    4 >= 2, so continue.
#    5 >= 4, so continue.
#    3 < 5, so k = 1 and the pivot is 3.
#
#    Everything after the pivot is non-increasing: [5, 4, 2].
#    That suffix is already its largest arrangement.
#    Therefore, we must increase the pivot to get a larger permutation.
#
# 2. Find the rightmost value greater than 3:
#    Skip 2; choose 4.
#    Because the suffix is non-increasing, this is its smallest value
#    that is greater than the pivot.
#
# 3. Swap 3 and 4:
#    [1, 4, 5, 3, 2]
#
# 4. Reverse the suffix [5, 3, 2] to get its smallest arrangement:
#    [1, 4, 2, 3, 5]
#
# Why initialize k = -1?
# Unlike C++, Python's for-loop variable does not become -1 when a
# backward range finishes. We explicitly record whether a pivot was found.
#
# Empty and single-element arrays remain unchanged.
# The function modifies the original array and returns None.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n) WORST CASE
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with the number of elements n.
#
# Finding the pivot: at most n - 1 comparisons -> O(n).
# Finding the replacement: at most n - 1 comparisons -> O(n).
# Swapping the pivot: O(1).
# Reversing the suffix: at most n/2 swaps -> O(n).
#
# These operations run sequentially, so ADD their costs:
# O(n) + O(n) + O(1) + O(n) = O(n).
#
# If no pivot exists, finding that out and reversing also take O(n).
# Best-case time is O(1), when the final two elements are increasing.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(1)
# ---------------------------------------------------------------------------
# Only a fixed number of index variables and temporary swap values are used.
# The suffix is reversed directly with two pointers.
# No additional list or recursion is needed.
#
# Avoid nums[k + 1:] = nums[k + 1:][::-1] if O(1) space is required:
# slicing would create additional lists.

'''
Time Complexity: O(n)

Reason:
The algorithm scans from the right to find the pivot, scans again to find
the next larger value, then reverses the suffix. Each step is linear at most.

Space Complexity: O(1)

Reason:
All changes are made in place using only index variables and swaps.
'''
