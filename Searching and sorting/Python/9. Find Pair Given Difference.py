def findPair(arr, targetDiff):
    arr.sort()

    leftIndex = 0
    rightIndex = 1

    while leftIndex < len(arr) and rightIndex < len(arr):
        currentDiff = arr[rightIndex] - arr[leftIndex]

        if currentDiff == targetDiff and leftIndex != rightIndex:
            return True
        elif currentDiff < targetDiff:
            rightIndex += 1
        else:
            leftIndex += 1

            if leftIndex == rightIndex:
                rightIndex += 1

    return False


arr = [1, 5, 3, 4, 2]
targetDiff = 3

if findPair(arr, targetDiff):
    print("Pair found with the given difference.")
else:
    print("No pair found with the given difference.")


'''
Time Complexity: O(n log n)

Reason:
The array is sorted first, which takes O(n log n). The two-pointer scan is
linear, so sorting dominates.

Space Complexity: O(1) auxiliary

Reason:
The two-pointer part uses only indexes. Python sorting may use temporary
memory internally, but the algorithm itself does not create another array.
'''
