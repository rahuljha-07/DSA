from collections import deque


class Stack:
    def __init__(self):
        self.dq = deque()

    def push(self, value):
        self.dq.append(value)

    def pop(self):
        if len(self.dq) == 0:
            print("Stack Underflow")
            return
        self.dq.pop()

    def top(self):
        if len(self.dq) == 0:
            print("Stack is empty")
            return -1
        return self.dq[-1]

    def empty(self):
        return len(self.dq) == 0


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        if len(self.dq) == 0:
            print("Queue Underflow")
            return
        self.dq.popleft()

    def front(self):
        if len(self.dq) == 0:
            print("Queue is empty")
            return -1
        return self.dq[0]

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
