def find_longest_conseq_subseq(arr):
    if not arr:
        return 0

    values = set()
    maximum = arr[0]
    minimum = arr[0]

    # Store unique values and find the range to scan.
    for num in arr:
        maximum = max(maximum, num)
        minimum = min(minimum, num)
        values.add(num)

    count = 0
    answer = 0

    # Include maximum by using maximum + 1 as the stopping value.
    for num in range(minimum, maximum + 1):
        if num in values:
            count += 1
        else:
            # A missing value breaks the consecutive run.
            answer = max(answer, count)
            count = 0

    # The final run may end at maximum without encountering a missing value.
    answer = max(answer, count)
    return answer


if __name__ == "__main__":
    arr = [1, 9, 3, 10, 4, 20, 2]

    print("Longest consecutive sequence length:",
          find_longest_conseq_subseq(arr))
    # Output: Longest consecutive sequence length: 4
    # Consecutive values: 1, 2, 3, 4.

    print(find_longest_conseq_subseq([1, 2, 2, 3]))  # 3
    print(find_longest_conseq_subseq([]))            # 0


# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
# Store the values in a set for fast membership checks.
# Then check every integer from the minimum value to the maximum value.
#
# Example: [1, 9, 3, 10, 4, 20, 2]
# minimum = 1, maximum = 20.
#
# Values 1, 2, 3, 4 exist -> count reaches 4.
# Value 5 is missing -> save answer = 4 and reset count.
# Values 9, 10 exist -> count reaches 2.
# Value 11 is missing -> answer stays 4 and count resets.
# Value 20 exists -> count becomes 1.
# Final update keeps answer = 4.
#
# Why update answer AFTER the loop?
# For [1, 2, 3], no missing value is encountered during the scan.
# Without the final update, that last run would never be recorded.
#
# The values do not need to be adjacent or appear in order in the input.
# Here, "consecutive" means consecutive integer values.
# The original array is not modified.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n + R) EXPECTED
# ---------------------------------------------------------------------------
# n = number of input elements.
# R = maximum - minimum + 1, the size of the value range.
#
# Building the set and finding min/max: O(n) expected.
# Scanning every integer in the range: O(R) expected.
# Set insertion and membership checks take O(1) on average.
#
# Total: O(n + R), NOT necessarily O(n).
#
# Example: [1, 1_000_000_000]
# Only 2 input elements, but this solution checks 1 billion values.
# Therefore, it can be very slow when values are far apart.
#
# An expected O(n) alternative starts a run only at values whose
# predecessor is absent, then checks consecutive values that exist.
#
# These expected bounds assume average O(1) hash-set operations.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(n) WORST CASE
# ---------------------------------------------------------------------------
# The set stores at most n distinct values.
# Other variables use O(1) space.
#
# Python's range does not create a list of all R integers.
# Therefore, extra space is O(n), not O(R).