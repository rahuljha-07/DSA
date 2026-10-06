import sys


# Function to recursively find the maximum number
def findMaxNumber(str, k, maxNum, index):
    if k <= 0 or index >= len(str):
        return
    maxChar = str[index]
    # Find the maximum character from index to end
    for i in range(index + 1, len(str)):
        if str[i] > maxChar:
            maxChar = str[i]
    # If current index already has the max digit, move to next
    if maxChar == str[index]:
        findMaxNumber(str, k, maxNum, index + 1)
        return
    # Swap will happen, so decrease k
    k -= 1
    # Swap with every occurrence of maxChar from right to left
    for i in range(index, len(str)):
        if str[i] == maxChar:
            str[index], str[i] = str[i], str[index]
            candidate = "".join(str)
            if candidate > maxNum[0]:
                maxNum[0] = candidate
            findMaxNumber(str, k, maxNum, index + 1)
            # Backtrack
            str[index], str[i] = str[i], str[index]


# Function to get the largest number with at most K swaps
def findMaximumNum(str, k):
    maxNum = [str]
    findMaxNumber(list(str), k, maxNum, 0)
    return maxNum[0]


def main():
    tokens = iter(sys.stdin.read().split())
    print("Enter the number of swaps (K): ", end="")
    k = int(next(tokens))
    print("Enter the string of digits: ", end="")
    str = next(tokens)
    print("Largest number possible:", findMaximumNum(str, k))


if __name__ == "__main__":
    main()


'''
Let n be digit count and k the swap limit.
Time: O(n^2*n^min(k,n)) conservative bound: up to n choices for each
swap-consuming level, with up to n non-swap index advances per branch
and O(n) scans/string comparisons. Maximum-digit pruning reduces branches.
Space: O(n) auxiliary mutable digits, best string, and recursion depth:
index advances on every call and swaps are undone in place.
The index-end check fixes the source's access past already-maximal strings.
'''
