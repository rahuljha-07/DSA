from bisect import bisect_right


def bishopandsoldier(n, q, a, queries):
    a.sort()

    pre = [0] * (n + 1)

    for i in range(1, n + 1):
        pre[i] = pre[i - 1] + a[i - 1]

    for x in queries:
        idx = bisect_right(a, x)
        print(idx, pre[idx])


n = 7
a = [1, 2, 3, 4, 5, 6, 7]
queries = [3, 10]
bishopandsoldier(n, len(queries), a, queries)


'''
Time Complexity: O(n log n + q log n)

Reason:
The soldiers array is sorted once. Prefix sum construction is O(n). Each
query uses upper_bound/bisect_right, which is O(log n).

Space Complexity: O(n)

Reason:
The prefix sum list stores n + 1 values.
'''
