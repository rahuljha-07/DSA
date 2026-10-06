import sys


# Helper function to generate permutations
def generatePermutations(str, startIndex, result):
    # Base case: If startIndex is at the end of the string, store the permutation
    if startIndex == len(str) - 1:
        result.append("".join(str))
        return
    # Iterate through the string and swap characters to generate permutations
    for i in range(startIndex, len(str)):
        # Swap the current character with the character at startIndex
        str[startIndex], str[i] = str[i], str[startIndex]
        # Recursively generate permutations for the remaining string
        generatePermutations(str, startIndex + 1, result)
        # Backtrack: Restore the original order of the string
        str[startIndex], str[i] = str[i], str[startIndex]


# Function to print all permutations of a given string
def printPermutations(str):
    result = []
    # Generate all permutations
    generatePermutations(list(str), 0, result)
    # Sort the permutations to ensure they are printed in lexicographical order
    result.sort()
    # Print the permutations
    for perm in result:
        print(perm)


def main():
    print("Enter a string: ", end="")
    inputString = sys.stdin.read().split()[0]
    print("Permutations of the string are:")
    printPermutations(inputString)


if __name__ == "__main__":
    main()


'''
Let n be string length and P=n! generated permutations (including duplicates).
Time: O(n*P) generation/copying plus O(n*P*log(P+1)) conservative sorting
bound, because comparing equal-prefix strings can inspect n characters.
Space: O(n) auxiliary characters/recursion plus O(n*P) stored results
and O(P) sorting workspace.
Duplicate letters still produce duplicate outputs; empty input produces
no permutations, matching the original helper's base case.
'''
