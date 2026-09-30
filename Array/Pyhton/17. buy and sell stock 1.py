def max_profit(prices):
    n = len(prices)

    # At least two days are needed to buy and then sell.
    if n < 2:
        return 0

    sell_price = prices[n - 1]
    profit = 0

    # Scan from the second-last day back to the first day.
    for i in range(n - 2, -1, -1):
        # Keep the highest price seen while scanning from the right.
        if prices[i] > sell_price:
            sell_price = prices[i]

        profit = max(profit, sell_price - prices[i])

    return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]

    print("Maximum profit:", max_profit(prices))
    # Output: Maximum profit: 5
    # Buy at 1 and sell later at 6.

    print(max_profit([7, 6, 4, 3, 1]))  # 0 — prices only decrease.


# ---------------------------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------------------------
# Scan backward so we know the best selling price available to the right.
# Treat each current price as a possible buying price.
#
# Example: [7, 1, 5, 3, 6, 4]
# Initially: sell_price = 4, profit = 0.
#
# Current price 6: sell_price becomes 6; candidate = 0; profit = 0.
# Current price 3: sell_price stays 6;   candidate = 3; profit = 3.
# Current price 5: sell_price stays 6;   candidate = 1; profit = 3.
# Current price 1: sell_price stays 6;   candidate = 5; profit = 5.
# Current price 7: sell_price becomes 7; candidate = 0; profit = 5.
#
# Answer: 5.
#
# Why is updating sell_price before calculating profit okay?
# If the current price becomes the new maximum, the candidate is 0.
# This represents no profitable trade, not an actual same-day transaction.
# Every positive candidate uses a selling price from a later day.
#
# We cannot simply subtract the array's minimum from its maximum:
# the buying day must come BEFORE the selling day.
#
# The input list is not modified.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n)
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with the number of prices n.
#
# The loop runs n - 1 times.
# Each iteration performs a fixed number of comparisons and calculations.
#
# Total work = (n - 1) × O(1) = O(n).
# Best, average, and worst-case time are O(n) for n >= 2.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(1)
# ---------------------------------------------------------------------------
# Extra space measures additional memory beyond the input list.
#
# Only a fixed number of variables are used.
# No additional list or recursion is needed.
#
# Therefore, extra space is O(1).