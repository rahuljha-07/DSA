# Function to find the maximum product subset of an array
def maxProductSubset(arr):
    if len(arr) == 1:
        return arr[0]
    # Product of all positive numbers
    positiveProduct = 1
    # Product of all negative numbers
    negativeProduct = 1
    # Count of negative numbers
    negativeCount = 0
    # Count of zeros
    zeroCount = 0
    maxNegative = float("-inf")
    # Traverse the array
    for num in arr:
        if num == 0:
            # Ignore zeros
            zeroCount += 1
            continue
        if num > 0:
            # Multiply positives
            positiveProduct *= num
        else:
            negativeCount += 1
            # Track the largest negative
            maxNegative = max(maxNegative, num)
            # Multiply negatives
            negativeProduct *= num
    # If the array only contains zeros, return 0
    if zeroCount == len(arr):
        return 0
    # If there are zeros and only one negative but no positives, choose zero.
    if negativeCount == 1 and negativeCount + zeroCount == len(arr) and zeroCount > 0:
        return 0
    # If there are an odd number of negatives, exclude the largest (closest to 0) negative
    if negativeCount % 2 != 0:
        # Exclude the largest negative
        negativeProduct //= maxNegative
    # Combine positive and adjusted negative product
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
