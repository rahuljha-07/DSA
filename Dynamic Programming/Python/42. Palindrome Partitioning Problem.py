t = []


def isPalindrome(str, i, j):
    while i < j:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True


def solve(str, i, j):
    if i >= j:
        return 0
    if isPalindrome(str, i, j):
        return 0
    if t[i][j] != -1:
        return t[i][j]
    ans = float("inf")
    for k in range(i, j):
        left = t[i][k] if t[i][k] != -1 else solve(str, i, k)
        right = t[k + 1][j] if t[k + 1][j] != -1 else solve(str, k + 1, j)
        temp = left + right + 1
        ans = min(ans, temp)
    t[i][j] = ans
    return ans


def main():
    str = "ababbbabbababa"
    n = len(str)
    t[:] = [[-1] * n for _ in range(n)]
    result = solve(str, 0, n - 1)
    print("Minimum number of cuts needed for Palindrome Partitioning is:", result)


if __name__ == "__main__":
    main()


'''
Let n be string length.
Time: O(n^4) conservative worst-case bound for the retained ordering:
O(n^2) non-palindromic interval computations each try O(n) splits, and
up to O(n^3) recursive calls can perform an O(n) palindrome scan BEFORE
the cache check. Palindromic intervals return without being cached.
With palindrome checks cached/precomputed this could be O(n^3), but
that optimization is not introduced.
Space: O(n^2) memo plus O(n) recursion depth; substrings are not copied.
Initialize/reset global t to -1 for each new string.
'''
