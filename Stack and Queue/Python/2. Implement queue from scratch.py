class Queue:
    def __init__(self):
        self.data = []

    # Enqueue operation to add an element at the rear of the queue
    def enqueue(self, value):
        # Add element to the end of the list
        self.data.append(value)

    # Dequeue operation to remove an element from the front of the queue
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty, cannot dequeue.")
            return
        self.data.pop(0)

    # Get the front element of the queue
    def getFront(self):
        if not self.isEmpty():
            # Return the first element
            return self.data[0]
        else:
            print("Queue is empty, cannot access front.")
            # or throw an exception
            return -1

    # Check if the queue is empty
    def isEmpty(self):
        # Queue is empty if the list is empty
        return len(self.data) == 0

    # Get the current size of the queue
    def size(self):
        # Return the number of elements in the list
        return len(self.data)


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front element:", queue.getFront())
queue.dequeue()
print("Front element after dequeue:", queue.getFront())

queue.dequeue()
queue.dequeue()
queue.dequeue()


'''
Time Complexity: O(1) for enqueue, front, isEmpty, and size; O(n) for dequeue

Reason:
Appending at the end is O(1) amortized. Removing index 0 shifts all remaining
items one position left, so dequeue costs O(n), matching vector erase(begin()).

Space Complexity: O(n)

Reason:
The internal list stores n queue elements.
'''
