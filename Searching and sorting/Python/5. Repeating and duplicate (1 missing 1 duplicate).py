def findTwoElement(arr, n):
    arr = list(arr)
    ans = [0, 0]

    # Rearrange the array elements to their corresponding indices
    i = 0
    while i < n:
        if arr[i] != arr[arr[i] - 1]:
            index = arr[i] - 1
            arr[i], arr[index] = arr[index], arr[i]
        else:
            i += 1

    # Find the repeating and missing elements
    for i in range(n):
        if arr[i] != i + 1:
            ans[0] = arr[i]
            ans[1] = i + 1
            break

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
