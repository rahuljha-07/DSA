class Solution:
    def __init__(self):
        self.dp = []

    def solve(self, e, f):
        # Base Cases
        # If we have only one egg, test all floors
        if e == 1:
            return f
        # If there are no floors, no tests are needed
        if f == 0:
            return 0
        # Check if result is already computed
        if self.dp[e][f] != -1:
            return self.dp[e][f]
        ans = float("inf")
        # Try dropping an egg from each floor and calculate the worst-case scenario
        for k in range(1, f + 1):
            # Egg breaks: Check floors below
            broken = self.solve(e - 1, k - 1)
            # Egg does not break: Check floors above
            not_broken = self.solve(e, f - k)
            # Take the worst-case scenario of these two
            maxval = max(broken, not_broken)
            # Update the minimum attempts
            ans = min(ans, maxval + 1)
        # Store the result in the memoization table
        self.dp[e][f] = ans
        return ans

    def eggDrop(self, e, f):
        if e < 1 or f < 0:
            raise ValueError("Egg count must be positive and floor count nonnegative")
        # Initialize the memoization table with -1 using list
        self.dp = [[-1] * (f + 1) for _ in range(e + 1)]
        # Solve the problem using the helper function
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
