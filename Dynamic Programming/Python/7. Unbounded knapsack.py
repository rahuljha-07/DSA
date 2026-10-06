t = []


# Unbounded Knapsack: Top-Down Approach
def unboundedKnapsack(wt, val, W, n):
    # Base case: if no items are left or capacity is 0
    if n == 0 or W == 0:
        return 0
    # Check if the result is already computed
    if t[n][W] != -1:
        return t[n][W]
    # If the weight of the nth item is less than or equal to the remaining capacity
    if wt[n - 1] <= W:
        t[n][W] = max(
            val[n - 1] + unboundedKnapsack(wt, val, W - wt[n - 1], n),
            # Exclude the item
            unboundedKnapsack(wt, val, W, n - 1),
        )
    else:
        # If the weight of the nth item exceeds the remaining capacity, exclude it
        t[n][W] = unboundedKnapsack(wt, val, W, n - 1)
    return t[n][W]


# Unbounded Knapsack: Bottom-Up Approach
def unboundedKnapsackBottomUp(wt, val, W, n):
    # Create a DP table to store results of subproblems
    t = [[0] * (W + 1) for _ in range(n + 1)]
    # Initialize the table for base cases:
    # When either the number of items (n) or capacity (W) is 0, the maximum value is 0
    # Fill the table iteratively
    # Loop through items
    for i in range(1, n + 1):
        # Loop through capacities
        for j in range(1, W + 1):
            if wt[i - 1] <= j:
                t[i][j] = max(val[i - 1] + t[i][j - wt[i - 1]], t[i - 1][j])
            else:
                # If the weight of the item exceeds the current capacity, exclude it
                t[i][j] = t[i - 1][j]
    # Return the maximum value for the given weight capacity and all items
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
