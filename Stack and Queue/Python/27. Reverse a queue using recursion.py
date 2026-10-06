from collections import deque


# Function to print the elements of the queue (for demonstration)
def printQueue(q):
    temp = deque(q)
    while len(temp) != 0:
        print(temp[0], end=" ")
        temp.popleft()
    print()


# Recursive function to reverse the queue
def performReverse(q):
    # Base case: If the queue is empty, return
    if len(q) == 0:
        return

    # Recursive case: Remove the front element
    frontElement = q[0]
    q.popleft()

    # Recursive call to reverse the remaining queue
    performReverse(q)

    # Add the removed element to the rear of the queue
    q.append(frontElement)


# Function to reverse the queue using recursion
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
