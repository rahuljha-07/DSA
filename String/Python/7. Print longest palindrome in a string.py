def longestPalindrome(s):
    # Handle edge case: empty string
    if not s:
        return ""

    left = 0
    right = 0

    start = 0
    maxLength = 1

    # Loop through each character
    for i in range(1, len(s)):

        # Check even-length palindrome
        left = i - 1
        right = i

        # Expand around center
        while left >= 0 and right < len(s) and s[left] == s[right]:

            if right - left + 1 > maxLength:
                start = left
                maxLength = right - left + 1

            left -= 1
            right += 1

        # Check odd-length palindrome
        left = i - 1
        right = i + 1

        # Expand around center
        while left >= 0 and right < len(s) and s[left] == s[right]:

            if right - left + 1 > maxLength:
                start = left
                maxLength = right - left + 1

            left -= 1
            right += 1

    # Return longest palindromic substring
    return s[start:start + maxLength]


# Example
s = "babad"

print(
    "The longest palindromic substring is:",
    longestPalindrome(s)
)


'''
Time Complexity:
O(n^2)

Reason:

For every index i, we try to expand around the center.

We check:
1. Even-length palindrome
2. Odd-length palindrome

For each center, expansion can take up to O(n) time.

Since there are n possible centers:

O(n * n) = O(n^2)


Space Complexity:
O(1)

Reason:

We only use variables such as:
left, right, start, maxLength, and i.

No extra data structure is used.

Therefore:
O(1)

Note:
The returned substring s[start:start + maxLength]
creates a new string in Python, so if we count the output,
that can take O(maxLength) space.

Auxiliary space remains O(1).
'''