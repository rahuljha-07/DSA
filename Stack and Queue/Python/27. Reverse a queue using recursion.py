from collections import deque


def printQueue(q):
    temp = deque(q)
    while len(temp) != 0:
        print(temp[0], end=" ")
        temp.popleft()
    print()


def performReverse(q):
    if len(q) == 0:
        return

    frontElement = q[0]
    q.popleft()

    performReverse(q)

    q.append(frontElement)


def reverseQueue(q):
    performReverse(q)


q = deque()
q.append(1)
q.append(2)
q.append(3)

print("Queue before reverse:", end=" ")
printQueue(q)
reverseQueue(q)
print("Queue after reverse:", end=" ")
printQueue(q)


'''
Time Complexity: O(n)

Reason:
Each queue element is removed once and appended once during recursion.

Space Complexity: O(n)

Reason:
The recursion stack can contain n calls.
'''
