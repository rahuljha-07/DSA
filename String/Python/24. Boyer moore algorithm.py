NO_OF_CHARS = 256


# Preprocessing function to fill the bad character array
def badCharHeuristic(str, size, badchar):
    # Initialize all occurrences as -1
    for i in range(NO_OF_CHARS):
        badchar[i] = -1

    # Fill the actual value of the last occurrence of each character in the pattern
    for i in range(size):
        badchar[ord(str[i])] = i


# Pattern searching function using the Bad Character Heuristic of the Boyer-Moore Algorithm
# Parameters:
# - txt: The text in which to search for the pattern
# - pat: The pattern to search for
def search(txt, pat):
    # Length of the pattern
    m = len(pat)
    # Length of the text
    n = len(txt)

    # Array to store the last occurrence of each character in the pattern
    badchar = [0] * NO_OF_CHARS

    # Fill the bad character array by calling the preprocessing function
    badCharHeuristic(pat, m, badchar)

    # s is the shift of the pattern with respect to the text
    s = 0
    # While there is a valid shift
    while s <= n - m:
        # Start comparing from the end of the pattern
        j = m - 1

        # Keep reducing index j while characters of pattern and text are matching
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1

        # If the pattern is found
        if j < 0:
            print("Pattern occurs at shift =", s)
            # Shift the pattern to align with the last occurrence of the next character in
            # the text
            s += m - badchar[ord(txt[s + m])] if s + m < n else 1
        else:
            # Shift the pattern so that the bad character in the text aligns with the last
            # occurrence in the pattern
            s += max(1, j - badchar[ord(txt[s + j])])


txt = "ABAAABCD"
pat = "ABC"
search(txt, pat)


'''
Time Complexity: O(n * m) in the worst case.

Reason:
The algorithm shifts the pattern using the bad character table.
Usually this skips characters and performs better in practice.
But in the worst case, many alignments may still compare up to m
characters against the text of length n.

Space Complexity: O(1)

Reason:
The bad character table has fixed size 256, so it does not grow
with the input text or pattern length.
'''
