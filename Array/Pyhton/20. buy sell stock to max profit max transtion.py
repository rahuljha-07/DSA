# selling and buying on the same day with any tranction to get max
def max_profit(prices):
    profit = 0

    for i in range(1, len(prices)):
        # Collect every increase between consecutive days.
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]

    print("Maximum profit:", max_profit(prices))
    # Output: Maximum profit: 7
    # Buy at 1, sell at 5 -> profit 4.
    # Buy at 3, sell at 6 -> profit 3.
    # Total = 7.


# ---------------------------------------------------------------------------
# HOW IT WORKS: GREEDY APPROACH
# ---------------------------------------------------------------------------
# With unlimited transactions, collect every positive daily price change.
# Ignore decreases because we do not need to hold stock through them.
#
# For [7, 1, 5, 3, 6, 4]:
# 7 -> 1: decrease, ignore.
# 1 -> 5: increase, add 4.
# 5 -> 3: decrease, ignore.
# 3 -> 6: increase, add 3.
# 6 -> 4: decrease, ignore.
# Total profit = 4 + 3 = 7.
#
# Why does adding consecutive increases work?
# For [1, 3, 5]:
# (3 - 1) + (5 - 3) = 5 - 1 = 4.
#
# Selling and buying again on the middle day gives the same profit
# as simply buying at 1 and holding until 5.
# Therefore, actual same-day selling and rebuying is not necessary.
#
# Every rising stretch can be handled as one buy followed by one sell.
# There is no transaction limit forcing us to skip a profitable stretch.
#
# Empty, single-element, and decreasing arrays return 0.
# The original list is not modified.


# ---------------------------------------------------------------------------
# TIME COMPLEXITY: O(n)
# ---------------------------------------------------------------------------
# Time complexity describes how work grows with the number of prices n.
#
# The loop checks n - 1 consecutive pairs.
# Each iteration performs O(1) work.
#
# Total = (n - 1) × O(1) = O(n).
# Best, average, and worst-case time are O(n) for n >= 2.


# ---------------------------------------------------------------------------
# EXTRA SPACE COMPLEXITY: O(1)
# ---------------------------------------------------------------------------
# Only profit and the loop index are stored.
# No extra list or recursion is needed.
#
# Extra memory stays constant as n grows, so it is O(1).

'''
Time Complexity: O(n)

Reason:
The loop checks every consecutive price pair once and adds only positive
price differences.

Space Complexity: O(1)

Reason:
Only the profit variable and loop index are used.
'''
