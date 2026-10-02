def valueEqualToIndex(arr, n):
    ans = []

    # Loop through the array to check each element
    for i in range(n):
        # Since it is 1-based indexing, compare arr[i] with i + 1
        if arr[i] == i + 1:
            ans.append(arr[i])

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
