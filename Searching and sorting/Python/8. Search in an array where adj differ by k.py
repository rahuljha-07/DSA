def searchInStepArray(arr, k, x):
    n = len(arr)
    i = 0

    # Iterate through the array
    while i < n:
        # Check if the current element is equal to the key
        if arr[i] == x:
            # Return the index if found
            return i

        # Calculate the difference between the current element and the key
        diff = abs(arr[i] - x)
        # Move to the next index based on the step property
        # We can skip ahead by the difference divided by k
        # and move to the right index without skipping possible matches
        # Ensure we move at least on e step forward
        i += max(1, diff // k)

    # If the key is not found, return -1
    return -1


arr1 = [4, 5, 6, 7, 6]
k1 = 1
x1 = 6
print("Index of", x1, "in arr1:", searchInStepArray(arr1, k1, x1))

arr2 = [20, 40, 50, 70, 70, 60]
k2 = 20
x2 = 60
print("Index of", x2, "in arr2:", searchInStepArray(arr2, k2, x2))


'''
Time Complexity: O(n) worst case

Reason:
The index jumps by at least 1 each iteration, so in the worst case it may
still visit every element. Larger jumps can make it faster in practice.

Space Complexity: O(1)

Reason:
Only n, i, and diff variables are used.
'''
