# Function to calculate the maximum number of ways to make the target sum
def coinChange(coins, n, sum):
    # Create a DP table `t` with dimensions (n+1) x (sum+1)
    t = [[0] * (sum + 1) for _ in range(n + 1)]
    # Initialize the DP table
    # If sum is 0, there's one way to achieve it: use no coins
    for i in range(n + 1):
        t[i][0] = 1
    # Fill the DP table iteratively
    for i in range(1, n + 1):
        # If no coins are available and sum > 0, there's no way to achieve it
        for j in range(1, sum + 1):
            if coins[i - 1] <= j:
                t[i][j] = t[i][j - coins[i - 1]] + t[i - 1][j]
            else:
                # Exclude the coin
                t[i][j] = t[i - 1][j]
    # The answer is in the bottom-right corner of the table
    return t[n][sum]


def main():
    coins = [1, 2, 3]
    n = len(coins)
    sum = 4
    print("Maximum number of ways to make the sum =", coinChange(coins, n, sum))


if __name__ == "__main__":
    main()


'''
Let n be the number of elements and S the target sum.
Time: O((n+1)*(S+1)): the table has (n+1)*(S+1) states and each state
uses at most two already-computed states in O(1) arithmetic work.
Space: O((n+1)*(S+1)) for the full 2D table; it is not compressed.
Assumes positive coin denominations and target. Arithmetic costs treat
stored counts/values as machine-sized; Python big integers can add cost.
Including a coin uses the same row because reuse is unlimited.
Counts are combinations, not ordered sequences; use distinct denominations.
'''
