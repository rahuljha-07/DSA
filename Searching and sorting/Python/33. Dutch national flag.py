def dutchNationalFlag(arr):
    # Pointer for the next position of the first value
    low = 0
    # Pointer for the current element being checked
    mid = 0
    # Pointer for the next position of the third value
    high = len(arr) - 1

    # Iterate until mid pointer crosses high pointer
    while mid <= high:
        if arr[mid] == 0:
            # Swap arr[low] and arr[mid], increment both low and mid
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            # Just increment mid
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            # Swap arr[mid] and arr[high], decrement high
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
