def minSwaps(nums):
    n = len(nums)
    v = [None] * n

    for i in range(n):
        v[i] = [nums[i], i]

    v.sort()

    c = 0
    i = 0
    while i < n:
        if v[i][1] == i:
            i += 1
        else:
            c += 1
            swapIndex = v[i][1]
            v[i], v[swapIndex] = v[swapIndex], v[i]

    return c


nums = [10, 19, 6, 3, 5]
print(minSwaps(nums))


'''
Time Complexity: O(n log n)

Reason:
The value/index pairs are sorted first, which takes O(n log n). The cycle
fixing loop performs at most O(n) swaps, so sorting dominates.

Space Complexity: O(n)

Reason:
The pair list v stores each element with its original index.
'''
