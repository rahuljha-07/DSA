def countWaysHelper(n, dp):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    dp[n] = countWaysHelper(n - 3, dp) + countWaysHelper(n - 5, dp) + countWaysHelper(n - 10, dp)
    return dp[n]


def count(n):
    dp = [-1] * (n + 1)
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
