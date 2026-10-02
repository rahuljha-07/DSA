import sys


def generatePermutations(str, startIndex, result):
    if startIndex == len(str) - 1:
        result.append("".join(str))
        return
    for i in range(startIndex, len(str)):
        str[startIndex], str[i] = str[i], str[startIndex]
        generatePermutations(str, startIndex + 1, result)
        str[startIndex], str[i] = str[i], str[startIndex]


def printPermutations(str):
    result = []
    generatePermutations(list(str), 0, result)
    result.sort()
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
