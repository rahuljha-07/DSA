# Function to solve the game optimally for the given subarray from i to j using memoization
def solve(i, j, a, dp):
    if i > j:
        return 0
    # Base case: If there is only one coin left, return its value
    if i == j:
        return a[i]
    # Check if the value is already computed (memoization)
    if dp[i][j] is not None:
        return dp[i][j]
    # Take the first coin; an optimal opponent leaves us the worse continuation.
    take_first = a[i] + min(solve(i + 2, j, a, dp), solve(i + 1, j - 1, a, dp))
    # Or take the last coin, again assuming the opponent leaves us the worse option.
    take_last = a[j] + min(solve(i + 1, j - 1, a, dp), solve(i, j - 2, a, dp))
    # Store the result in dp[i][j] to avoid redundant computations
    dp[i][j] = max(take_first, take_last)
    return dp[i][j]


# Wrapper function to start solving the game from the whole array
def maxAmount(n, a):
    # None marks an uncomputed interval; a computed winning amount may be negative.
    dp = [[None] * n for _ in range(n)]
    # Call the recursive solve function starting from the whole array (0 to n-1)
    return solve(0, n - 1, a, dp)


def main():
    arr = [8, 15, 3, 7]
    n = len(arr)
    print("Maximum amount that can be won:", maxAmount(n, arr))


if __name__ == "__main__":
    main()


'''
Let n be the coin count.
Time: O(n^2): at most n*n interval states, each with a constant number
of endpoint choices/opponent responses. Memoization avoids repeated games.
Space: O(n^2) memo table plus O(n) recursive depth.
The missing i>j base case is added so even-length games terminate safely.
None distinguishes uncomputed states from valid negative winnings.
'''
