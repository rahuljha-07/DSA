def minWindow(s, t):
    # Frequency map for characters in t
    mp = {}
    for ch in t:
        mp[ch] = mp.get(ch, 0) + 1

    minLen = float('inf')
    # Start index of the minimum window
    startIdx = 0
    # Left pointer for the sliding window
    i = 0
    # Right pointer for the sliding window
    j = 0
    # Number of unique characters in t
    count = len(mp)

    while j < len(s):
        if s[j] in mp:
            mp[s[j]] -= 1
            if mp[s[j]] == 0:
                # Found a complete match for this character
                count -= 1

        # Try to contract the window until it's no longer valid
        while count == 0:
            # Update minLen before modifying mp[s[i]]
            if j - i + 1 < minLen:
                minLen = j - i + 1
                startIdx = i

            if s[i] in mp:
                mp[s[i]] += 1
                # Lost a required character
                if mp[s[i]] == 1:
                    # Window becomes invalid
                    count += 1
            # Move the left pointer to contract the window
            i += 1

        # Expand the window by moving the right pointer
        j += 1

    if minLen == float('inf'):
        return ""

    # Return the minimum window substring
    return s[startIdx:startIdx + minLen]


s = "timetopractice"
t = "toc"
print(minWindow(s, t))


'''
Time Complexity: O(n + m), where n is length of s and m is length of t.

Reason:
First we build the frequency map from t, which takes O(m).
Then the sliding window scans s using two pointers.
Both pointers move forward only, so s is processed in O(n).

Space Complexity: O(m)

Reason:
The frequency map stores characters from t.
In the worst case, all characters in t are distinct.
'''
