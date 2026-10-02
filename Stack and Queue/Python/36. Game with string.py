import heapq


def minValue(s, k):
    ans = 0
    m = {}
    q = []

    for i in range(len(s)):
        m[s[i]] = m.get(s[i], 0) + 1

    for ch in m:
        heapq.heappush(q, -m[ch])

    while k > 0 and len(q) != 0:
        temp = -heapq.heappop(q)
        if temp > 1:
            temp -= 1
            heapq.heappush(q, -temp)
        k -= 1

    while len(q) != 0:
        freq = -heapq.heappop(q)
        ans += freq * freq

    return ans


str = "abccc"
k = 1
print("Minimized value:", minValue(str, k))


'''
Time Complexity: O(n + k log d + d log d)

Reason:
Counting frequencies takes O(n). Each removal updates the max heap of d
distinct characters in O(log d). Final heap processing removes d entries.

Space Complexity: O(d)

Reason:
The frequency map and heap store one entry per distinct character.
'''
