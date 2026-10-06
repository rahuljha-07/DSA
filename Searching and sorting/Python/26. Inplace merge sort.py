# Function to merge two sorted halves of the array in place
def mergeInPlace(arr, left, mid, right):
    start1 = left
    start2 = mid + 1

    # Iterate through both halves
    while start1 <= mid and start2 <= right:
        # If the current element in the first half is in the correct position
        if arr[start1] <= arr[start2]:
            start1 += 1
        else:
            # Element in the second half is smaller, shift the first half
            value = arr[start2]
            index = start2

            # Shift all elements in the first half to the right
            while index != start1:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start1] = value

            # Update all pointers
            start1 += 1
            mid += 1
            start2 += 1


# In-place merge sort function
def mergeSort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2

        # Recursively sort the first half
        mergeSort(arr, left, mid)
        # Recursively sort the second half
        mergeSort(arr, mid + 1, right)
        # Merge the two halves in place
        mergeInPlace(arr, left, mid, right)


arr = [56, 2, 45]

print("Original array:", end=" ")
for num in arr:
    print(num, end=" ")
print()

mergeSort(arr, 0, len(arr) - 1)

print("Sorted array:", end=" ")
for num in arr:
    print(num, end=" ")
print()


'''
Time Complexity: O(n^2)

Reason:
Merge sort creates O(log n) levels, but this in-place merge can shift many
elements for each insertion. Across merges, the shifting can make the worst
case quadratic.

Space Complexity: O(log n)

Reason:
No merge arrays are created, but recursive mergeSort uses call stack space.
'''
