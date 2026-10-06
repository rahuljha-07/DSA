def findKthSmallestNumber(intervals, k):
    # Step 1: Sort intervals based on their starting points
    # Automatically sorts by `start` first, then by `end` if `start`s are equal
    intervals.sort()

    # Step 2: Merge overlapping or contiguous intervals
    # Pointer to the last merged interval
    idx = 0
    for i in range(1, len(intervals)):
        if intervals[idx][1] >= intervals[i][0]:
            intervals[idx][1] = max(intervals[idx][1], intervals[i][1])
        else:
            # Move to the next interval in the merged list
            idx += 1
            intervals[idx] = intervals[i]

    # Step 3: Iterate over merged intervals to find the K-th smallest number
    answer = -1
    for i in range(idx + 1):
        # Calculate the size of the current interval
        intervalSize = intervals[i][1] - intervals[i][0] + 1

        if intervalSize >= k:
            # K-th smallest number falls within this interval
            answer = intervals[i][0] + k - 1
            break
        else:
            # Move to the next interval by reducing K
            k -= intervalSize

    # If K-th smallest is not found, answer will be -1
    return answer


intervals = [[1, 5], [3, 8], [10, 12]]
k = 6
print("K-th smallest number:", findKthSmallestNumber(intervals, k))


'''
Time Complexity: O(n log n)

Reason:
Intervals are sorted first. The merge pass and the final scan are both
linear, so sorting dominates.

Space Complexity: O(1) auxiliary

Reason:
Intervals are merged in the same list using indexes. No extra interval list
is created.
'''
