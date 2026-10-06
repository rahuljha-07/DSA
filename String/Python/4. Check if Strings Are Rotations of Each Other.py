# =========================================================
# 1. USING STRING CONCATENATION + FIND
# =========================================================

def areRotations_find(s1, s2):
    if len(s1) != len(s2):
        return False

    concat = s1 + s1

    ind = concat.find(s2)

    if ind == -1:
        return False

    return True


'''
Time Complexity:
Depends on Python's internal string search implementation.

Conceptually:
We create s1 + s1, which takes O(n).

The substring search can be considered up to O(n * m)
in a simple implementation.

For equal-length strings, worst-case simple analysis can be O(n^2).

Space Complexity:
O(n)

Reason:

concat stores s1 + s1, which has length 2n.

Therefore:
O(n)
'''



# =========================================================
# 2. USING KMP ALGORITHM
# =========================================================

# Build the prefix table (LPS array)
def buildPrefixTable(pattern):
    n = len(pattern)

    lps = [0] * n

    length = 0

    for i in range(1, n):

        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]

        if pattern[i] == pattern[length]:
            length += 1

        lps[i] = length

    return lps


# KMP search to check if pattern exists in text
def kmpSearch(text, pattern):
    lps = buildPrefixTable(pattern)

    # for pattern
    j = 0  # Pointer for pattern

    for i in range(len(text)):

        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == len(pattern):
            # Found
            return True

    # Not found
    return False


# Check if s2 is rotation of s1 using KMP
def areRotations_kmp(s1, s2):

    if len(s1) != len(s2):
        return False

    concat = s1 + s1

    return kmpSearch(concat, s2)


# =========================================================
# EXAMPLE
# =========================================================

s1 = "ABACD"
s2 = "CDABA"

if areRotations_kmp(s1, s2):
    print("Strings are rotations of each other.")
else:
    print("Strings are NOT rotations of each other.")


'''
Time Complexity:
O(n)

Reason:

Let the length of s1 and s2 be n.

Creating:
concat = s1 + s1

takes O(n).

Building the LPS array for s2 takes:
O(n)

KMP searches for s2 inside concat, whose length is 2n.

KMP search takes:
O(2n + n)

Which simplifies to:
O(n)


Space Complexity:
O(n)

Reason:

concat requires O(n) space.

The LPS array also requires O(n) space.

Therefore:
O(n)
'''
