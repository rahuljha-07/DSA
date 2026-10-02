def threeWayPartition(arr, pivot):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] < pivot:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] > pivot:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1


arr = [3, 5, 2, 3, 7, 3, 1, 4]
pivot = 3

threeWayPartition(arr, pivot)

for i in arr:
    print(i, end=" ")
print()


'''
Time Complexity: O(n)

Reason:
The Dutch National Flag pointers shrink the unprocessed region each step.
Each element is inspected a constant number of times.

Space Complexity: O(1)

Reason:
Partitioning is done in place with low, mid, and high pointers.
'''
