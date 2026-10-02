def maximizeCutsHelper(n, x, y, z, dp):
    if n == 0:
        return 0
    if n < 0:
        return -1
    if dp[n] is not None:
        return dp[n]
    cutX = maximizeCutsHelper(n - x, x, y, z, dp)
    cutY = maximizeCutsHelper(n - y, x, y, z, dp)
    cutZ = maximizeCutsHelper(n - z, x, y, z, dp)
    maxCuts = max(cutX, cutY, cutZ)
    dp[n] = -1 if maxCuts == -1 else 1 + maxCuts
    return dp[n]


def maximizeCuts(n, x, y, z):
    dp = [None] * (n + 1)
    result = maximizeCutsHelper(n, x, y, z, dp)
    return 0 if result == -1 else result


def main():
    n = 4
    x = 2
    y = 1
    z = 1
    result = maximizeCuts(n, x, y, z)
    print("Maximum number of cuts:", result)


if __name__ == "__main__":
    main()


'''
Let n>=0 be rod length and a=min(x,y,z)>0.
Time: O(n+1): memoize each remaining length once, trying three cuts.
None marks uncomputed states so impossible (-1) results are also cached;
the source's shared -1 sentinel could repeatedly recompute failures.
Space: O(n+1) DP plus O(n/a+1) recursion depth. The recurrence is unchanged.
'''
