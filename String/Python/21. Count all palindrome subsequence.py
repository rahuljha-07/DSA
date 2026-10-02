memo = {}


def countPalindromicSubsequences(str, start, end):
    key = f"{start}_{end}"

    if key in memo:
        return memo[key]

    if start > end:
        return 0

    if start == end:
        return 1

    count = 0

    if str[start] == str[end]:
        count += countPalindromicSubsequences(str, start + 1, end - 1) + 1

    count += countPalindromicSubsequences(str, start + 1, end)
    count += countPalindromicSubsequences(str, start, end - 1)
    count -= countPalindromicSubsequences(str, start + 1, end - 1)

    memo[key] = count
    return memo[key]


str = "abcadb"
palindromicCount = countPalindromicSubsequences(str, 0, len(str) - 1)

print("Number of palindromic subsequences:", palindromicCount)


'''
Time Complexity: O(n^2), where n is the string length.

Reason:
The recursive state is identified by start and end.
There are n choices for start and n choices for end,
so at most O(n^2) states are solved.

Memoization makes sure each state is computed once.
Each state does only constant extra work besides recursive calls.

Space Complexity: O(n^2)

Reason:
The memo dictionary stores the answer for each start/end pair.
The recursion stack can go up to O(n), but O(n^2) memo space dominates.
'''
