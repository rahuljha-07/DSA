def min_subarray_sum(arr):
    # A nonempty subarray requires at least one element.
    if not arr:
        raise ValueError("The list must not be empty.")

    minimum = arr[0]  # Smallest subarray sum found so far.
    current_sum = 0  # Running sum of the current candidate subarray.

    for num in arr:
        current_sum += num

        # Update BEFORE resetting so all-positive lists work correctly.
        minimum = min(minimum, current_sum)

        if current_sum > 0:
            # A positive sum would increase the sum of future elements.
            # Discard it and start fresh at the next element.
            current_sum = 0

    return minimum


if __name__ == "__main__":
    arr = [3, -4, 2, -3, -1, 7, -5]

    print("Minimum subarray sum:", min_subarray_sum(arr))
    # Output: Minimum subarray sum: -6
    # The subarray is [-4, 2, -3, -1].

    print("All-positive example:", min_subarray_sum([5, 2, 8]))
    # Output: All-positive example: 2


# ---------------------------------------------------------------------------
# HOW IT WORKS: REVERSE KADANE'S ALGORITHM
# ---------------------------------------------------------------------------
# A subarray is a contiguous portion of an array: elements must be adjacent.
# We want the smallest sum among all NONEMPTY subarrays.
#
# At each element:
# 1. Add it to current_sum.
# 2. Update minimum if the current sum is smaller.
# 3. If current_sum becomes positive, reset it to 0.
#
# Why discard a positive sum?
# Suppose the previous portion sums to 5 and the next element is -4:
# - Keeping that portion gives 5 + (-4) = 1.
# - Starting fresh gives -4, which is smaller.
# A positive prefix can only increase any future subarray sum.
#
# Keep a negative running sum even if the current element is positive:
# that negative running sum could help produce a smaller sum later.
#
# Example: [3, -4, 2, -3, -1, 7, -5]
# - Add 3:  current_sum = 3;  minimum = 3;  reset current_sum to 0.
# - Add -4: current_sum = -4; minimum = -4.
# - Add 2:  current_sum = -2; minimum = -4.
# - Add -3: current_sum = -5; minimum = -5.
# - Add -1: current_sum = -6; minimum = -6.
# - Add 7:  current_sum = 1;  minimum = -6; reset current_sum to 0.
# - Add -5: current_sum = -5; minimum = -6.
#
# Answer: -6, from [-4, 2, -3, -1].
#
# Why initialize minimum to arr[0] instead of 0?
# For [5, 2, 8], the correct answer is 2.
# Starting minimum at 0 would incorrectly return 0, even though no
# nonempty subarray has that sum.
#
# Difference from maximum-sum Kadane:
# - Maximum sum: use max() and reset when current_sum < 0.
# - Minimum sum: use min() and reset when current_sum > 0.
#
# This function returns the sum, not the subarray itself.
# The input list is not modified.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n)
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with the input size n.
#
# The loop visits all n elements exactly once.
# Each iteration performs a constant amount of work:
# one addition, a minimum comparison, a condition check, and possibly a reset.
#
# Total work = n × O(1) = O(n).
#
# Best, average, and worst-case time are all O(n) for nonempty lists.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(1)
# ---------------------------------------------------------------------------
# Extra space measures additional memory beyond the input list.
#
# We use only a fixed number of variables: minimum, current_sum, and num.
# No additional list or recursive calls are needed.
#
# Extra memory does not grow with n, so it is O(1).