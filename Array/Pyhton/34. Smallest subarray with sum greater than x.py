def sb(arr, n, x):
    # Assumes nonnegative array values and x >= 0.
    i = 0
    j = 0
    sum = 0
    sz = float("inf")

    while j < n:
        while sum <= x and j < n:
            sum += arr[j]
            j += 1

        while sum > x and i < n:
            sz = min(sz, j - i)
            sum -= arr[i]
            i += 1

    return sz  # Returns infinity if no subarray has sum > x.


arr = [1, 4, 45, 6, 0, 19]
x = 51
print(sb(arr, len(arr), x))  # 3


# TIME: O(n)
# i and j each move forward at most n times.
# Despite nested loops, total pointer movement is O(n).
#
# EXTRA SPACE: O(1)
# Only a fixed number of variables are used.