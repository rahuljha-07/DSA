class QueueUsingStacks:
    def __init__(self):
        self.input = []
        self.output = []

    # Enqueue an element into the queue
    def enqueue(self, value):
        self.input.append(value)

    def _transfer(self):
        while len(self.input) != 0:
            self.output.append(self.input[-1])
            self.input.pop()

    # Dequeue an element from the queue
    def dequeue(self):
        if len(self.output) == 0:
            if len(self.input) == 0:
                print("Queue Underflow")
                return -1
            self._transfer()

        # Pop from output stack, which represents the front of the queue
        front = self.output[-1]
        self.output.pop()
        return front

    # Get the front element of the queue
    def front(self):
        if len(self.output) == 0:
            if len(self.input) == 0:
                print("Queue is Empty")
                return -1
            self._transfer()

        # Front of the queue is the top of output stack
        return self.output[-1]

    # Check if the queue is empty
    def empty(self):
        return len(self.input) == 0 and len(self.output) == 0


queue = QueueUsingStacks()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front of queue:", queue.front())
print("Dequeued:", queue.dequeue())
print("Front of queue:", queue.front())
print("Dequeued:", queue.dequeue())

queue.enqueue(40)
print("Front of queue:", queue.front())
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())

if queue.empty():
    print("Queue is empty")


'''
Time Complexity: O(1) amortized per operation

Reason:
Each element moves from input stack to output stack at most once, then is
popped once. A single dequeue can be O(n), but averaged over operations it is O(1).

Space Complexity: O(n)

Reason:
The two stacks together store all queue elements.
'''
