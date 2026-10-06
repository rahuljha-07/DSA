def countZeroSumSubarrays(arr, n):
    # Map to store cumulative sums and their indices
    sumMap = {}
    # Cumulative sum
    sum = 0
    # Count of zero-sum subarrays
    count = 0

    # Initialize map with sum 0 at index -1 (to handle subarrays starting at index 0)
    sumMap[0] = [-1]

    # Traverse the array
    for i in range(n):
        # Add current element to cumulative sum
        sum += arr[i]

        if sum in sumMap:
            # If found, the number of zero-sum subarrays ending at i is the number of times
            # this sum has appeared before
            count += len(sumMap[sum])

        if sum not in sumMap:
            sumMap[sum] = []
        # Add the current index to the list of indices for this cumulative sum
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
