class Solution:
    def __init__(self):
        self.dp = []

    def solve(self, e, f):
        if e == 1:
            return f
        if f == 0:
            return 0
        if self.dp[e][f] != -1:
            return self.dp[e][f]
        ans = float("inf")
        for k in range(1, f + 1):
            broken = self.solve(e - 1, k - 1)
            not_broken = self.solve(e, f - k)
            maxval = max(broken, not_broken)
            ans = min(ans, maxval + 1)
        self.dp[e][f] = ans
        return ans

    def eggDrop(self, e, f):
        if e < 1 or f < 0:
            raise ValueError("Egg count must be positive and floor count nonnegative")
        self.dp = [[-1] * (f + 1) for _ in range(e + 1)]
        return self.solve(e, f)


def main():
    sol = Solution()
    e = 2
    f = 10
    print("Minimum number of attempts needed:", sol.eggDrop(e, f))


if __name__ == "__main__":
    main()


'''
Let e>=1 be eggs and f>=0 floors.
Time: O((e+1)*(f+1) + e*f^2): at most e*f states; every non-base state
tests all candidate floors up to f. The table allocation is included.
Space: O((e+1)*(f+1)) memo plus O(e+f) recursion depth.
This retains the exhaustive floor-split DP, not binary-search optimization.
'''
