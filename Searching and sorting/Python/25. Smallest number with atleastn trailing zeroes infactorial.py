def hasAtLeastNTrailingZeroes(number, requiredZeroes):
    temp = number
    count = 0
    factor = 5

    while factor <= temp:
        count += temp // factor
        factor *= 5

    return count >= requiredZeroes


def findSmallestFactorialNumberWithTrailingZeroes(n):
    if n == 1:
        return 5

    low = 0
    high = 5 * n
    result = -1

    while low < high:
        mid = (low + high) // 2
        if hasAtLeastNTrailingZeroes(mid, n):
            result = mid
            high = mid
        else:
            low = mid + 1

    return low


n = 6
result = findSmallestFactorialNumberWithTrailingZeroes(n)
print("The smallest number whose factorial has at least", n, "trailing zeroes is:", result)


'''
Time Complexity: O(log n * log n)

Reason:
Binary search is done from 0 to 5n. For each mid, trailing zeroes are counted
by powers of 5, which takes O(log n) divisions.

Space Complexity: O(1)

Reason:
Only count, factor, and binary-search variables are used.
'''
