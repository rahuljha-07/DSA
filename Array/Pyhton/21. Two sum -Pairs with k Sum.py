def get_pairs_count(arr, k):
    count = 0
    frequency = {}  # Value -> number of times it has appeared so far.

    for i in range(len(arr)):
        complement = k - arr[i]

        # Each earlier occurrence of the complement forms a valid pair.
        if complement in frequency:
            count += frequency[complement]

        # Record the current value AFTER counting its pairs.
        frequency[arr[i]] = frequency.get(arr[i], 0) + 1

    return count


if __name__ == "__main__":
    arr = [1, 5, 7, -1, 5]
    k = 6

    print("Number of pairs:", get_pairs_count(arr, k))
    # Output: Number of pairs: 3
    # Index pairs: (0, 1), (0, 4), (2, 3).
    # Value pairs: (1, 5), (1, 5), (7, -1).

    print(get_pairs_count([3, 3, 3], 6))  # 3


# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
# For each value x, we need an earlier value equal to k - x.
# The dictionary stores the frequencies of previously visited values.
#
# Example: arr = [1, 5, 7, -1, 5], k = 6.
#
# Current 1:
# Need 5. None seen yet.
# count = 0; record 1.
#
# Current 5:
# Need 1. Seen once.
# count = 1; record 5.
#
# Current 7:
# Need -1. None seen yet.
# count = 1; record 7.
#
# Current -1:
# Need 7. Seen once.
# count = 2; record -1.
#
# Current 5:
# Need 1. Seen once.
# count = 3; record this second 5.
#
# Why count BEFORE recording the current value?
# For x = 3 and k = 6, recording first would let the element pair
# with itself. We must only pair it with earlier elements.
#
# Why add the frequency rather than just 1?
# For [3, 3, 3] and k = 6:
# - First 3 finds 0 earlier threes.
# - Second 3 finds 1 earlier three.
# - Third 3 finds 2 earlier threes.
# Total = 0 + 1 + 2 = 3 pairs.
#
# frequency.get(value, 0):
# Returns the stored frequency, or 0 if the value is not present.
#
# Each pair is counted exactly once, when its later element is visited.
# The original array is not modified.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n) EXPECTED
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with the number of elements n.
#
# We visit each element once.
# Dictionary lookup and update take O(1) on average.
#
# Expected total work = n × O(1) = O(n).
#
# Pathological hash collisions can make dictionary operations O(n),
# giving O(n²) worst-case total time.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(n) WORST CASE
# ---------------------------------------------------------------------------
# Extra space measures additional memory beyond the input array.
#
# The dictionary stores one entry for each distinct value.
# With u distinct values, it uses O(u) space.
# In the worst case, every value is distinct, so u = n.
#
# Therefore, worst-case extra space is O(n).