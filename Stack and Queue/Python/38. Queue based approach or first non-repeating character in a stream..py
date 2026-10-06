from collections import deque


# Function to return a list of first non-repeating characters in a stream
def getFirstNonRepeatingCharactersInStream(stream, n):
    # Map to store character frequencies
    charCount = {}
    q = deque()
    # list to store the result
    result = []

    # Process each character in the stream
    for i in range(n):
        currentChar = stream[i]

        charCount[currentChar] = charCount.get(currentChar, 0) + 1

        # If the character appears for the first time, add it to the queue
        if charCount[currentChar] == 1:
            q.append(currentChar)

        # Check the front of the queue to find the first non-repeating character
        while len(q) != 0:
            frontChar = q[0]
            if charCount[frontChar] == 1:
                # If the front character is non-repeating, keep it in the queue
                break
            else:
                # If the front character is repeating, remove it
                q.popleft()

        # Add the first non-repeating character to the result list or "#" if none
        if len(q) == 0:
            # No non-repeating character
            result.append("#")
        else:
            # Convert char to string
            result.append(q[0])

    return result


stream = ['a', 'b', 'c', 'a', 'c', 'b', 'd']
result = getFirstNonRepeatingCharactersInStream(stream, len(stream))

for s in result:
    print(s, end=" ")
print()


'''
Time Complexity: O(n)

Reason:
Each stream character is added once. Repeating characters are removed from
the queue at most once, so total queue work is linear.

Space Complexity: O(d)

Reason:
The frequency map and queue store characters from the stream, bounded by the
number of distinct characters d.
'''
