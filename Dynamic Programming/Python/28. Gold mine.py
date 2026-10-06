# Function to get the maximum amount of gold
def getMaxGold(mine):
    # Number of rows
    n = len(mine)
    if n == 0 or not mine[0]:
        return 0
    # Number of columns
    m = len(mine[0])
    # Create a table to store the maximum gold collected up to each cell
    dp = [[0] * m for _ in range(n)]
    # Copy the last column as the base case
    for i in range(n):
        dp[i][m - 1] = mine[i][m - 1]
    # Fill the DP table column by column from right to left
    for col in range(m - 2, -1, -1):
        for row in range(n):
            # Check the three possible directions from the current cell
            # Right
            right = dp[row][col + 1]
            # Diagonally up-right
            right_up = dp[row - 1][col + 1] if row - 1 >= 0 else 0
            # Diagonally down-right
            right_down = dp[row + 1][col + 1] if row + 1 < n else 0
            # Update the DP table with the maximum gold collected
            dp[row][col] = mine[row][col] + max(right, right_up, right_down)
    # Find the maximum gold in the first column
    maxGold = 0
    for i in range(n):
        maxGold = max(maxGold, dp[i][0])
    return maxGold


def main():
    mine1 = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]
    print("Maximum gold collected (Example 1):", getMaxGold(mine1))
    mine2 = [[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]
    print("Maximum gold collected (Example 2):", getMaxGold(mine2))


if __name__ == "__main__":
    main()


'''
Let n/m be mine rows/columns, with nonnegative gold values.
Time: O(n*m): visit each cell once and choose among three rightward
neighbors in constant time; the final first-column maximum costs O(n).
Space: O(n*m) auxiliary for dp; the mine itself is not modified.
Zero boundary values retain the source's nonnegative-value assumption.
'''
