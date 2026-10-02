def mergeSortedArrays(arr1, arr2):
    mergedArray = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            mergedArray.append(arr1[i])
            i += 1
        else:
            mergedArray.append(arr2[j])
            j += 1

    while i < len(arr1):
        mergedArray.append(arr1[i])
        i += 1

    while j < len(arr2):
        mergedArray.append(arr2[j])
        j += 1

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
