def findPivotInRotatedArray(arr):
    n = len(arr)
    start = 0
    end = n - 1

    # Loop until the start pointer crosses the end pointer
    while start <= end:
        # Calculate mid-point of the current segment
        mid = start + (end - start) // 2

        # Calculate the indices for the next and previous elements in a circular manner
        next = 0 if mid == n - 1 else mid + 1
        prev = n - 1 if mid == 0 else mid - 1

        # Check if the mid element is less than or equal to both its next and previous
        # elements
        # If true, mid is the pivot (minimum element) in the rotated array
        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            # Pivot found at index 'mid'
            return mid

        # If the left part of the array is sorted, move to the right part
        if arr[start] <= arr[mid]:
            start = mid + 1
        else:
            # If the right part of the array is sorted, move to the left part
            end = mid - 1

    # Pivot not found, though it should exist in a rotated sorted array
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
