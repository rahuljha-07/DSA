# Helper function with recursion + memoization
def countWaysHelper(n, dp):
    # Base cases
    # One way to achieve 0 score (do nothing)
    if n == 0:
        return 1
    # No way to achieve a negative score
    if n < 0:
        return 0
    # If already computed, return the stored value
    if dp[n] != -1:
        return dp[n]
    # Recursive calls for the three possible moves (3, 5, 10 points)
    dp[n] = countWaysHelper(n - 3, dp) + countWaysHelper(n - 5, dp) + countWaysHelper(n - 10, dp)
    return dp[n]


# Function to initialize the dp array and call the helper function
def count(n):
    # Create a memoization table initialized to -1
    dp = [-1] * (n + 1)
    # Call the recursive helper function
    return countWaysHelper(n, dp)


def main():
    n1 = 10
    n2 = 20
    for n in (n1, n2):
        print(f"Number of ways to reach score {n}:", count(n))


if __name__ == "__main__":
    main()


'''
Let n>=0 be the target score.
Time: O(n+1) arithmetic operations: each remaining score is memoized
once and adds results for three fixed scoring moves.
Space: O(n+1) memo plus O(n/3+1) recursive depth.
The source counts ORDERED scoring sequences: 3 then 5 differs from
5 then 3. It is not the unordered coin-change interpretation.
Counts can grow large; Python additions cost more than O(1) for big integers.
'''
