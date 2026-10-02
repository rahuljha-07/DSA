memo = {}


def countPalindromicSubsequences(str, start, end):
    key = f"{start}_{end}"
    if key in memo:
        return memo[key]

    result = set()

    if start > end:
        return result

    if start == end:
        result.add(str[start])
        return result

    if str[start] == str[end]:
        innerSubseqs = countPalindromicSubsequences(str, start + 1, end - 1)
        for subseq in innerSubseqs:
            result.add(str[start] + subseq + str[end])
        result.add(str[start])
        result.add(str[end])

    leftSubseqs = countPalindromicSubsequences(str, start + 1, end)
    rightSubseqs = countPalindromicSubsequences(str, start, end - 1)

    result.update(leftSubseqs)
    result.update(rightSubseqs)

    memo[key] = result
    return memo[key]


str = "abcadb"
palindromicSubsequences = countPalindromicSubsequences(str, 0, len(str) - 1)

print("Number of palindromic subsequences:", len(palindromicSubsequences))
print("Palindromic Subsequences:", end=" ")
for subseq in palindromicSubsequences:
    print(subseq, end=" ")
print()


'''
Time Complexity: O(n^2 * k), where k is the cost of storing generated subsequences.

Reason:
There are O(n^2) start/end states.
For each state, sets of palindromic subsequences may be merged.
The variable k represents the total cost of copying, storing,
and merging those generated strings.

Space Complexity: O(n^2 * k)

Reason:
Memoization stores a set of subsequences for many start/end states.
Since the actual subsequences are stored as strings, space depends
on both the number of states and the generated output size.
'''
