def max_subarray_sum(arr):
    # A nonempty subarray requires at least one element.
    if not arr:
        raise ValueError("The list must not be empty.")

    maximum = arr[0]  # Best subarray sum found so far.
    current_sum = 0  # Running sum of the current candidate subarray.

    for num in arr:
        current_sum += num

        # Record the best sum BEFORE resetting a negative running sum.
        # This ensures all-negative lists return the largest element, not 0.
        maximum = max(maximum, current_sum)

        if current_sum < 0:
            # A negative sum would only reduce the sum of future elements.
            # Discard this candidate and start fresh at the next element.
            current_sum = 0

    return maximum


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]

    print("Maximum subarray sum:", max_subarray_sum(arr))
    # Output: Maximum subarray sum: 7
    # The subarray is [4, -1, -2, 1, 5].

    print("All-negative example:", max_subarray_sum([-5, -2, -8]))
    # Output: All-negative example: -2


# ---------------------------------------------------------------------------
# HOW IT WORKS: KADANE'S ALGORITHM
# ---------------------------------------------------------------------------
# A subarray is a CONTIGUOUS portion of an array: elements must be adjacent.
# We want the largest sum among all nonempty subarrays.
#
# At each element:
# 1. Add it to current_sum.
# 2. Update maximum if this sum is better.
# 3. If current_sum becomes negative, reset it to 0.
#
# Why discard a negative sum?
# If the previous portion sums to -5 and the next element is 4:
# - Keeping that portion gives -5 + 4 = -1.
# - Starting fresh gives 4.
# A negative prefix can only make any future subarray sum smaller.
#
# A positive running sum is kept even when the current element is negative,
# because that running sum might still help build a better answer later.
#
# Example:
#
# num | current_sum after adding | maximum | current_sum after reset
# ----|--------------------------|---------|------------------------
# -2  |           -2             |   -2    |            0
# -3  |           -3             |   -2    |            0
#  4  |            4             |    4    |            4
# -1  |            3             |    4    |            3
# -2  |            1             |    4    |            1
#  1  |            2             |    4    |            2
#  5  |            7             |    7    |            7
# -3  |            4             |    7    |            4
#
# Answer: 7.
#
# Initializing maximum to arr[0], instead of 0, allows negative answers.
# Updating maximum before resetting ensures those answers are recorded.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n)
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with the input size n.
#
# - The loop visits each of the n elements exactly once.
# - Each iteration performs one addition, a maximum comparison,
#   a condition check, and possibly an assignment.
# - Each operation takes O(1) under the usual integer-operation model.
#
# Total work = n × O(1) = O(n).
#
# Best, average, and worst-case time are all O(n) for nonempty lists.
# We do not explicitly generate and sum every possible subarray.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(1)
# ---------------------------------------------------------------------------
# Extra space measures additional memory beyond the input list.
#
# Only a fixed number of variables are used:
# maximum, current_sum, and num.
#
# No additional array or recursive calls are needed.
# Therefore, extra space is O(1).
# The input list is not modified.

'''
Time Complexity: O(n)

Reason:
Kadane's algorithm scans the array once. At each element it updates the
running sum and best answer in constant time.

Space Complexity: O(1)

Reason:
Only the running sum and maximum sum variables are stored.
'''
