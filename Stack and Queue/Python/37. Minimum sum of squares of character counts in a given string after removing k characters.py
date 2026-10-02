import heapq


def minValue(s, k):
    ans = 0
    freqMap = {}
    maxHeap = []

    for c in s:
        freqMap[c] = freqMap.get(c, 0) + 1

    for entry in freqMap:
        heapq.heappush(maxHeap, -freqMap[entry])

    while k > 0 and len(maxHeap) != 0:
        topFreq = -heapq.heappop(maxHeap)

        if topFreq > 1:
            heapq.heappush(maxHeap, -(topFreq - 1))
        k -= 1

    while len(maxHeap) != 0:
        freq = -heapq.heappop(maxHeap)
        ans += freq * freq

    return ans


str = "abccc"
k = 1
print("Minimized value:", minValue(str, k))

str = "aaab"
k = 2
print("Minimized value:", minValue(str, k))


'''
Time Complexity: O(n + k log d + d log d)

Reason:
Frequencies are counted in O(n). The most frequent character is reduced k
times using a heap of d distinct characters, and final frequencies are popped.

Space Complexity: O(d)

Reason:
The map and heap store frequencies for d distinct characters.
'''
