def find(arr, n, x):
    result = [-1, -1]

    # Binary search for the first occurrence of x
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            if mid == 0 or arr[mid - 1] != x:
                result[0] = mid
                break
            high = mid - 1

    # Binary search for the last occurrence of x
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            if mid == n - 1 or arr[mid + 1] != x:
                result[1] = mid
                break
            low = mid + 1

    return result


arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(find(arr, len(arr), x))


'''
Time Complexity: O(log n)

Reason:
Two binary searches are performed: one for the first occurrence and one
for the last occurrence. Each binary search halves the search range.

Space Complexity: O(1)

Reason:
Only low, high, mid, and the fixed-size result list are used.
'''
