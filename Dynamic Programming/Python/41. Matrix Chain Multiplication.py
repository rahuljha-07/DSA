t = []


def solve(arr, i, j):
    if i >= j:
        return 0
    if t[i][j] != -1:
        return t[i][j]
    ans = float("inf")
    for k in range(i, j):
        temp = solve(arr, i, k) + solve(arr, k + 1, j) + arr[i - 1] * arr[k] * arr[j]
        ans = min(ans, temp)
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
