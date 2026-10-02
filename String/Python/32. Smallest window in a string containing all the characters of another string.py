def minWindow(s, t):
    mp = {}
    for ch in t:
        mp[ch] = mp.get(ch, 0) + 1

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
