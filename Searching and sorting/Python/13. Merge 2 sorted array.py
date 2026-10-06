def mergeSortedArrays(arr1, arr2):
    # To store the merged result
    mergedArray = []
    # Pointer for arr1
    i = 0
    # Pointer for arr2
    j = 0

    # Loop until we reach the end of either array
    while i < len(arr1) and j < len(arr2):
        # Compare elements at both pointers
        if arr1[i] <= arr2[j]:
            # Add smaller element to mergedArray
            mergedArray.append(arr1[i])
            # Move the pointer in arr1
            i += 1
        else:
            mergedArray.append(arr2[j])
            # Move the pointer in arr2
            j += 1

    # If any elements are left in arr1, add them to mergedArray
    while i < len(arr1):
        mergedArray.append(arr1[i])
        i += 1

    # If any elements are left in arr2, add them to mergedArray
    while j < len(arr2):
        mergedArray.append(arr2[j])
        j += 1

    # Return the merged sorted array
    return mergedArray


arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]

merged = mergeSortedArrays(arr1, arr2)
print("Merged Array:", end=" ")
for num in merged:
    print(num, end=" ")
print()


'''
Time Complexity: O(n + m)

Reason:
Each element from both sorted arrays is copied into the result exactly once.
The two pointers only move forward.

Space Complexity: O(n + m)

Reason:
The mergedArray list stores all elements from arr1 and arr2.
'''
