def max_profit(price):
    n = len(price)
    if n < 2:
        return 0

    profit = [0] * n

    # First pass: best single-transaction profit from each day to the end.
    max_price = price[n - 1]

    for i in range(n - 2, -1, -1):
        if price[i] > max_price:
            max_price = price[i]

        profit[i] = max(profit[i + 1], max_price - price[i])

    # Second pass: combine an earlier transaction with a later one.
    min_price = price[0]

    for i in range(1, n):
        if price[i] < min_price:
            min_price = price[i]

        # profit[i] still holds the best single transaction from i onward.
        # price[i] - min_price is the best first transaction ending today.
        # profit[i - 1] holds the best combined answer found so far.
        profit[i] = max(
            profit[i - 1],
            profit[i] + (price[i] - min_price)
        )

    return profit[n - 1]


if __name__ == "__main__":
    price = [10, 22, 5, 75, 65, 80]

    print("Maximum profit:", max_profit(price))
    # Output: Maximum profit: 87
    # First transaction:  buy at 10, sell at 22 -> profit 12.
    # Second transaction: buy at 5, sell at 80  -> profit 75.
    # Total = 12 + 75 = 87.


# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
# First pass: scan backward.
#
# profit[i] stores the best profit from ONE transaction using days i onward.
# We choose between:
# - Skipping today's buying opportunity: profit[i + 1].
# - Buying today and selling at the highest later price: max_price - price[i].
#
# For [10, 22, 5, 75, 65, 80], after the first pass:
# profit = [75, 75, 75, 15, 15, 0].
#
# Second pass: scan forward and use each day as a dividing point.
#
# Earlier transaction:
# Buy at the lowest price seen so far and sell on day i.
# Its profit is price[i] - min_price.
#
# Later transaction:
# The existing profit[i] gives the best single transaction from day i onward.
#
# Add these two profits and compare with the best answer already found.
#
# Example at i = 1, where price[i] = 22:
# First transaction profit  = 22 - 10 = 12.
# Later transaction profit  = profit[1] = 75.
# Combined profit          = 12 + 75 = 87.
#
# The two passes allow a first sale and second purchase on the same day.
# At the same price, those actions cancel out and provide no extra profit.
# We never need to hold two stocks simultaneously.
#
# After the second pass, profit no longer means only "best suffix profit":
# its entries have been overwritten with the best combined answers.
#
# Decreasing prices return 0 because making no transaction is allowed.
# The original price list is not modified.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n)
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with the number of days n.
#
# Creating profit: O(n).
# Backward loop: n - 1 iterations, O(1) work each -> O(n).
# Forward loop:  n - 1 iterations, O(1) work each -> O(n).
#
# These steps run sequentially, so ADD their costs:
# O(n) + O(n) + O(n) = O(n).
#
# Two separate loops do not make this O(n²).


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(n)
# ---------------------------------------------------------------------------
# Extra space measures additional memory beyond the input list.
#
# The profit list stores n values -> O(n).
# All other variables use O(1) space.
#
# Total extra space: O(n) + O(1) = O(n).