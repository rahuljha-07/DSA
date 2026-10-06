import heapq


# Function to calculate the minimized value of the string
def minValue(s, k):
    # Variable to store the final minimized value
    ans = 0
    # Map to store the frequency of each character
    m = {}
    # Max-heap to store character frequencies in descending order
    q = []

    # Step 1: Count the frequency of each character in the string
    for i in range(len(s)):
        m[s[i]] = m.get(s[i], 0) + 1

    for ch in m:
        # Store negated values so heapq's min-heap behaves as a max-heap.
        heapq.heappush(q, -m[ch])

    # Step 3: Reduce the frequency of the most frequent characters k times
    while k > 0 and len(q) != 0:
        temp = -heapq.heappop(q)
        if temp > 1:
            # Reduce this frequency by 1
            temp -= 1
            heapq.heappush(q, -temp)
        k -= 1

    # Step 4: Calculate the minimized value as the sum of squares of all remaining
    # frequencies
    while len(q) != 0:
        freq = -heapq.heappop(q)
        ans += freq * freq

    # Return the minimized value
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
