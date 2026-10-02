def countZeroSumSubarrays(arr, n):
    sumMap = {}
    sum = 0
    count = 0

    sumMap[0] = [-1]

    for i in range(n):
        sum += arr[i]

        if sum in sumMap:
            count += len(sumMap[sum])

        if sum not in sumMap:
            sumMap[sum] = []
        sumMap[sum].append(i)

    return count


arr = [0, 0, 5, 5, 0, 0]
result = countZeroSumSubarrays(arr, len(arr))
print("Total zero-sum subarrays:", result)


'''
Time Complexity: O(n)

Reason:
The array is scanned once. Dictionary lookup and append are O(1) on average.
For each index, we add the number of previous equal prefix sums to count.

Space Complexity: O(n)

Reason:
The map stores lists of indices for prefix sums, and together those lists
can contain n indexes.
'''
