class Solution:
    def __init__(self):
        self.validResults = []
        self.processedStrings = {}

    def calculateMinInvalid(self, s):
        parenthesesStack = []
        for c in s:
            if c == '(':
                parenthesesStack.append('(')
            elif c == ')':
                if parenthesesStack and parenthesesStack[-1] == '(':
                    parenthesesStack.pop()
                else:
                    parenthesesStack.append(')')
        return len(parenthesesStack)

    def backtrack(self, currentString, remainingInvalid):
        if self.processedStrings.get(currentString, 0) != 0:
            return
        self.processedStrings[currentString] = 1
        if remainingInvalid == 0:
            if self.calculateMinInvalid(currentString) == 0:
                self.validResults.append(currentString)
            return
        for i in range(len(currentString)):
            if currentString[i] not in "()":
                continue
            newString = currentString[:i] + currentString[i + 1:]
            self.backtrack(newString, remainingInvalid - 1)

    def removeInvalidParentheses(self, s):
        self.validResults.clear()
        self.processedStrings.clear()
        minInvalidCount = self.calculateMinInvalid(s)
        self.backtrack(s, minInvalidCount)
        return list(self.validResults)


def main():
    solution = Solution()
    input = "(a)())()"
    results = solution.removeInvalidParentheses(input)
    print("Valid strings after removing invalid parentheses:")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()


'''
Let n be string length and U distinct explored strings (U<=2^n).
Time: O(n^2*U) expected upper bound: each state tries up to n deletions;
each new string's slicing/concatenation/hash costs O(n). Validation is O(n).
Space: O(n*U) stored processed strings/results plus O(n^2) recursion strings.
Only the minimum invalid-count deletions are explored. State is reset per
public call so reusing Solution does not mix results from different inputs.
'''
