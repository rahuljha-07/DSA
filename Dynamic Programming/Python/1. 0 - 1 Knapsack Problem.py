t = []


# bottom up
def knapsack(wt, val, W, n):
    # Base case: if no items are left or capacity is 0
    if n == 0 or W == 0:
        return 0
    # Check if the result is already computed (memoization)
    if t[n][W] != -1:
        return t[n][W]
    # If the weight of the nth item is less than or equal to the remaining capacity
    if wt[n - 1] <= W:
        t[n][W] = max(
            val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1),
            # Exclude the item
            knapsack(wt, val, W, n - 1),
        )
    else:
        # If the weight of the nth item exceeds the remaining capacity, exclude it
        t[n][W] = knapsack(wt, val, W, n - 1)
    return t[n][W]


# top down
def knapSack(w, wt, val, n):
    # Create a DP table to store results of subproblems
    t = [[0] * (w + 1) for _ in range(n + 1)]
    # Initialize the table for base cases:
    # When either the number of items (n) or capacity (w) is 0, the maximum value is 0
    # Fill the table iteratively
    # Loop through items
    for i in range(1, n + 1):
        # Loop through capacities
        for j in range(1, w + 1):
            if wt[i - 1] <= j:
                t[i][j] = max(val[i - 1] + t[i - 1][j - wt[i - 1]], t[i - 1][j])
            else:
                # If the weight of the current item is less than or equal to capacity
                # Take the maximum of including or excluding the current item
                # If the weight of the current item exceeds the current capacity, exclude it
                t[i][j] = t[i - 1][j]
    # Return the maximum value for the given weight capacity and all items
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
