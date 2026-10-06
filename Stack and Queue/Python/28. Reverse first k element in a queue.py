from collections import deque


# Function to reverse the first k elements of a queue
def modifyQueue(q, k):
    q = deque(q)
    s = []

    # Step 1: Push the first k elements into the stack
    for i in range(k):
        # Push the front element onto the stack
        s.append(q[0])
        # Remove the front element from the queue
        q.popleft()

    # Step 2: Pop from the stack and enqueue back to the queue
    while len(s) != 0:
        # Push the top element from the stack to the queue
        q.append(s[-1])
        # Remove the top element from the stack
        s.pop()

    # Step 3: Move the remaining elements (n - k) to the back of the queue
    # Get the current size of the queue
    n = len(q)
    for i in range(n - k):
        # Move the front element to the back
        q.append(q[0])
        # Remove the front element
        q.popleft()

    # Return the modified queue
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

Space Complexity: O(n + k), which is O(n) for 0 <= k <= n

Reason:
Copying the queue stores n elements, preserving C++'s pass-by-value behavior.
The stack additionally stores the first k elements during reversal.
'''
