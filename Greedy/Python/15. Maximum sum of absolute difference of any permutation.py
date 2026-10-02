def maxAbsoluteDifferenceSum(arr):
    arr.sort()
    result = []
    n = len(arr)
    if n == 0:
        return 0
    left = 0
    right = n - 1
    while left <= right:
        if left == right:
            result.append(arr[left])
        else:
            result.append(arr[left])
            result.append(arr[right])
        left += 1
        right -= 1
    maxSum = 0
    for i in range(n - 1):
        maxSum += abs(result[i] - result[i + 1])
    maxSum += abs(result[n - 1] - result[0])
    return maxSum


def main():
    arr = [1, 2, 4, 8]
    print(maxAbsoluteDifferenceSum(arr))


if __name__ == "__main__":
    main()


'''
Let n be the array length.
Time: O(n log(n+1)): sorting dominates building the alternating permutation
and summing its n differences, including the last-to-first cyclic difference.
Space: O(n) auxiliary: result holds n elements and sorting can also use
O(n) temporary space. The input arr is sorted in place.
'''
