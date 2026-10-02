def maxSteal(houses, index, memo):
    if index >= len(houses):
        return 0

    if memo[index] != -1:
        return memo[index]

    steal = houses[index] + maxSteal(houses, index + 2, memo)
    skip = maxSteal(houses, index + 1, memo)

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
