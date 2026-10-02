# ---------------------------------------------------------------------------
# APPROACH 1: O(n) EXTRA SPACE — ORDER PRESERVED
# ---------------------------------------------------------------------------

def rearrange_with_extra_space(nums):
    positives = []
    negatives = []
    result = []

    # Collect each group in its original relative order.
    for num in nums:
        if num >= 0:
            positives.append(num)
        else:
            negatives.append(num)

    i = j = 0

    # Alternate while both groups have elements.
    while i < len(positives) and j < len(negatives):
        result.append(positives[i])
        result.append(negatives[j])
        i += 1
        j += 1

    # Append whichever group still has elements.
    while i < len(positives):
        result.append(positives[i])
        i += 1

    while j < len(negatives):
        result.append(negatives[j])
        j += 1

    return result


# ---------------------------------------------------------------------------
# APPROACH 2: O(1) EXTRA SPACE — ORDER NOT PRESERVED
# ---------------------------------------------------------------------------

def rearrange_in_place(nums):
    pos = 0  # Start with the even index, expecting positive number here.
    neg = 1  # Start with the odd index, expecting negative number here.

    while True:
        # Find the first misplaced positive position.
        while pos < len(nums) and nums[pos] >= 0:
            pos += 2

        # Find the first misplaced negative position.
        while neg < len(nums) and nums[neg] < 0:
            neg += 2

        # Swap if both misplaced elements exist.
        if pos < len(nums) and neg < len(nums):
            nums[pos], nums[neg] = nums[neg], nums[pos]
        else:
            break


# ---------------------------------------------------------------------------
# APPROACH 3: O(1) EXTRA SPACE — ORDER PRESERVED
# ---------------------------------------------------------------------------

def rearrange_maintain_order(nums):
    n = len(nums)

    for i in range(n):
        if i % 2 == 0:
            # Even index: expect a nonnegative number.
            if nums[i] >= 0:
                continue

            j = i + 1
            while j < n and nums[j] < 0:
                j += 1
        else:
            # Odd index: expect a negative number.
            if nums[i] < 0:
                continue

            j = i + 1
            while j < n and nums[j] >= 0:
                j += 1

        # No number of the required sign remains.
        # Leave the remaining elements in their existing order.
        if j == n:
            break

        # Bring nums[j] to index i by shifting intervening elements right.
        # This preserves relative order within both sign groups.
        value = nums[j]

        while j > i:
            nums[j] = nums[j - 1]
            j -= 1

        nums[i] = value


if __name__ == "__main__":
    nums = [1, 2, 3, -1, -2, -3, -4]
    print("Extra space:", rearrange_with_extra_space(nums))
    # [1, -1, 2, -2, 3, -3, -4]

    nums = [1, 2, 3, -1, -2, -3, -4]
    rearrange_in_place(nums)
    print("In place, order not preserved:", nums)
    # [1, -1, 3, -2, 2, -3, -4]

    nums = [1, 2, 3, -1, -2, -3, -4]
    rearrange_maintain_order(nums)
    print("In place, order preserved:", nums)
    # [1, -1, 2, -2, 3, -3, -4]


# ---------------------------------------------------------------------------
# HOW THE APPROACHES DIFFER
# ---------------------------------------------------------------------------
# Approach 1:
# Separate the groups, then build a new alternating result.
# The original input is unchanged.
#
# Approach 2:
# Partition into nonnegative and negative regions, then interleave by swaps.
# Swapping can change relative order within the groups.
#
# Approach 3:
# At each incorrect position, find the next required sign.
# Save that element, shift the intervening elements right, and insert it.
# Shifting preserves relative order but can require more work.
#
# Empty inputs and inputs containing only one sign are also supported.


# ---------------------------------------------------------------------------
# TIME AND EXTRA SPACE COMPLEXITY
# ---------------------------------------------------------------------------
# Time complexity: how the amount of work grows with input size n.
# Extra space complexity: additional memory beyond the input array.
#
# APPROACH 1:
# Time: O(n).
# - Separating the elements takes O(n).
# - Building the result takes O(n).
# - Sequential costs add: O(n) + O(n) = O(n).
#
# Extra space: O(n).
# - positives and negatives together store n elements.
# - result stores another n elements.
# - O(2n) simplifies to O(n).
#
# APPROACH 2:
# Time: O(n).
# - Partitioning scans n elements.
# - Interleaving performs at most O(n) swaps.
# - Total: O(n) + O(n) = O(n).
#
# Extra space: O(1).
# - Only a fixed number of variables; no extra lists.
#
# APPROACH 3:
# Time: O(n²) worst case.
# - Up to n positions are considered.
# - Finding and shifting an element can take O(n) per position.
# - Long groups of the same sign can require repeated long shifts.
# - Worst case: O(n²). Best case: O(n) if already arranged.
#
# Extra space: O(1).
# - Shifting uses one saved value and a few indices.
# - No slices, extra lists, or recursion are used.


'''
Time Complexity:
Approach 1: O(n)
Approach 2: O(n)
Approach 3: O(n^2) worst case

Reason:
Approach 1 separates and rebuilds the array with linear scans.
Approach 2 moves even and odd misplaced pointers forward only.
Approach 3 may repeatedly search ahead and shift elements, causing
quadratic work in the worst case.

Space Complexity:
Approach 1: O(n)
Approach 2: O(1)
Approach 3: O(1)

Reason:
Approach 1 uses extra positive, negative, and result lists.
Approaches 2 and 3 modify the array in place using fixed variables.
'''
