from collections import deque


class Stack:
    def __init__(self):
        self.dq = deque()

    # Push an element onto the stack
    def push(self, value):
        # Insert at the back
        self.dq.append(value)

    # Pop the top element from the stack
    def pop(self):
        if len(self.dq) == 0:
            print("Stack Underflow")
            return
        self.dq.pop()

    # Get the top element of the stack
    def top(self):
        if len(self.dq) == 0:
            print("Stack is empty")
            return -1
        # Return the last element
        return self.dq[-1]

    # Check if the stack is empty
    def empty(self):
        return len(self.dq) == 0


class Queue:
    def __init__(self):
        self.dq = deque()

    # Enqueue an element into the queue
    def enqueue(self, value):
        self.dq.append(value)

    # Dequeue the front element from the queue
    def dequeue(self):
        if len(self.dq) == 0:
            print("Queue Underflow")
            return
        # Remove from the front
        self.dq.popleft()

    # Get the front element of the queue
    def front(self):
        if len(self.dq) == 0:
            print("Queue is empty")
            return -1
        # Return the first element
        return self.dq[0]

    # Check if the queue is empty
    def empty(self):
        return len(self.dq) == 0


stack = Stack()
stack.push(10)
stack.push(20)
print("Top of stack:", stack.top())
stack.pop()
print("Top of stack after pop:", stack.top())

queue = Queue()
queue.enqueue(30)
queue.enqueue(40)
print("Front of queue:", queue.front())
queue.dequeue()
print("Front of queue after dequeue:", queue.front())


'''
Time Complexity: O(1) for all shown stack and queue operations

Reason:
Deque supports append, pop, append at back, and pop from front in O(1).

Space Complexity: O(n)

Reason:
The deque stores n elements.
'''
