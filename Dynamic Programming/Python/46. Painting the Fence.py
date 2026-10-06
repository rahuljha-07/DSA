class Solution:
    def __init__(self):
        self.totalWays = 0
        self.dp = []

    def solve(self, idx, str, n, k, lastColor, count):
        # Base case: If all posts are painted
        if idx == n:
            # Print the valid pattern
            print(str)
            # Valid pattern found
            return 1
        # Check if the result is already computed
        if self.dp[idx][lastColor][count] != -1:
            return self.dp[idx][lastColor][count]
        # To accumulate valid ways from this state
        ways = 0
        # Iterate through all possible colors
        for i in range(1, k + 1):
            if i == lastColor:
                # If the same color as last, ensure not more than 2 consecutively
                if count < 2:
                    ways += self.solve(idx + 1, str + f"{i}", n, k, i, count + 1)
            else:
                # Different color, reset consecutive count
                ways += self.solve(idx + 1, str + f"{i}", n, k, i, 1)
        # Store the result in the memoization table and return
        self.dp[idx][lastColor][count] = ways
        return ways

    def countWays(self, n, k):
        # Initialize the memoization table with -1
        self.dp = [[[-1] * 3 for _ in range(k + 1)] for _ in range(n)]
        # Start the recursive process
        return self.solve(0, "", n, k, 0, 0)


def main():
    sol = Solution()
    n = 3
    k = 4
    print("Valid ways to paint the fence:")
    total = sol.countWays(n, k)
    print("Total valid ways:", total)


if __name__ == "__main__":
    main()


'''
Let n>=0 be posts, k>=0 colors, and B=max(1, digits(k)).
Time: O(n*k^2) counting arithmetic: O(n*k) idx/color/run states, each
tries k colors. Retained prefix string copying/printing adds a conservative
O(n^2*k^2*B) bound (plus O(n*(k+1)) table allocation).
Space: O(n*(k+1)) memo plus O(n^2*B) live prefix strings across recursion.
The count is memoized correctly, but cache hits skip printing their full
prefixes: the source does NOT print every valid coloring. That behavior is
preserved rather than removing memoization or changing to a counting formula.
For k>9, concatenated multi-digit color labels have no separators, as in C++.
'''
