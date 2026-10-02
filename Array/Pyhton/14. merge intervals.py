# 14. Merge Overlapping Intervals
# Each interval is [start, end], with start <= end.


def merge(intervals):
    # Sort by start, then by end when starts are equal.
    intervals.sort()
    ans = []

    for i in range(len(intervals)):
        start = intervals[i][0]
        end = intervals[i][1]

        # No previous interval, or this interval starts after the last one ends.
        if not ans or start > ans[-1][1]:
            ans.append([start, end])
        else:
            # Overlap: extend the last merged interval if needed.
            ans[-1][1] = max(ans[-1][1], end)

    return ans


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

    print("Merged intervals:", merge(intervals))
    # Output: Merged intervals: [[1, 6], [8, 10], [15, 18]]


# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
# Sorting places intervals in increasing order of their start values.
# Each interval then needs comparison only with the LAST merged interval.
#
# Python equivalents of your C++ code:
# - ans.empty()  -> not ans
# - ans.back()  -> ans[-1]
# - push_back() -> append()
#
# Example:
# [1, 3]   -> ans is empty; add it.
#            ans = [[1, 3]]
#
# [2, 6]   -> 2 <= 3, so they overlap.
#            Update the end to max(3, 6) = 6.
#            ans = [[1, 6]]
#
# [8, 10]  -> 8 > 6, so there is no overlap; add it.
#            ans = [[1, 6], [8, 10]]
#
# [15, 18] -> 15 > 10; add it.
#            ans = [[1, 6], [8, 10], [15, 18]]
#
# Why use max()?
# For [1, 10] and [2, 5], the second interval is inside the first.
# The merged end must remain 10, not shrink to 5.
#
# Touching intervals also merge:
# [1, 3] and [3, 5] -> [1, 5].
#
# An empty input returns [].
# Sorting changes the order of the original input list.
# Appending [start, end] creates a separate pair, so extending the answer
# does not modify the original interval's endpoints.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n log n) WORST CASE
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with the number of intervals n.
#
# Sorting: O(n log n).
# Loop: visits n intervals once, with O(1) work per interval
#       (including amortized O(1) append).
#
# These steps run sequentially, so ADD their costs:
# O(n log n) + O(n) = O(n log n).


# ---------------------------------------------------------------------------
# SPACE COMPLEXITY: O(n) WORST CASE
# ---------------------------------------------------------------------------
# If no intervals overlap, ans stores all n intervals: O(n) output space.
# Python's list.sort() can also use O(n) temporary space.
#
# Total additional space, including the output: O(n).
# Auxiliary space excluding the output: O(n) worst case due to sorting.

'''
Time Complexity: O(n log n)

Reason:
Intervals are sorted first, which costs O(n log n). The merge pass then
visits each interval once, so sorting dominates.

Space Complexity: O(n)

Reason:
The answer list can store all intervals when none overlap. Python sorting
may also use temporary memory.
'''
