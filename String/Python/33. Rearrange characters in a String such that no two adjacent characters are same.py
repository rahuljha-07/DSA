import heapq


# Function to rearrange characters in a string so that no two adjacent characters are the
# same
def rearrangeString(s):
    # Create a frequency map to count occurrences of each character
    charCount = {}
    for c in s:
        charCount[c] = charCount.get(c, 0) + 1

    # Create a max heap based on character frequencies
    maxHeap = []
    for entry in charCount:
        # Store negated values so heapq's min-heap behaves as a max-heap.
        heapq.heappush(maxHeap, (-charCount[entry], entry))

    # Check the condition for possibility
    n = len(s)
    if -maxHeap[0][0] > (n + 1) // 2:
        # If the most frequent character's count is greater than half of the string length
        return "Not Possible"

    # Create a list to store the characters while maintaining the odd/even index filling
    resultVec = [''] * n
    index = 0

    # Fill characters in the result
    while len(maxHeap) != 0:
        # Get the character with the highest frequency
        count, character = heapq.heappop(maxHeap)
        count = -count

        # Place the character in the result
        for i in range(count):
            if index >= n:
                # Move to odd index after filling even indices
                index = 1
            # Place character at the current index
            resultVec[index] = character
            # Increment index to fill the next position
            index += 2

    return "".join(resultVec)


input1 = "aaabc"
print("Input:", input1 + ",", "Output:", rearrangeString(input1))

input2 = "aaabb"
print("Input:", input2 + ",", "Output:", rearrangeString(input2))

input3 = "aa"
print("Input:", input3 + ",", "Output:", rearrangeString(input3))

input4 = "aaaabc"
print("Input:", input4 + ",", "Output:", rearrangeString(input4))


'''
Time Complexity: O(n log k), where k is number of distinct characters.

Reason:
Counting frequencies takes O(n).
Each distinct character is inserted into the heap, costing O(log k).
Then characters are popped from the heap and placed in the result.

The heap operations depend on k distinct characters, while filling
the result touches n positions.

Space Complexity: O(n + k)

Reason:
The frequency map and heap store k distinct characters.
The result list stores n characters before joining them.
'''
