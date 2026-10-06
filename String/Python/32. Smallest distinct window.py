def minWindow(s):
    # Frequency map for characters in t
    mp = {}
    for ch in s:
        mp[ch] = 1

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
            # Update the minimum window before contracting
            if j - i + 1 < minLen:
                minLen = j - i + 1
                startIdx = i
            if s[i] in mp:
                mp[s[i]] += 1
                if mp[s[i]] == 1:
                    # We lost a required character
                    count += 1
            # Move left pointer to contract
            i += 1
        # Expand the window by moving the right pointer
        j += 1

    if minLen == float('inf'):
        return ""

    # Return the minimum window substring
    return s[startIdx:startIdx + minLen]


s = "aabcbcdbca"
print(minWindow(s))


'''
Time Complexity: O(n), where n is the string length.

Reason:
The right pointer visits each character once.
The left pointer also moves forward only, so every character is
removed from the window at most once.
Therefore the total sliding window work is linear.

Space Complexity: O(k)

Reason:
The map stores counts for distinct characters only.
If there are k distinct characters, the map size is O(k).
'''
