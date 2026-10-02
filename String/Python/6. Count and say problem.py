def countAndSay(n):
    # Base case
    if n == 1:
        return "1"

    # Start with the first sequence element
    s = "1"

    # Generate from 2nd element up to nth element
    for i in range(2, n + 1):

        t = ""
        c = 1

        # Traverse the current string
        for j in range(1, len(s)):

            # Same character, increase count
            if s[j] == s[j - 1]:
                c += 1

            else:
                # Add count + previous character
                t += str(c) + s[j - 1]

                # Reset count
                c = 1

        # Add the last group
        t += str(c) + s[len(s) - 1]

        # Update s for next iteration
        s = t

    return s


# Example
n = 4

print(
    "The", n,
    "th element of the count-and-say sequence is:",
    countAndSay(n)
)


'''
Time Complexity:
O(L)

Reason:

At every step, we traverse the entire current string
to generate the next string.

If L represents the total number of characters processed
across all generated terms, the total time complexity is O(L).

The sequence length grows as n increases, so it is not simply O(n).


Space Complexity:
O(Ln)

More precisely, at any one time we mainly store:

s -> current term
t -> next term

So the auxiliary space is proportional to the length of
the largest generated term.

If the nth term has length L_n:

Space Complexity:
O(L_n)
'''