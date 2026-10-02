def minWindow(s):
    mp = {}
    for ch in s:
        mp[ch] = 1

    minLen = float('inf')
    startIdx = 0
    i = 0
    j = 0
    count = len(mp)

    while j < len(s):
        if s[j] in mp:
            mp[s[j]] -= 1
            if mp[s[j]] == 0:
                count -= 1

        while count == 0:
            if j - i + 1 < minLen:
                minLen = j - i + 1
                startIdx = i
            if s[i] in mp:
                mp[s[i]] += 1
                if mp[s[i]] == 1:
                    count += 1
            i += 1
        j += 1

    if minLen == float('inf'):
        return ""

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
