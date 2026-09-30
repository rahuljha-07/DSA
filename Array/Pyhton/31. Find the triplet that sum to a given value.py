def find_three_numbers(arr, x):
    n = len(arr)
    arr.sort()

    # Fix the first element, leaving at least two elements after it.
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == x:
                return True
            elif total < x:
                left += 1   # Need a larger sum.
            else:
                right -= 1  # Need a smaller sum.

    return False


if __name__ == "__main__":
    arr = [1, 4, 45, 6, 10, 8]
    x = 22

    print("Triplet exists:", find_three_numbers(arr, x))
    # Output: Triplet exists: True
    # Triplet: 4 + 8 + 10 = 22.

    print(find_three_numbers([1, 2, 3], 10))  # False
    print(find_three_numbers([2, 2, 2], 6))   # True


# ---------------------------------------------------------------------------
# HOW IT WORKS: SORTING + TWO POINTERS
# ---------------------------------------------------------------------------
# Sort the array, then fix one element arr[i].
# Find two elements after it whose sum is x - arr[i].
#
# left starts immediately after i.
# right starts at the last index.
#
# If the total is too small:
# Move left forward to try a larger value.
#
# If the total is too large:
# Move right backward to try a smaller value.
#
# Why is moving a pointer safe?
# If the sum is too small, even the largest remaining right-side value
# cannot work with the current left value. We can discard that left value.
# Similarly, if the sum is too large, the current right value cannot
# work with any remaining left value, so we discard it.
#
# Example: [1, 4, 45, 6, 10, 8], target = 22.
# After sorting: [1, 4, 6, 8, 10, 45].
#
# Fix 1: no matching pair is found.
#
# Fix 4:
# 4 + 6 + 45 = 55 -> too large; move right.
# 4 + 6 + 10 = 20 -> too small; move left.
# 4 + 8 + 10 = 22 -> return True.
#
# i < left < right ensures that all three indices are different.
# Values may repeat if they occur at different indices.
#
# Fewer than three elements returns False because the outer loop is empty.
# Sorting modifies the order of the original array.
# This function returns only True or False, not the triplet itself.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n²) WORST CASE
# ---------------------------------------------------------------------------
# Sorting takes O(n log n).
#
# The outer loop tries up to n - 2 first elements.
# For each one, the pointers move toward each other across the remaining
# portion, taking O(n) time at most.
#
# Across all outer iterations, the scans can require:
# (n - 2) + (n - 3) + ... + 1 = O(n²) pointer steps.
#
# Total: O(n log n) + O(n²) = O(n²).
# Finding a match early can reduce the scanning work.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(n) WORST CASE IN PYTHON
# ---------------------------------------------------------------------------
# The two-pointer search itself uses O(1) extra space.
# However, Python's list.sort() can use O(n) temporary memory.
#
# Therefore, including sorting, worst-case extra space is O(n).