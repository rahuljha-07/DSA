class Solution:
    def __init__(self):
        self.m = {}

    def solve(self, i, j, s, isTrue):
        if i > j:
            return 0
        if i == j:
            return int(s[i] == ('T' if isTrue else 'F'))
        temp = f"{i} {j} {int(isTrue)}"
        if temp in self.m:
            return self.m[temp]
        ans = 0
        for k in range(i + 1, j, 2):
            leftTrue = self.solve(i, k - 1, s, True)
            leftFalse = self.solve(i, k - 1, s, False)
            rightTrue = self.solve(k + 1, j, s, True)
            rightFalse = self.solve(k + 1, j, s, False)
            if s[k] == '&':
                if isTrue:
                    ans += leftTrue * rightTrue
                else:
                    ans += leftTrue * rightFalse + leftFalse * rightTrue + leftFalse * rightFalse
            if s[k] == '|':
                if isTrue:
                    ans += leftTrue * rightTrue + leftFalse * rightTrue + leftTrue * rightFalse
                else:
                    ans += leftFalse * rightFalse
            if s[k] == '^':
                if isTrue:
                    ans += leftTrue * rightFalse + leftFalse * rightTrue
                else:
                    ans += leftTrue * rightTrue + leftFalse * rightFalse
        self.m[temp] = ans
        return ans

    def countWays(self, n, s):
        self.m.clear()
        i = 0
        j = n - 1
        ans = self.solve(i, j, s, True)
        return ans


def main():
    sol = Solution()
    s = "T|T&F^T"
    n = len(s)
    print("Number of ways to evaluate the expression to True:", sol.countWays(n, s))


if __name__ == "__main__":
    main()


'''
Let n=len(s), a valid alternating literal/operator expression.
Time: O(n^3) arithmetic work: O(n^2) intervals times two truth targets,
each trying O(n) operators. String-key construction/hashing can add
O(log(n+1)) per lookup, giving O(n^3 log(n+1)) conservative actual work.
Space: O(n^2 log(n+1)) key characters/cached counts plus O(n) recursion.
Counts are not reduced modulo anything; large integer arithmetic adds cost.
countWays clears m so reusing one Solution cannot mix different expressions.
'''
