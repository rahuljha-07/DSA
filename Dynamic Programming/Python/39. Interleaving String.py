import sys


# Helper function to check if interleaving is possible
def isInterleave_helper(s1, s2, s3, i, j, k, m):
    # If we have reached the end of both s1 and s2 and s3, return true
    if i == len(s1) and j == len(s2) and k == len(s3):
        return True
    # If we have already computed this state, return the result
    if m[i][j] != -1:
        return m[i][j]
    x = False
    y = False
    # If we have not reached the end of s1, check if we can take a character from s1
    if i < len(s1) and s1[i] == s3[k]:
        x = isInterleave_helper(s1, s2, s3, i + 1, j, k + 1, m)
    # If we have not reached the end of s2, check if we can take a character from s2
    if j < len(s2) and s2[j] == s3[k]:
        y = isInterleave_helper(s1, s2, s3, i, j + 1, k + 1, m)
    # Save the result of the current state and return it (Memoization)
    m[i][j] = x or y
    return m[i][j]


def isInterleave(s1, s2, s3):
    a = len(s1)
    b = len(s2)
    if a + b != len(s3):
        return False
    # Create a memoization table initialized to -1 (indicating not yet computed)
    m = [[-1] * (b + 1) for _ in range(a + 1)]
    # Start from the beginning of both strings and s3
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
