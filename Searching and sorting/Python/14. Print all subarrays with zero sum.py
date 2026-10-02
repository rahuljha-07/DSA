def printAllSubarraysWithZeroSum(arr, n):
    sumMap = {}

    sum = 0
    sumMap[0] = [-1]

    for i in range(n):
        sum += arr[i]

        if sum in sumMap:
            for startIdx in sumMap[sum]:
                print("Subarray with zero sum found from index", startIdx + 1, "to", i)

        if sum not in sumMap:
            sumMap[sum] = []
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
