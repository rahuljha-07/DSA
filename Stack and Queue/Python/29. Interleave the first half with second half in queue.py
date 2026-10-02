from collections import deque


def interleaveQueue(q):
    if len(q) % 2 != 0:
        print("Queue size must be even for interleaving.")
        return

    n = len(q)
    halfSize = n // 2
    firstHalf = deque()

    for i in range(halfSize):
        firstHalf.append(q[0])
        q.popleft()

    while len(firstHalf) != 0:
        q.append(firstHalf[0])
        firstHalf.popleft()

        q.append(q[0])
        q.popleft()


def displayQueue(q):
    print(*q)


q = deque([1, 2, 3, 4])
print("Original queue:", end=" ")
displayQueue(q)
interleaveQueue(q)
print("Interleaved queue:", end=" ")
displayQueue(q)

q2 = deque([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print("Original queue:", end=" ")
displayQueue(q2)
interleaveQueue(q2)
print("Interleaved queue:", end=" ")
displayQueue(q2)


'''
Time Complexity: O(n)

Reason:
The first half is moved once to another queue, then each element is appended
back in interleaved order.

Space Complexity: O(n)

Reason:
The auxiliary queue stores n / 2 elements, which is O(n).
'''
