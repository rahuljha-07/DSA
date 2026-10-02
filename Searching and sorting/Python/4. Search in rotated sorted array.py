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


def binarySearch(arr, start, end, target):
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def searchInRotatedArray(arr, target):
    n = len(arr)
    pivot = findPivotInRotatedArray(arr)

    if pivot == -1:
        return binarySearch(arr, 0, n - 1, target)

    if arr[pivot] == target:
        return pivot

    if pivot > 0 and target >= arr[0] and target <= arr[pivot - 1]:
        return binarySearch(arr, 0, pivot - 1, target)
    else:
        return binarySearch(arr, pivot, n - 1, target)


arr = [15, 18, 2, 3, 6, 12]
target = 3

index = searchInRotatedArray(arr, target)
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found in the array.")


'''
Time Complexity: O(log n)

Reason:
First, binary search is used to find the pivot. Then one more binary search
is performed on the correct sorted half of the array.

Space Complexity: O(1)

Reason:
Only a fixed number of index variables are used.
'''
