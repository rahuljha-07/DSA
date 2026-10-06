INT_MAX = float("inf")


# Helper function for recursion with memoization
def minimumCostHelper(w, cost, n, dp):
    # Base cases
    # No weight to fill, cost is 0
    if w == 0:
        return 0
    # No items left or invalid weight
    if n == 0 or w < 0:
        return INT_MAX
    # If already computed, return the stored value
    if dp[n][w] != -1:
        return dp[n][w]
    # Exclude the current packet
    exclude = minimumCostHelper(w, cost, n - 1, dp)
    include = INT_MAX
    # Only include if cost is valid and weight is sufficient
    if cost[n - 1] != -1 and w >= n:
        subProblem = minimumCostHelper(w - n, cost, n, dp)
        # Ensure the subproblem is solvable
        if subProblem != INT_MAX:
            include = cost[n - 1] + subProblem
    # Store the result in dp
    dp[n][w] = min(include, exclude)
    return dp[n][w]


def minimumCost(w, cost, n):
    # Create a memoization table initialized to -1
    dp = [[-1] * (w + 1) for _ in range(n + 1)]
    result = minimumCostHelper(w, cost, n, dp)
    # If the result is a large initial value, it means the weight cannot be achieved
    return -1 if result == INT_MAX else result


def main():
    cost1 = [20, 10, 4, 50, 100]
    n1 = 5
    w1 = 5
    print("Minimum cost:", minimumCost(w1, cost1, n1))
    cost2 = [-1, -1, 4, 3, -1]
    n2 = 5
    w2 = 5
    print("Minimum cost:", minimumCost(w2, cost2, n2))


if __name__ == "__main__":
    main()


'''
Let n be available packet sizes and w the required weight.
Time: O((n+1)*(w+1)): each packet-count/weight state is cached, considering
include and exclude once. Size n can be reused on the include branch.
Space: O((n+1)*(w+1)) memo table plus O(n+w) recursive depth.
cost[i] is the nonnegative price of weight i+1; -1 means unavailable.
Infinity replaces the bounded C++ impossible-cost sentinel.
'''
