NO_OF_CHARS = 256


def badCharHeuristic(str, size, badchar):
    for i in range(NO_OF_CHARS):
        badchar[i] = -1

    for i in range(size):
        badchar[ord(str[i])] = i


def search(txt, pat):
    m = len(pat)
    n = len(txt)

    badchar = [0] * NO_OF_CHARS

    badCharHeuristic(pat, m, badchar)

    s = 0
    while s <= n - m:
        j = m - 1

        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1

        if j < 0:
            print("Pattern occurs at shift =", s)
            s += m - badchar[ord(txt[s + m])] if s + m < n else 1
        else:
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
