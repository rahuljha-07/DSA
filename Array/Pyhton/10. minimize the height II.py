def get_min_diff(arr, k):
    n = len(arr)
    if n <= 1:
        return 0

    arr.sort()

    result = arr[n - 1] - arr[0]
    smallest = arr[0] + k
    largest = arr[n - 1] - k

    for i in range(n - 1):
        # Increase towers up to i; decrease towers after i.
        min_height = min(smallest, arr[i + 1] - k)
        max_height = max(largest, arr[i] + k)

        # Skip adjustments that produce a negative height.
        if min_height < 0:
            continue

        result = min(result, max_height - min_height)

    return result


arr = [1, 5, 8, 10]
k = 2
print(get_min_diff(arr, k))  # 5


# TIME: O(n log n)
# Sorting: O(n log n).
# Loop: n - 1 iterations with O(1) work each = O(n).
# Total: O(n log n) + O(n) = O(n log n).
#
# EXTRA SPACE: O(n) worst case.
# Variables use O(1), but Python's sort may use O(n) temporary memory.