def findTwoElement(arr, n):
    arr = list(arr)
    # Create a list to hold the result
    # To store the repeating and missing elements
    ans = [0, 0]

    # Rearrange the array elements to their corresponding indices
    i = 0
    while i < n:
        # Check if the current element is not in the correct position
        if arr[i] != arr[arr[i] - 1]:
            # Swap the element with the element at its correct index
            index = arr[i] - 1
            arr[i], arr[index] = arr[index], arr[i]
        else:
            # Move to the next element if the current one is in the correct position
            i += 1

    # Find the repeating and missing elements
    for i in range(n):
        # Check if the current element is not equal to its expected value (i + 1)
        if arr[i] != i + 1:
            # The repeating element
            ans[0] = arr[i]
            # The missing element
            ans[1] = i + 1
            # No need to continue searching
            break

    # Return the result list containing the repeating and missing elements
    return ans


arr = [1, 3, 3]
print(findTwoElement(arr, len(arr)))


'''
Time Complexity: O(n)

Reason:
The cyclic placement loop moves values toward their correct indexes.
Although it has swaps, each successful swap places at least one value
closer to its correct position. The final scan is also O(n).

Space Complexity: O(n)

Reason:
A local copy of n elements preserves C++'s pass-by-value behavior. The copy
is rearranged in place; the indexes and fixed-size answer use O(1) more space.
'''
