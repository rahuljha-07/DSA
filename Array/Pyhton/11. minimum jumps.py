memo = []

def recursive_min_jumps(current_index, arr, n):
    # Already at the last element: no more jumps needed.
    if current_index >= n - 1:
        return 0

    # Return the stored answer if this position was already solved.
    if memo[current_index] != -1:
        return memo[current_index]

    # A zero means we cannot move forward from this position.
    if arr[current_index] == 0:
        memo[current_index] = float("inf")
        return memo[current_index]

    jumps = float("inf")  # Infinity represents an unreachable end.

    max_jump = arr[current_index]

    for step in range(1, max_jump + 1):
        # Stop when the next position is outside the array.
        if current_index + step >= n:
            break

        next_jumps = recursive_min_jumps(current_index + step, arr, n)

        if next_jumps != float("inf"):
            jumps = min(jumps, 1 + next_jumps)
            next_jumps = recursive_min_jumps(current_index + step, arr, n)

            if next_jumps != float("inf"):
                jumps = min(jumps, 1 + next_jumps)

    # Save the minimum jumps needed from this position.
    memo[current_index] = jumps
    return jumps


def min_jumps(arr):
    global memo

    n = len(arr)
    if n == 0:
        return -1

    # -1 means the answer for this index has not been calculated.
    memo = [-1] * n

    result = recursive_min_jumps(0, arr, n)
    return -1 if result == float("inf") else result


if __name__ == "__main__":
    arr = [2, 3, 1, 1, 4]

    print("Minimum jumps:", min_jumps(arr))  # 2
    # Path: index 0 -> index 1 -> index 4.

    print("Unreachable example:", min_jumps([1, 0, 2]))  # -1


# HOW IT WORKS
# From each index, try every possible next position.
# For each choice:
#   total jumps = 1 current jump + minimum jumps from the next position.
# Keep the smallest total and store it in memo.
#
# Memoization means saving answers so the same position is not
# fully calculated again when reached through a different path.
#
# float("inf") plays the role of INT_MAX in your C++ code.
# A single-element array returns 0 because we are already at the end.


# TIME COMPLEXITY: O(n²) WORST CASE
# Time complexity describes how work grows with input size n.
#
# Memoization lets us fully solve each index at most once.
# However, each index can still try many next positions.
#
# If every index can reach all later indices, total choices checked are:
#   (n - 1) + (n - 2) + ... + 1 = n(n - 1)/2.
#
# Ignoring constants and smaller terms gives O(n²).
# Memoization avoids repeated calculations, not the loop at each index.


# EXTRA SPACE COMPLEXITY: O(n)
# Space complexity measures additional memory beyond the input.
#
# Memo array: O(n).
# Recursion stack: O(n), since a path can advance one index at a time.
# Total: O(n) + O(n) = O(n).
#
# Python limits recursion depth, so very long paths can cause
# a RecursionError. An iterative approach avoids this limitation.