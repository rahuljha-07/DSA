memo = {}


def countPalindromicSubsequences(str, start, end):
    # Create a unique key for the current substring
    key = f"{start}_{end}"

    if key in memo:
        return memo[key]

    # Base case: if the substring is empty
    if start > end:
        # no palindromic subsequences
        return 0

    # Base case: if the substring has one character
    if start == end:
        # single character is a palindrome
        return 1

    count = 0

    # If characters at the start and end are the same
    if str[start] == str[end]:
        # 1 for the palindrome made by the two matching characters
        count += countPalindromicSubsequences(str, start + 1, end - 1) + 1

    count += countPalindromicSubsequences(str, start + 1, end)
    # Count palindromic subsequences excluding either the start or end character
    # excluding start
    count += countPalindromicSubsequences(str, start, end - 1)
    # excluding end
    # subtracting the overlap, as it gets counted twice
    count -= countPalindromicSubsequences(str, start + 1, end - 1)

    # Memoize the result
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
