t = []


# Recursive function to solve MCM
def solve(arr, i, j):
    # Base case: If the chain has less than two matrices, no cost
    if i >= j:
        return 0
    # Check if the result is already computed in the memoization table
    if t[i][j] != -1:
        return t[i][j]
    ans = float("inf")
    # Try placing the parenthesis at every possible split point `k`
    for k in range(i, j):
        # Cost of multiplying matrices from i to k and k+1 to j
        temp = solve(arr, i, k) + solve(arr, k + 1, j) + arr[i - 1] * arr[k] * arr[j]
        # Update the minimum cost
        ans = min(ans, temp)
    # Store the result in the memoization table and return it
    t[i][j] = ans
    return ans


def main():
    arr = [40, 20, 30, 10, 30]
    n = len(arr)
    t[:] = [[-1] * n for _ in range(n)]
    result = solve(arr, 1, n - 1)
    print("Minimum number of multiplications is:", result)


if __name__ == "__main__":
    main()


'''
Let n be the number of dimensions (n-1 matrices), all positive.
Time: O(n^3): O(n^2) interval states, each trying up to n split points;
memoization ensures each interval is computed only once.
Space: O(n^2) global t plus O(n) recursion depth. Initialize/reset t
to -1 for each new dimension array, as main does.
'''
