# Function to find a pair in the list with a given difference
def findPair(arr, targetDiff):
    # Sort the list to use the two-pointer technique
    arr.sort()

    # Left pointer
    leftIndex = 0
    # Right pointer
    rightIndex = 1

    # Iterate until left and right pointers are within bounds
    while leftIndex < len(arr) and rightIndex < len(arr):
        # Calculate the current difference
        currentDiff = arr[rightIndex] - arr[leftIndex]

        # Check if the current difference matches the target difference
        if currentDiff == targetDiff and leftIndex != rightIndex:
            # Found a pair with the specified difference
            return True
        # If the current difference is less than the target difference, move the right
        # pointer to the right
        elif currentDiff < targetDiff:
            rightIndex += 1
        # If the current difference is greater than the target difference, move the left
        # pointer to the right
        else:
            leftIndex += 1

            if leftIndex == rightIndex:
                rightIndex += 1

    # No pair found with the specified difference
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
