# Function to calculate the maximum sum of absolute differences
def maxAbsoluteDifferenceSum(arr):
    # Step 1: Sort the array
    arr.sort()
    # Step 2: Create the new sequence by alternating smallest and largest elements
    result = []
    n = len(arr)
    if n == 0:
        return 0
    left = 0
    right = n - 1
    while left <= right:
        if left == right:
            # Add the last remaining element if odd-sized
            # Add smallest element
            result.append(arr[left])
        else:
            result.append(arr[left])
            # Add largest element
            result.append(arr[right])
        left += 1
        right -= 1
    # Step 3: Calculate the sum of absolute differences
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
