t = []


# Function to determine if a subset with sum `sum` exists
def subsetSum(arr, n, sum):
    # Base cases
    # Subset with sum 0 always exists (empty subset)
    if sum == 0:
        return True
    # No elements left, no subset can sum to > 0
    if n == 0:
        return False
    # If already computed, return the stored result
    if t[n][sum] != -1:
        return t[n][sum]
    # If the current element is smaller than the remaining sum, include or exclude the
    # current element
    if arr[n - 1] <= sum:
        t[n][sum] = subsetSum(arr, n - 1, sum - arr[n - 1]) or subsetSum(arr, n - 1, sum)
    else:
        # Otherwise, exclude it
        t[n][sum] = subsetSum(arr, n - 1, sum)
    return t[n][sum]


# bottom up
def subsetSumBottomUp(arr, n, sum):
    # Create a DP table `t` with dimensions (n+1) x (sum+1)
    t = [[False] * (sum + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        # No items => no subset for sum > 0
        t[i][0] = True
    # Fill the table iteratively
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                # Exclude the current element
                t[i][j] = t[i - 1][j]
    # The answer is in the bottom-right corner of the table
    return t[n][sum]


def main():
    arr = [3, 34, 4, 12, 5, 2]
    n = len(arr)
    sum = 9
    t[:] = [[-1] * (sum + 1) for _ in range(n + 1)]
    print(f"Subset with sum {sum} {'exists' if subsetSum(arr, n, sum) else 'does not exist'}.")


if __name__ == "__main__":
    main()


'''
Let n be the number of elements and S the target sum.
Time: O((n+1)*(S+1)): the table has (n+1)*(S+1) states and each state
uses at most two already-computed states in O(1) arithmetic work.
Space: O((n+1)*(S+1)) for the full 2D table; it is not compressed.
Assumes nonnegative array values and target. Arithmetic costs treat
stored counts/values as machine-sized; Python big integers can add cost.
Memoized subsetSum adds O(n) stack; initialize/reset global t to -1.
subsetSumBottomUp names the source's second, otherwise duplicate function.
'''
