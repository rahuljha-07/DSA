# exaclty same as subset sum partiion just check this condition
def equalPartition(n, arr):
    sum = 0
    for i in range(n):
        sum += arr[i]
    if sum % 2 != 0 or sum == 0:
        return 0
    return subset(arr, n, sum // 2)


def subset(arr, n, sum):
    # The C++ snippet referred to the subset-sum helper from the earlier topic.
    t = [[False] * (sum + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        t[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]
    return t[n][sum]


'''
Let n be elements and S=total//2, with nonnegative values.
Time: O(n) to sum/reject odd or zero totals; otherwise
O((n+1)*(S+1)) to fill the earlier topic's include/exclude subset-sum DP.
Space: O((n+1)*(S+1)) auxiliary table, or O(1) for early rejection.
The missing subset helper is supplied using the existing 2D DP approach.
As in the source, a zero-total array returns 0 even though an equal
empty/all-zero partition is mathematically possible.
'''
