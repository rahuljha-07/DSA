def willAWinHelper(n, x, y, memo):
    if n == 0:
        return False
    if n == 1:
        return True
    if n in memo:
        return memo[n]
    if n - 1 >= 0 and not willAWinHelper(n - 1, x, y, memo):
        memo[n] = True
        return True
    if n - x >= 0 and not willAWinHelper(n - x, x, y, memo):
        memo[n] = True
        return True
    if n - y >= 0 and not willAWinHelper(n - y, x, y, memo):
        memo[n] = True
        return True
    memo[n] = False
    return False


def willAWin(n, x, y):
    memo = {}
    return willAWinHelper(n, x, y, memo)


def main():
    n = 5
    x = 3
    y = 4
    print("A" if willAWin(n, x, y) else "B")


if __name__ == "__main__":
    main()


'''
Let n>=0 be coins, with positive move sizes x and y.
Time: O(n+1) expected: each remaining count is memoized once and tries
at most three moves; dictionary lookups take expected O(1).
Space: O(n) memo plus O(n) stack, since repeatedly taking one coin
can create the longest recursion chain. No game-tree enumeration is stored.
'''
