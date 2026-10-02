t = []


def unboundedKnapsack(wt, val, W, n):
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    if wt[n - 1] <= W:
        t[n][W] = max(
            val[n - 1] + unboundedKnapsack(wt, val, W - wt[n - 1], n),
            unboundedKnapsack(wt, val, W, n - 1),
        )
    else:
        t[n][W] = unboundedKnapsack(wt, val, W, n - 1)
    return t[n][W]


def unboundedKnapsackBottomUp(wt, val, W, n):
    t = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if wt[i - 1] <= j:
                t[i][j] = max(val[i - 1] + t[i][j - wt[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]
    return t[n][W]


def main():
    wt = [1, 3, 4, 5]
    val = [10, 40, 50, 70]
    W = 8
    n = len(wt)
    t[:] = [[-1] * (W + 1) for _ in range(n + 1)]
    print("Maximum value in the knapsack (Top-Down) =", unboundedKnapsack(wt, val, W, n))


if __name__ == "__main__":
    main()


'''
Let n be item types, W integer capacity, and a the smallest positive weight.
Time: O((n+1)*(W+1)): each item-count/capacity state is solved once;
including an item stays on the same row because items can be reused.
Space: O((n+1)*(W+1)) table; recursion additionally uses O(n+W/a) stack.
Initialize/reset global t to -1 for each new memoized input.
The alternate duplicate function is named unboundedKnapsackBottomUp.
'''
