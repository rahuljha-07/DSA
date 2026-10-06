class Solution:
    def __init__(self):
        self.m = {}

    # Recursive function to solve the Boolean Parenthesization problem
    def solve(self, i, j, s, isTrue):
        # Base case: if the start index is greater than the end index
        if i > j:
            # No valid expression
            return 0
        # Base case: if the expression has only one character
        if i == j:
            # If we need the result to be True
            # If we need the result to be False
            return int(s[i] == ('T' if isTrue else 'F'))
        # Create a unique key for the memoization map
        temp = f"{i} {j} {int(isTrue)}"
        if temp in self.m:
            # Return the stored result if exists
            return self.m[temp]
        # Initialize the result
        ans = 0
        for k in range(i + 1, j, 2):
            # Recursively calculate the number of True and False values for left and right
            # sub-expressions
            # Left part of the expression needs to be True
            leftTrue = self.solve(i, k - 1, s, True)
            # Left part of the expression needs to be False
            leftFalse = self.solve(i, k - 1, s, False)
            # Right part of the expression needs to be True
            rightTrue = self.solve(k + 1, j, s, True)
            # Right part of the expression needs to be False
            rightFalse = self.solve(k + 1, j, s, False)
            # Handle each operator between the two sub-expressions
            if s[k] == '&':
                # AND operation
                if isTrue:
                    # True if both sides are True
                    ans += leftTrue * rightTrue
                else:
                    ans += leftTrue * rightFalse + leftFalse * rightTrue + leftFalse * rightFalse
            # False if any one side is False
            if s[k] == '|':
                # OR operation
                if isTrue:
                    ans += leftTrue * rightTrue + leftFalse * rightTrue + leftTrue * rightFalse
                # True if any one side is True
                else:
                    # False only if both sides are False
                    ans += leftFalse * rightFalse
            if s[k] == '^':
                # XOR operation
                if isTrue:
                    ans += leftTrue * rightFalse + leftFalse * rightTrue
                # True if one side is True and the other side is False
                else:
                    ans += leftTrue * rightTrue + leftFalse * rightFalse
        # False if both sides are the same
        # Store the result in the memoization map to avoid redundant calculations
        self.m[temp] = ans
        return ans

    # Function to count the number of ways to parenthesize the expression to get True
    def countWays(self, n, s):
        self.m.clear()
        i = 0
        j = n - 1
        # Solve for the full range [i, j] with the result being True
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
