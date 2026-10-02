def isPalindrome(S):
    i = 0
    j = len(S) - 1

    # Check characters from both ends
    while i < j:

        if S[i] != S[j]:
            return 0  # Not a palindrome

        i += 1
        j -= 1

    return 1  # It's a palindrome


'''
Time Complexity:
O(n)

Reason:

We compare characters from both ends and move
toward the center.

At most n / 2 comparisons are performed.

Therefore:
O(n)


Space Complexity:
O(1)

Reason:

We only use two variables i and j.

No extra data structure is used.

Therefore:
O(1)
'''