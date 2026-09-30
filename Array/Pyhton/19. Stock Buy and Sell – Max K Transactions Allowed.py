def max_profit(k, prices):
    n = len(prices)
    if n < 2 or k <= 0:
        return 0

    # dp[t][d] = maximum profit using at most t transactions
    # during days 0 through d, with no stock held at the end.
    dp = [[0] * n for _ in range(k + 1)]
    # another way of writing
    # dp = []
    # for row in range(k + 1):
    #     dp.append([0] * n)
    for t in range(1, k + 1):
        max_val = float("-inf")

        for d in range(1, n):
            # Consider day d - 1 as a possible buying day.
            # Keep the best: previous profit minus buying cost.
            candidate = dp[t - 1][d - 1] - prices[d - 1]
            if candidate > max_val:
                max_val = candidate

            # Either sell today or keep the best profit from yesterday.
            if max_val + prices[d] > dp[t][d - 1]:
                dp[t][d] = max_val + prices[d]
            else:
                dp[t][d] = dp[t][d - 1]

    return dp[k][n - 1]


if __name__ == "__main__":
    n = int(input("Enter number of days: "))
    prices = list(map(int, input("Enter stock prices: ").split()))

    if n < 0 or len(prices) != n:
        raise ValueError("Enter exactly n stock prices.")

    k = int(input("Enter max transactions allowed: "))

    print("Maximum Profit:", max_profit(k, prices))

    # Example input:
    # Enter number of days: 6
    # Enter stock prices: 3 2 6 5 0 3
    # Enter max transactions allowed: 2
    #
    # Output:
    # Maximum Profit: 7
    #
    # Buy at 2, sell at 6 -> profit 4.
    # Buy at 0, sell at 3 -> profit 3.
    # Total = 7.


# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
# dp[t][d] stores the best profit by day d using AT MOST t transactions.
#
# Base cases:
# dp[0][d] = 0: no transactions allowed.
# dp[t][0] = 0: one day alone cannot produce a profitable transaction.
#
# On each day d, choose between:
#
# 1. Do not sell today:
#    Keep dp[t][d - 1].
#
# 2. Sell today:
#    For a buying day b < d, the combined profit would be:
#    dp[t - 1][b] + prices[d] - prices[b].
#
#    Rearranging:
#    prices[d] + (dp[t - 1][b] - prices[b]).
#
# max_val keeps the largest bracketed value across buying days seen so far.
# Therefore:
# dp[t][d] = max(dp[t][d - 1], prices[d] + max_val).
#
# Why update max_val using day d - 1?
# That is the newest eligible buying day before today's selling day.
# Older buying days are already represented in max_val.
#
# Example with one transaction and prices [3, 2, 6]:
# Day 1:
# max_val = max(-infinity, 0 - 3) = -3.
# Selling at 2 gives -1, so keep profit 0.
#
# Day 2:
# max_val = max(-3, 0 - 2) = -2.
# Selling at 6 gives 4, so store profit 4.
#
# max_val is reset for each transaction count because the previous
# profit row changes.
#
# A previous sale and the next purchase may share a day in this recurrence.
# At the same price, they provide no extra gain and can be combined into
# one transaction. This is valid for the standard problem with no cooldown.
#
# Python note:
# [[0] * n for _ in range(k + 1)] creates independent rows.
# Do NOT use [[0] * n] * (k + 1), which repeats references to the same row.
#
# The original prices list is not modified.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(k * n)
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with the input sizes.
# Here, n is the number of days and k is the transaction limit.
#
# Creating the table takes O((k + 1) * n).
# The outer loop runs k times.
# For EACH outer iteration, the inner loop runs n - 1 times.
# Each inner iteration performs O(1) work.
#
# These loops are nested, so MULTIPLY:
# k * (n - 1) * O(1) = O(k * n), for k >= 1.
#
# Without max_val, checking every previous buying day for every cell
# would take O(k * n²). Keeping a running maximum avoids that extra loop.
#
# Inputs with fewer than two days or k <= 0 return in O(1) time.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(k * n)
# ---------------------------------------------------------------------------
# The table has k + 1 rows and n columns.
# It stores (k + 1) * n values -> O(k * n), for k >= 1.
#
# Other variables use O(1) additional space.
# No recursion is used.