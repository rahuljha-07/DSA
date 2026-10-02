D = 1000
t = [[-1.0] * D for _ in range(D)]


def Knapsack(wt, val, W, n):
    if n == 0 or W == 0:
        return 0.0
    if t[n][W] != -1:
        return t[n][W]
    else:
        if wt[n - 1] <= W:
            includeFull = val[n - 1] + Knapsack(wt, val, W - wt[n - 1], n - 1)
            excludeItem = Knapsack(wt, val, W, n - 1)
            t[n][W] = max(includeFull, excludeItem)
        else:
            includeFraction = val[n - 1] * (W / wt[n - 1])
            exclude = Knapsack(wt, val, W, n - 1)
            t[n][W] = max(includeFraction, exclude)
        return t[n][W]


def main():
    for row in t:
        row[:] = [-1.0] * D
    wt = [10, 20, 30]
    val = [60, 100, 120]
    W = 50
    n = len(wt)
    maxValue = Knapsack(wt, val, W, n)
    print("Maximum value in Knapsack =", maxValue)


if __name__ == "__main__":
    main()


'''
Let n be items, W integer capacity, and D=1000 the fixed table dimension.
Time: O(n*W) memoized state work; initializing/resetting all t costs O(D^2).
Space: O(D^2) global table plus O(n) recursive depth; requires n,W<D,
positive integer weights, and nonnegative values. Reset t for new inputs.
The source's memoized recurrence is retained, NOT replaced by ratio sorting.
It only considers a fraction when an item exceeds remaining capacity and
is therefore not a correct general fractional-knapsack solver. For example,
wt=[2,2], val=[3,2], W=3 yields 3.5 although the optimum is 4.
Python initializes real -1.0 values rather than C++'s invalid double memset.
'''
