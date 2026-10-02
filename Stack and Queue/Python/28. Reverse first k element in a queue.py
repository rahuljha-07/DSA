from collections import deque


def modifyQueue(q, k):
    s = []

    for i in range(k):
        s.append(q[0])
        q.popleft()

    while len(s) != 0:
        q.append(s[-1])
        s.pop()

    n = len(q)
    for i in range(n - k):
        q.append(q[0])
        q.popleft()

    return q


q = deque([1, 2, 3, 4, 5])
k = 3
print("Original queue:", *q)
q = modifyQueue(q, k)
print("Modified queue after reversing first", k, "elements:", *q)


'''
Time Complexity: O(n)

Reason:
The first k elements are moved to a stack and back, then the remaining n-k
elements are rotated once.

Space Complexity: O(k)

Reason:
The stack stores the first k queue elements.
'''
