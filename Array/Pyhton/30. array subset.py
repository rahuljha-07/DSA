def is_subset(arr1, arr2):
    values = set()

    # Store the distinct values from arr1.
    for num in arr1:
        values.add(num)

    # Every value in arr2 must exist in arr1.
    for num in arr2:
        if num not in values:
            return "No"

    return "Yes"


if __name__ == "__main__":
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]

    print(is_subset(arr1, arr2))       # Yes
    print(is_subset([1, 2], [2, 3]))   # No
    print(is_subset([1, 2], [1, 1]))   # Yes — checks presence only.
    print(is_subset([1, 2], []))       # Yes — an empty set is a subset.


# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
# A set stores unique values and supports fast membership checks.
#
# 1. Insert all values from arr1 into a set.
# 2. Check every value in arr2.
# 3. If any value is missing, return "No" immediately.
# 4. If all values exist, return "Yes".
#
# Important: this matches your C++ code's presence-only behavior.
# For arr1 = [1, 2] and arr2 = [1, 1], the answer is "Yes".
# Both checks find 1; we do not remove it after checking.
#
# If the problem requires matching duplicate frequencies, use a frequency
# dictionary instead and decrease the count after each match.
#
# Neither input array is modified.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n + m) EXPECTED
# ---------------------------------------------------------------------------
# n = len(arr1), m = len(arr2).
#
# Building the set: n insertions -> O(n) expected.
# Checking arr2: at most m lookups -> O(m) expected.
# Python set insertion and lookup take O(1) on average.
#
# Total: O(n) + O(m) = O(n + m) expected.
#
# Your C++ code uses std::set, an ordered structure whose insertion and
# lookup take O(log n). Python's set is hash-based, more like unordered_set.
#
# Pathological hash collisions can make the Python version take
# O(n² + n*m) time in the worst case.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(n) WORST CASE
# ---------------------------------------------------------------------------
# The set stores at most n distinct values from arr1.
# Other variables use O(1) space.
#
# Therefore, worst-case extra space is O(n).