t = []


def knapsack(wt, val, W, n):
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    if wt[n - 1] <= W:
        t[n][W] = max(
            val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1),
            knapsack(wt, val, W, n - 1),
        )
    else:
        t[n][W] = knapsack(wt, val, W, n - 1)
    return t[n][W]


def knapSack(w, wt, val, n):
    t = [[0] * (w + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if wt[i - 1] <= j:
                t[i][j] = max(val[i - 1] + t[i - 1][j - wt[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]
    return t[n][w]


def main():
    wt = [1, 3, 4, 5]
    val = [1, 4, 5, 7]
    W = 7
    n = len(wt)
    t[:] = [[-1] * (W + 1) for _ in range(n + 1)]
    print("Maximum value in the knapsack =", knapsack(wt, val, W, n))


if __name__ == "__main__":
    main()


'''
Let n be items and W the capacity, with positive integer weights.
Time: O((n+1)*(W+1)) for either method: at most n*W include/exclude
states, each O(1), plus table allocation. This is pseudo-polynomial in W.
Space: O((n+1)*(W+1)) table; memoized recursion also needs O(n) stack.
Initialize/reset global t to -1 for each new knapsack input.
The source's memoized and iterative implementations are both retained.
'''
