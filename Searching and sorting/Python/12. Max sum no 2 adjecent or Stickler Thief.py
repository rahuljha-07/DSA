def maxSteal(houses, index, memo):
    # Base case: if no houses are left, return 0
    if index >= len(houses):
        return 0

    # Check if we've already computed the result for this index
    if memo[index] != -1:
        return memo[index]

    # Option 1: Steal from the current house and skip the next one
    steal = houses[index] + maxSteal(houses, index + 2, memo)
    # Option 2: Skip the current house and move to the next one
    skip = maxSteal(houses, index + 1, memo)

    # Store the result in memo and return the maximum of both choices
    memo[index] = max(steal, skip)
    return memo[index]


houses = [6, 7, 1, 30, 8, 2, 4]
memo = [-1] * len(houses)
result = maxSteal(houses, 0, memo)
print("Maximum money that can be stolen:", result)


'''
Time Complexity: O(n)

Reason:
Each index is solved once because memo stores the answer. Every state does
constant work after its recursive calls return.

Space Complexity: O(n)

Reason:
The memo list stores n values. The recursion stack can also grow to O(n).
'''
