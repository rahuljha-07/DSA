INT_MAX = (1 << 31) - 1


def coinChangeMinCoins(coins, n, sum):
    t = [[INT_MAX - 1] * (sum + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        t[i][0] = 0
    if n == 0:
        return 0 if sum == 0 else -1
    for j in range(1, sum + 1):
        if j % coins[0] == 0:
            t[1][j] = j // coins[0]
        else:
            t[1][j] = INT_MAX - 1
    for i in range(2, n + 1):
        for j in range(1, sum + 1):
            if coins[i - 1] <= j:
                t[i][j] = min(1 + t[i][j - coins[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]
    return -1 if t[n][sum] == INT_MAX - 1 else t[n][sum]


'''
Let n be the number of elements and S the target sum.
Time: O((n+1)*(S+1)): the table has (n+1)*(S+1) states and each state
uses at most two already-computed states in O(1) arithmetic work.
Space: O((n+1)*(S+1)) for the full 2D table; it is not compressed.
Assumes positive coin denominations and target. Arithmetic costs treat
stored counts/values as machine-sized; Python big integers can add cost.
The first coin row checks divisibility; later rows take the minimum
of reusing a coin and excluding it. n=0 is handled before coins[0] access.
'''
