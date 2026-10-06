class CircularQueueArray:
    def __init__(self, size):
        self.data = [0] * size
        # -1 marks an empty array queue; modulo capacity makes indexes wrap around.
        self.front = -1
        self.rear = -1
        self.capacity = size

    # Check if the queue is empty
    def isEmpty(self):
        return self.front == -1

    # Check if the queue is full
    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front

    # Enqueue an element into the circular queue
    def enqueue(self, value):
        if self.isFull():
            print("Queue Overflow")
            return False
        if self.isEmpty():
            self.front = 0
        # Advance the rear circularly, reusing the free slots at the array's beginning.
        self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = value
        return True

    # Dequeue an element from the circular queue
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return False
        if self.front == self.rear:
            # Queue becomes empty after this dequeue
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return True

    # Get the front element of the queue
    def getFront(self):
        if self.isEmpty():
            print("Queue is empty")
            return -1
        return self.data[self.front]

    # Get the rear element of the queue
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
        # The linked-list variant uses None for an empty queue.
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.front = newNode
            self.rear = newNode
            # Point front to rear
            self.front.next = self.rear
            # The front's previous link points to the rear.
            self.front.prev = self.rear
            # Make it circular
            self.rear.next = self.front
            self.rear.prev = self.front
        else:
            # Link the new rear to both the old rear and the front, preserving the circle.
            self.rear.next = newNode
            # Link back to rear
            newNode.prev = self.rear
            # Circular link to front
            newNode.next = self.front
            # Circular link from front
            self.front.prev = newNode
            # Move rear to the new node
            self.rear = newNode

    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return

        if self.front == self.rear:
            # Only one element in the queue
            self.front = None
            self.rear = None
        else:
            # After removing the front, reconnect the rear and new front in both directions.
            self.front = self.front.next
            # Maintain circularity
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

    # Print the elements of the queue (for demonstration)
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
