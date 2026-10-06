def willAWinHelper(n, x, y, memo):
    # Base cases
    # A loses if no coins left
    if n == 0:
        return False
    # A wins if 1 coin is left (can pick the last coin)
    if n == 1:
        return True
    if n in memo:
        return memo[n]
    # Check all possible moves for A
    # Option 1: Pick 1 coin
    if n - 1 >= 0 and not willAWinHelper(n - 1, x, y, memo):
        # A wins
        memo[n] = True
        return True
    # Option 2: Pick x coins
    if n - x >= 0 and not willAWinHelper(n - x, x, y, memo):
        memo[n] = True
        return True
    # Option 3: Pick y coins
    if n - y >= 0 and not willAWinHelper(n - y, x, y, memo):
        memo[n] = True
        return True
    # If none of the moves lead to a win for A, A loses
    memo[n] = False
    return False


# Wrapper function to initialize memoization and call the recursive helper
def willAWin(n, x, y):
    # Memoization table
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
