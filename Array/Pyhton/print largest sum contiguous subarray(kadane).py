def maxSubarraySum(arr):
    # Assumes arr is nonempty.
    maxi = float("-inf")
    # Current subarray sum
    sum = 0
    # Start index of the max subarray
    ansStart = -1
    # End index of the max subarray
    ansEnd = -1
    # Temporary start index for the current subarray
    start = 0

    for i in range(len(arr)):
        # Start of a potential new subarray.
        if sum == 0:
            start = i

        # Add the current element to the sum
        sum += arr[i]

        # Update the maximum sum and its indices.
        if sum > maxi:
            maxi = sum
            ansStart = start
            ansEnd = i

        # Discard a negative running sum.
        if sum < 0:
            sum = 0

    # Optionally, print the indices of the maximum sum subarray
    print("Maximum subarray sum is from index", ansStart, "to", ansEnd)
    return maxi


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum subarray sum:", maxSubarraySum(arr))

# Output:
# Maximum subarray sum is from index 3 to 6
# Maximum subarray sum: 6


'''
TIME: O(n)
The loop visits each element once and performs O(1) work per iteration.

EXTRA SPACE: O(1)
Only a fixed number of variables are used.
The subarray is tracked using indices, without creating another list.
'''
