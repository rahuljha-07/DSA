import heapq


def minValue(s, k):
    # Variable to store the minimized sum of squares
    ans = 0
    # Map to store the frequency of each character
    freqMap = {}
    # Max-heap to store character frequencies in descending order
    maxHeap = []

    # Step 1: Count the frequency of each character in the string
    for c in s:
        freqMap[c] = freqMap.get(c, 0) + 1

    # Step 2: Push all frequencies into the max-heap
    for entry in freqMap:
        # Store negated values so heapq's min-heap behaves as a max-heap.
        heapq.heappush(maxHeap, -freqMap[entry])

    # Step 3: Reduce the highest frequency `k` times
    while k > 0 and len(maxHeap) != 0:
        topFreq = -heapq.heappop(maxHeap)

        # Reduce the frequency by 1 if it's greater than 1
        if topFreq > 1:
            # Push the updated frequency back to the heap
            heapq.heappush(maxHeap, -(topFreq - 1))
        k -= 1

    # Step 4: Calculate the minimized value as the sum of squares of all remaining
    # frequencies
    while len(maxHeap) != 0:
        freq = -heapq.heappop(maxHeap)
        # Add the square of each frequency to ans
        ans += freq * freq

    # Return the minimized value
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
