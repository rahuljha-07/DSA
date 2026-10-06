import sys


# Recursive helper function with memoization
def minRemovalsHelper(left, right, arr, k, dp):
    # Base case: If the range is valid
    if left > right or arr[right] - arr[left] <= k:
        return 0
    # If already computed, return the stored value
    if dp[left][right] != -1:
        return dp[left][right]
    # Remove either the leftmost or the rightmost element
    removeLeft = minRemovalsHelper(left + 1, right, arr, k, dp)
    removeRight = minRemovalsHelper(left, right - 1, arr, k, dp)
    # Store and return the result
    dp[left][right] = 1 + min(removeLeft, removeRight)
    return dp[left][right]


def minRemovalsToSatisfyCondition(arr, k):
    n = len(arr)
    # Sort the array
    arr.sort()
    # Create a memoization table initialized to -1
    dp = [[-1] * n for _ in range(n)]
    # Call the recursive helper function
    return minRemovalsHelper(0, n - 1, arr, k, dp)


def main():
    tokens = iter(map(int, sys.stdin.read().split()))
    n = next(tokens)
    k = next(tokens)
    arr = [next(tokens) for _ in range(n)]
    print(minRemovalsToSatisfyCondition(arr, k))


if __name__ == "__main__":
    main()


'''
Let n be array length and k>=0 the allowed max-min difference.
Time: O(n log(n+1)+n^2): sort arr, then memoize at most O(n^2)
left/right intervals, each trying removal from either end in O(1) work.
Space: O(n^2+n) auxiliary table, recursion stack, and sorting workspace.
arr is sorted in place. Empty intervals return before endpoint access.
'''
