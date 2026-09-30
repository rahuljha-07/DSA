def more_than_n_by_k(arr, k):
    if k <= 0:
        raise ValueError("k must be greater than 0.")

    n = len(arr)
    threshold = n // k
    frequency = {}

    # Count the occurrences of each value.
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    # Print values whose frequency is STRICTLY greater than n/k.
    for num, count in frequency.items():
        if count > threshold:
            print(num)


if __name__ == "__main__":
    arr = [3, 1, 2, 2, 1, 2, 3, 3]
    k = 4

    more_than_n_by_k(arr, k)

    # Output:
    # 3
    # 2
    #
    # n = 8, so n/k = 2.
    # 3 appears 3 times -> qualifies.
    # 1 appears 2 times -> does not qualify.
    # 2 appears 3 times -> qualifies.


# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
# First, build a dictionary:
# value -> number of occurrences.
#
# For the example:
# frequency = {3: 3, 1: 2, 2: 3}.
#
# Then check each distinct value's count against n // k.
#
# frequency.get(num, 0):
# Returns the current count, or 0 if num is not yet in the dictionary.
#
# frequency.items():
# Gives each (value, count) pair.
# This matches i.first and i.second in your C++ unordered_map loop.
#
# Why is integer division correct?
# Counts are integers, so:
# count > n/k is equivalent to count > floor(n/k).
#
# Example: n = 10, k = 3.
# n/k is approximately 3.33, so a qualifying count must be at least 4.
# Checking count > 10 // 3 means count > 3, giving the same result.
#
# Use >, not >=: appearing exactly n/k times does not qualify.
#
# Python dictionaries preserve insertion order, so qualifying values
# print in their first-appearance order. They are not automatically sorted.
#
# Empty input prints nothing.
# The original array is not modified.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n) EXPECTED
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with the input size n.
#
# Counting frequencies: n iterations with average O(1) dictionary work.
# Checking frequencies: u iterations, where u is the distinct-value count.
# Since u <= n:
#
# O(n + u) = O(n) expected.
#
# The loops run sequentially, so ADD their costs.
# Pathological hash collisions can cause O(n²) worst-case total time.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(n) WORST CASE
# ---------------------------------------------------------------------------
# The dictionary stores one entry for each of the u distinct values.
# Extra space is O(u), which becomes O(n) when all values are distinct.
#
# Other variables use O(1) space.