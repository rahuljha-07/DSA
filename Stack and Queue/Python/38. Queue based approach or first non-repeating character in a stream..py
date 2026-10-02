from collections import deque


def getFirstNonRepeatingCharactersInStream(stream, n):
    charCount = {}
    q = deque()
    result = []

    for i in range(n):
        currentChar = stream[i]

        charCount[currentChar] = charCount.get(currentChar, 0) + 1

        if charCount[currentChar] == 1:
            q.append(currentChar)

        while len(q) != 0:
            frontChar = q[0]
            if charCount[frontChar] == 1:
                break
            else:
                q.popleft()

        if len(q) == 0:
            result.append("#")
        else:
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
