# code uses logic of dutch national flag
def threeWayPartition(arr, pivot):
    # Pointer for the next position of elements less than pivot
    low = 0
    # Pointer for the current element being checked
    mid = 0
    # Pointer for the next position of elements greater than pivot
    high = len(arr) - 1

    # Iterate until mid pointer crosses high pointer
    while mid <= high:
        if arr[mid] < pivot:
            # Swap arr[low] and arr[mid], increment both low and mid
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] > pivot:
            # Swap arr[mid] and arr[high], decrement high
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            # Just increment mid
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
