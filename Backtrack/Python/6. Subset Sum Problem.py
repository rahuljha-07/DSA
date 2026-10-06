# Function to check if there exists a subset with the given sum
def subsetHelper(dp, arr, n, sum):
    # Base cases
    # Sum of 0 can always be achieved with an empty subset
    if sum == 0:
        return True
    # If no elements are left, we cannot achieve any non-zero sum
    if n == 0:
        return False
    # If already computed, return the value from memoization table
    if dp[n][sum] != -1:
        return dp[n][sum]
    # If the current element is less than or equal to the target sum
    if arr[n - 1] <= sum:
        # Exclude the current element
        dp[n][sum] = (subsetHelper(dp, arr, n - 1, sum - arr[n - 1])
                      or subsetHelper(dp, arr, n - 1, sum))
    else:
        dp[n][sum] = subsetHelper(dp, arr, n - 1, sum)
    return dp[n][sum]


# bottom up approach
def subsetSumPartition(n, arr, sum):
    # Initialize a 2D dp array with -1 (indicating uncomputed states)
    dp = [[-1] * (sum + 1) for _ in range(n + 1)]
    # Call the recursive helper function
    return subsetHelper(dp, arr, n, sum)


# top down approach
def subsetSumTopDown(arr, n, sum):
    # Create a DP table to store solutions to subproblems
    t = [[False] * (sum + 1) for _ in range(n + 1)]
    # Initialize the DP table
    # If the sum is 0, it is always possible to achieve it with an empty subset
    for i in range(n + 1):
        t[i][0] = True
    # If no elements are available and sum > 0, it is not possible to achieve the sum
    for j in range(1, sum + 1):
        t[0][j] = False
    # Fill the table iteratively
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            # If the current element can be included (arr[i-1] <= j)
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                # Exclude the element
                t[i][j] = t[i - 1][j]
    # The final answer is stored in t[n][sum]
    return t[n][sum]


def main():
    arr = [2, 3, 7, 8, 10]
    n = len(arr)
    sum = 11
    print("Subset with the given sum exists." if subsetSumPartition(n, arr, sum)
          else "Subset with the given sum does not exist.")


if __name__ == "__main__":
    main()


'''
Let n be element count and S the nonnegative target sum.
Time: O((n+1)*(S+1)) for both: allocate the full table, then compute at
most one constant-time result per (item count, remaining sum) state.
Space: O((n+1)*(S+1)) auxiliary table; memoized recursion adds O(n) stack.
Despite its source name, subsetSumTopDown is bottom-up tabulation.
These are pseudo-polynomial bounds; array values must be nonnegative.
'''
