class Solution:
    def __init__(self):
        self.dp = {}

    def isPalindrome(self, str):
        l = 0
        r = len(str) - 1
        while l < r:
            if str[l] != str[r]:
                return False
            l += 1
            r -= 1
        return True

    def solve(self, idx, current, s):
        # Base case: When we reach the end of the string
        if idx == len(s):
            if current and self.isPalindrome(current):
                print("Palindrome Subsequence:", current)
                return 1
            return 0
        if idx in self.dp and self.dp[idx][0] == current:
            return self.dp[idx][1]
        # Choice 1: Include the current character
        pick = self.solve(idx + 1, current + s[idx], s)
        # Choice 2: Exclude the current character
        notPick = self.solve(idx + 1, current, s)
        # Store the result in the memoization table
        self.dp[idx] = (current, pick + notPick)
        return self.dp[idx][1]

    def countPalindromicSubsequences(self, s):
        # Clear the memoization table
        self.dp.clear()
        return self.solve(0, "", s)


def main():
    sol = Solution()
    s1 = "abcd"
    s2 = "aab"
    s3 = "b"
    for s in (s1, s2, s3):
        print("Input:", s)
        print("Total Palindromic Subsequences: ", end="")
        total = sol.countPalindromicSubsequences(s)
        print(total)
        print()


if __name__ == "__main__":
    main()


'''
Let n be string length.
Time: O(n*2^n) conservative worst case: include/exclude may explore
2^n subsequences; copied strings, leaf palindrome scans, and printing
can each cost O(n). Caching only the latest prefix at each idx does
not provide the usual O(n^2) interval-DP complexity.
Space: O(n^2) auxiliary: up to n cached prefix strings of O(n) length
plus copied strings across an O(n)-deep stack. Printed output is not stored.
Counts include repeated value-identical subsequences from different index
choices. Memo hits can skip duplicate printing; the source behavior is retained.
'''
