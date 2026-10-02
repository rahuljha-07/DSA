import sys


def isInterleave_helper(s1, s2, s3, i, j, k, m):
    if i == len(s1) and j == len(s2) and k == len(s3):
        return True
    if m[i][j] != -1:
        return m[i][j]
    x = False
    y = False
    if i < len(s1) and s1[i] == s3[k]:
        x = isInterleave_helper(s1, s2, s3, i + 1, j, k + 1, m)
    if j < len(s2) and s2[j] == s3[k]:
        y = isInterleave_helper(s1, s2, s3, i, j + 1, k + 1, m)
    m[i][j] = x or y
    return m[i][j]


def isInterleave(s1, s2, s3):
    a = len(s1)
    b = len(s2)
    if a + b != len(s3):
        return False
    m = [[-1] * (b + 1) for _ in range(a + 1)]
    return isInterleave_helper(s1, s2, s3, 0, 0, 0, m)


def main():
    s1, s2, s3 = sys.stdin.read().split()
    print(1 if isInterleave(s1, s2, s3) else 0)


if __name__ == "__main__":
    main()


'''
Let a/b be lengths of s1/s2.
Time: O((a+1)*(b+1)): each (i,j) is cached once and tries at most two
next characters. k=i+j, so a separate k dimension is unnecessary.
Space: O((a+1)*(b+1)) memo plus O(a+b) recursion stack.
Strings are shared, not copied in each call. The length check rejects
mismatches in O(1) before s3[k] can be accessed outside its bounds.
'''
