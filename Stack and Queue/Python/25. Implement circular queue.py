class CircularQueueArray:
    def __init__(self, size):
        self.data = [0] * size
        self.front = -1
        self.rear = -1
        self.capacity = size

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, value):
        if self.isFull():
            print("Queue Overflow")
            return False
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = value
        return True

    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return True

    def getFront(self):
        if self.isEmpty():
            print("Queue is empty")
            return -1
        return self.data[self.front]

    def getRear(self):
        if self.isEmpty():
            print("Queue is empty")
            return -1
        return self.data[self.rear]


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class CircularQueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.front = newNode
            self.rear = newNode
            self.front.next = self.rear
            self.front.prev = self.rear
            self.rear.next = self.front
            self.rear.prev = self.front
        else:
            self.rear.next = newNode
            newNode.prev = self.rear
            newNode.next = self.front
            self.front.prev = newNode
            self.rear = newNode

    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
            self.front.prev = self.rear

    def getFront(self):
        if self.isEmpty():
            print("Queue is empty")
            return -1
        return self.front.data

    def getRear(self):
        if self.isEmpty():
            print("Queue is empty")
            return -1
        return self.rear.data

    def printQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        current = self.front
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.front:
                break
        print()


queue = CircularQueueArray(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
print("Front element:", queue.getFront())
print("Rear element:", queue.getRear())
queue.dequeue()
print("After one dequeue, front element:", queue.getFront())
queue.enqueue(60)
print("After enqueue 60, rear element:", queue.getRear())


'''
Time Complexity: O(1) for enqueue, dequeue, getFront, and getRear

Reason:
Both array and linked-list versions update only front/rear pointers or indexes.
No traversal is needed for basic operations.

Space Complexity: O(n)

Reason:
The array version preallocates n slots. The linked-list version stores one
node per queue element.
'''
