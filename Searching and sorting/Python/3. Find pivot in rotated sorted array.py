def findPivotInRotatedArray(arr):
    n = len(arr)
    start = 0
    end = n - 1

    while start <= end:
        mid = start + (end - start) // 2

        next = 0 if mid == n - 1 else mid + 1
        prev = n - 1 if mid == 0 else mid - 1

        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return mid

        if arr[start] <= arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


arr = [15, 18, 2, 3, 6, 12]
pivotIndex = findPivotInRotatedArray(arr)

if pivotIndex != -1:
    print("Pivot found at index:", pivotIndex, "value:", arr[pivotIndex])
else:
    print("Pivot not found.")


'''
Time Complexity: O(log n)

Reason:
The pivot is found using binary search. Each step discards one sorted half
of the current search range.

Space Complexity: O(1)

Reason:
Only start, end, mid, next, and prev variables are used.
'''
