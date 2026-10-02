def trappingWater(arr, n):
    if n == 0:
        return 0

    # Arrays to store the maximum height to the left and right of each index.
    maxLeft = [0] * n
    maxRight = [0] * n

    # Fill maxLeft array.
    maxLeft[0] = arr[0]
    for i in range(1, n):
        maxLeft[i] = max(maxLeft[i - 1], arr[i])

    # Fill maxRight array.
    maxRight[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        maxRight[i] = max(maxRight[i + 1], arr[i])

    # Calculate the total trapped water.
    totalWater = 0
    for i in range(n):
        totalWater += min(maxLeft[i], maxRight[i]) - arr[i]

    return totalWater


arr = [3, 0, 0, 2, 0, 4]
print(trappingWater(arr, len(arr)))  # 10


# TIME COMPLEXITY: O(n)
# Each loop takes O(n). The loops run separately, so their costs add:
# O(n) + O(n) + O(n) = O(n).
#
# EXTRA SPACE COMPLEXITY: O(n)
# maxLeft and maxRight each store n values:
# O(n) + O(n) = O(n).

'''
Time Complexity: O(n)

Reason:
One pass builds maxLeft, one pass builds maxRight, and one pass calculates
water at every index. The three linear passes add to O(n).

Space Complexity: O(n)

Reason:
maxLeft and maxRight each store n values.
'''
