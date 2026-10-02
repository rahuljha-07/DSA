class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty, cannot dequeue.")
            return
        self.data.pop(0)

    def getFront(self):
        if not self.isEmpty():
            return self.data[0]
        else:
            print("Queue is empty, cannot access front.")
            return -1

    def isEmpty(self):
        return len(self.data) == 0

    def size(self):
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
