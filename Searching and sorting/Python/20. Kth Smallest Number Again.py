def findKthSmallestNumber(intervals, k):
    intervals.sort()

    idx = 0
    for i in range(1, len(intervals)):
        if intervals[idx][1] >= intervals[i][0]:
            intervals[idx][1] = max(intervals[idx][1], intervals[i][1])
        else:
            idx += 1
            intervals[idx] = intervals[i]

    answer = -1
    for i in range(idx + 1):
        intervalSize = intervals[i][1] - intervals[i][0] + 1

        if intervalSize >= k:
            answer = intervals[i][0] + k - 1
            break
        else:
            k -= intervalSize

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
