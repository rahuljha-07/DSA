def dutchNationalFlag(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


arr = [2, 0, 2, 1, 1, 0]
dutchNationalFlag(arr)

for i in arr:
    print(i, end=" ")
print()


'''
Time Complexity: O(n)

Reason:
Each step moves mid forward or high backward, shrinking the unknown region.
Every element is processed a constant number of times.

Space Complexity: O(1)

Reason:
Sorting is done in place with low, mid, and high pointers.
'''
