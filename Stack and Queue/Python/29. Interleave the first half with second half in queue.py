from collections import deque


# Function to interleave the first half with the second half of a queue
def interleaveQueue(q):
    if len(q) % 2 != 0:
        print("Queue size must be even for interleaving.")
        return

    n = len(q)
    halfSize = n // 2
    firstHalf = deque()

    # Step 1: Move the first half of elements to another queue
    for i in range(halfSize):
        firstHalf.append(q[0])
        q.popleft()

    # Step 2: Interleave elements from firstHalf and secondHalf (remaining q elements)
    while len(firstHalf) != 0:
        # First half element
        q.append(firstHalf[0])
        firstHalf.popleft()

        # Second half element
        q.append(q[0])
        q.popleft()


# Function to display the elements of the queue
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
