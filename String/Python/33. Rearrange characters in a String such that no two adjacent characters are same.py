import heapq


def rearrangeString(s):
    charCount = {}
    for c in s:
        charCount[c] = charCount.get(c, 0) + 1

    maxHeap = []
    for entry in charCount:
        heapq.heappush(maxHeap, (-charCount[entry], entry))

    n = len(s)
    if -maxHeap[0][0] > (n + 1) // 2:
        return "Not Possible"

    resultVec = [''] * n
    index = 0

    while len(maxHeap) != 0:
        count, character = heapq.heappop(maxHeap)
        count = -count

        for i in range(count):
            if index >= n:
                index = 1
            resultVec[index] = character
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
