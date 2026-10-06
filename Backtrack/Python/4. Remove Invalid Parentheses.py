class Solution:
    def __init__(self):
        self.validResults = []
        self.processedStrings = {}

    # Function to calculate the minimum number of invalid parentheses
    def calculateMinInvalid(self, s):
        # Stack to track unmatched parentheses
        parenthesesStack = []
        for c in s:
            if c == '(':
                # Push open parentheses onto the stack
                # Unmatched closing parentheses
                parenthesesStack.append('(')
            elif c == ')':
                if parenthesesStack and parenthesesStack[-1] == '(':
                    # Balanced pair found, remove from stack
                    parenthesesStack.pop()
                else:
                    parenthesesStack.append(')')
        # Remaining stack size is the count of invalid parentheses
        return len(parenthesesStack)

    # Recursive function to solve the problem
    def backtrack(self, currentString, remainingInvalid):
        # Check if this string has already been processed
        if self.processedStrings.get(currentString, 0) != 0:
            return
        self.processedStrings[currentString] = 1
        # Base case: If no invalid parentheses remain
        if remainingInvalid == 0:
            # Check if the current string is valid
            if self.calculateMinInvalid(currentString) == 0:
                # Add to results if valid
                self.validResults.append(currentString)
            return
        # Try removing each character in the string
        for i in range(len(currentString)):
            if currentString[i] not in "()":
                continue
            # Create a new string by excluding the current character
            newString = currentString[:i] + currentString[i + 1:]
            # Recurse with the new string and decrement the remaining invalid count
            self.backtrack(newString, remainingInvalid - 1)

    def removeInvalidParentheses(self, s):
        self.validResults.clear()
        self.processedStrings.clear()
        minInvalidCount = self.calculateMinInvalid(s)
        # Start backtracking to generate all valid strings
        self.backtrack(s, minInvalidCount)
        # Return the list of valid results
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
