# Function to find and print all subarrays with sum zero
def printAllSubarraysWithZeroSum(arr, n):
    # Map to store the cumulative sum and the indices where it appears
    sumMap = {}

    # Initialize the cumulative sum and add a base case for sum = 0
    sum = 0
    # For subarrays starting from index 0
    sumMap[0] = [-1]

    # Iterate over the array
    for i in range(n):
        # Add the current element to the cumulative sum
        sum += arr[i]

        if sum in sumMap:
            # If found, it means there's a subarray with a sum of zero
            for startIdx in sumMap[sum]:
                print("Subarray with zero sum found from index", startIdx + 1, "to", i)

        if sum not in sumMap:
            sumMap[sum] = []
        # Store the current index in the sum map
        sumMap[sum].append(i)


arr = [3, 4, -7, 1, 3, 3, 1, -4]
print("All subarrays with zero sum are:")
printAllSubarraysWithZeroSum(arr, len(arr))


'''
Time Complexity: O(n + z)

Reason:
The array is scanned once. Whenever a prefix sum repeats, all earlier
indices for that sum are printed. z is the number of printed zero-sum subarrays.

Space Complexity: O(n)

Reason:
The map can store every prefix sum index in the worst case.
'''
