def maxProductSubset(arr):
    if len(arr) == 1:
        return arr[0]
    positiveProduct = 1
    negativeProduct = 1
    negativeCount = 0
    zeroCount = 0
    maxNegative = float("-inf")
    for num in arr:
        if num == 0:
            zeroCount += 1
            continue
        if num > 0:
            positiveProduct *= num
        else:
            negativeCount += 1
            maxNegative = max(maxNegative, num)
            negativeProduct *= num
    if zeroCount == len(arr):
        return 0
    if negativeCount == 1 and negativeCount + zeroCount == len(arr) and zeroCount > 0:
        return 0
    if negativeCount % 2 != 0:
        negativeProduct //= maxNegative
    return positiveProduct * (negativeProduct if negativeCount > 0 else 1)


def main():
    arr = [-1, 0, -2, 4, 3]
    print("Maximum Product Subset:", maxProductSubset(arr))


if __name__ == "__main__":
    main()


'''
Let n be elements.
Time: O(n) arithmetic operations: scan signs/products once, then remove
the closest-to-zero negative factor if needed. No sorting or subsets.
Space: O(1) numeric variables under fixed-size arithmetic; Python products
are arbitrary precision, so actual time/storage also grow with product bits.
Nonempty-subset edge cases are corrected: a singleton negative returns
itself, and a positive 1 is not mistaken for the absence of positive values.
Empty input returns zero, retaining the source's all-zero condition.
'''
