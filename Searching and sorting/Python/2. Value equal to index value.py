def valueEqualToIndex(arr, n):
    # Initialize an empty list to store the result
    ans = []

    # Loop through the array to check each element
    for i in range(n):
        # Since it is 1-based indexing, compare arr[i] with i + 1
        if arr[i] == i + 1:
            # If element matches its index value, add it to the result
            ans.append(arr[i])

    # Return the list containing elements that matched their indices
    return ans


arr = [15, 2, 45, 4, 7]
print(valueEqualToIndex(arr, len(arr)))


'''
Time Complexity: O(n)

Reason:
The loop checks every array element once and compares it with its 1-based
index value.

Space Complexity: O(1), excluding output

Reason:
Only loop variables are used. The ans list stores the required output.
'''
