# 25. Length of the Longest Subarray with Sum 0
# Store each prefix sum with the FIRST index where it appeared.


def max_len(arr):
    first_index = {}  # Prefix sum -> earliest index.
    maximum = 0
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum == 0:
            # The entire prefix from index 0 through i sums to 0.
            maximum = i + 1
        else:
            if current_sum in first_index:
                # Elements AFTER the earlier index through i sum to 0.
                maximum = max(maximum, i - first_index[current_sum])
            else:
                # Keep only the first occurrence to get the longest length.
                first_index[current_sum] = i

    return maximum


if __name__ == "__main__":
    arr = [15, -2, 2, -8, 1, 7, 10, 23]

    print("Longest zero-sum subarray length:", max_len(arr))
    # Output: Longest zero-sum subarray length: 5
    # Subarray: [-2, 2, -8, 1, 7], at indices 1 through 5.

    print(max_len([1, 0]))     # 1 — subarray [0].
    print(max_len([0, 0, 0]))  # 3 — the entire array.
    print(max_len([1, 2, 3]))  # 0 — no zero-sum subarray.


# ---------------------------------------------------------------------------
# HOW IT WORKS: PREFIX SUM + DICTIONARY
# ---------------------------------------------------------------------------
# Yes, your map stores:
#     prefix sum -> index where that sum FIRST appeared.
#
# Important: that stored index is just BEFORE the zero-sum subarray,
# not the first index inside it.
#
# If the same prefix sum occurs at indices j and i:
# sum of arr[j + 1] through arr[i] = prefix_sum[i] - prefix_sum[j] = 0.
#
# Length = i - (j + 1) + 1 = i - j.
#
# Example: [1, 0]
# Index 0: current_sum = 1. Store {1: 0}.
# Index 1: current_sum = 1 again.
# Length = 1 - 0 = 1. The subarray is [0].
#
# Larger example: [15, -2, 2, -8, 1, 7, 10, 23]
# Index 0: sum = 15. Store {15: 0}.
# Index 1: sum = 13. Store {13: 1}.
# Index 2: sum = 15 again. Length = 2 - 0 = 2.
# Index 3: sum = 7. Store {7: 3}.
# Index 4: sum = 8. Store {8: 4}.
# Index 5: sum = 15 again. Length = 5 - 0 = 5.
# Remaining indices do not produce a longer zero-sum subarray.
#
# Why keep the FIRST index?
# The earliest occurrence gives the largest distance to the current index.
# If we replaced {15: 0} with {15: 2}, then at index 5 we would calculate
# only 5 - 2 = 3 instead of 5 - 0 = 5.
#
# Why handle current_sum == 0 separately?
# The subarray starts at index 0, so its length is i + 1.
# This is the longest possible subarray ending at i.
#
# Unlike the previous existence-check problem, a set is not enough:
# we need the earlier INDEX to calculate the length.
#
# Empty input returns 0. The original array is not modified.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n) EXPECTED
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with the number of elements n.
#
# The loop visits all n elements once.
# Dictionary lookup and insertion take O(1) on average.
# Other calculations take O(1) per iteration.
#
# Expected total work = n × O(1) = O(n).
# Pathological hash collisions can cause O(n²) worst-case total time.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(n) WORST CASE
# ---------------------------------------------------------------------------
# Extra space measures additional memory beyond the input array.
#
# The dictionary can store up to n distinct prefix sums and their indices.
# Other variables use O(1) space.
#
# Therefore, worst-case extra space is O(n).

'''
Time Complexity: O(n) expected

Reason:
The loop visits each element once. Dictionary lookup and insertion for
prefix sums are O(1) on average.

Space Complexity: O(n)

Reason:
The dictionary can store the first index of up to n distinct prefix sums.
'''
