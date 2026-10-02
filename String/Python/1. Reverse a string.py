def reverseString(s):
    n = len(s)
    left = 0
    right = n - 1

    # Loop to swap characters from start and end
    while left < right:
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1


'''
Time Complexity:
O(n)

Reason:

We traverse only half of the string,
but asymptotically that is still O(n).

Each swap takes O(1) time.


Space Complexity:
O(1)

Reason:

We reverse the string in-place.

Only variables n, left, and right are used.

Therefore:
O(1)
'''