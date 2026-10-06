def rabinKarp(text, pattern):
    n = len(text)
    m = len(pattern)
    # A prime number for hashing
    prime = 101
    # The base for ASCII characters
    base = 256

    # Hash value for the pattern
    patternHash = 0
    # Hash value for the current window in the text
    windowHash = 0
    h = 1

    # Result list to store the starting indices of matched patterns
    result = []

    for i in range(m - 1):
        h = (h * base) % prime

    # Pre-compute base^(m-1) % prime
    # for (int i = 0; i < m - 1; i++)
    # h = (h * base) % prime;
    # Compute the hash value of the pattern and the first window of the text
    for i in range(m):
        patternHash = (base * patternHash + ord(pattern[i])) % prime
        windowHash = (base * windowHash + ord(text[i])) % prime

    # Slide the pattern over the text one character at a time
    for i in range(n - m + 1):
        # Check if the current window hash matches the pattern hash
        if patternHash == windowHash:
            # If hash matches, check each character to avoid false positives
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                result.append(i)

        # Calculate the hash of the next window
        if i < n - m:
            windowHash = (base * (windowHash - ord(text[i]) * h) + ord(text[i + m])) % prime
            # Ensure non-negative hash
            if windowHash < 0:
                windowHash += prime

    return result


text = "aabacaadaba"
pattern = "aba"
indices = rabinKarp(text, pattern)

print("Pattern found at indices:", end=" ")
for idx in indices:
    print(idx, end=" ")
print()


'''
Time Complexity: O(n + m) average case, O(n * m) worst case.

Reason:
First we calculate the hash for the pattern and the first window,
which takes O(m).

Then we slide the window across the text once, which takes O(n).
If the hash matches, we compare the actual characters.
Normally hash matches are rare, so this stays close to O(n + m).
In the worst case, many hash collisions can happen and each match
check may compare m characters, so it becomes O(n * m).

Space Complexity: O(1)

Reason:
Only a few integer variables are used for hashes and indexes.
The result list stores matching indexes, so output space is separate.
'''
