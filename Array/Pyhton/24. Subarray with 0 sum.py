def subarray_exists(arr):
    seen = set()  # Stores prefix sums encountered so far.
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        # Zero prefix sum: arr[0] through arr[i] sums to 0.
        # Repeated prefix sum: the elements between the two occurrences sum to 0.
        if current_sum == 0 or current_sum in seen:
            return True

        seen.add(current_sum)

    return False


if __name__ == "__main__":
    arr = [4, 2, -3, 1, 6]

    print("Zero-sum subarray exists:", subarray_exists(arr))
    # Output: Zero-sum subarray exists: True
    # The subarray [2, -3, 1] sums to 0.

    print(subarray_exists([1, 2, 3]))  # False
    print(subarray_exists([5, 0, 3]))  # True — [0] is valid.
    print(subarray_exists([]))         # False


# ---------------------------------------------------------------------------
# HOW IT WORKS: PREFIX SUM + SET
# ---------------------------------------------------------------------------
# A prefix sum is the sum of all elements from index 0 to the current index.
#
# There are two ways to detect a zero-sum subarray:
#
# 1. The current prefix sum is 0.
#    Example: [2, -2].
#    The entire prefix sums to 0.
#
# 2. The same prefix sum appears twice.
#    The elements added between those occurrences must sum to 0.
#
# Example: [4, 2, -3, 1, 6]
#
# Index 0: sum = 4. Store 4.
# Index 1: sum = 6. Store 6.
# Index 2: sum = 3. Store 3.
# Index 3: sum = 4. Already seen! Return True.
#
# Prefix sum through index 3 = 4.
# Prefix sum through index 0 = 4.
# Subarray sum from index 1 through 3 = 4 - 4 = 0.
# That subarray is [2, -3, 1].
#
# Check BEFORE inserting the current sum.
# Otherwise, every sum would find itself in the set immediately.
#
# This function returns only True or False, not the subarray itself.
# The original array is not modified.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n) EXPECTED
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with the number of elements n.
#
# We visit at most n elements.
# Set lookup and insertion take O(1) on average.
#
# Expected total work = n × O(1) = O(n).
# Best case: O(1), if the first element is 0.
#
# Pathological hash collisions can cause O(n²) worst-case total time.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(n) WORST CASE
# ---------------------------------------------------------------------------
# Extra space measures additional memory beyond the input array.
#
# The set can store up to n distinct prefix sums.
# Other variables use O(1) space.
#
# Therefore, worst-case extra space is O(n).