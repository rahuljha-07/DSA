from collections import deque


class NQueuesInArray:
    # Constructor initializes the list and free_indices
    def __init__(self, size):
        # Initialize the array with -1
        self.vec = [-1] * size
        self.free_indices = []
        self.queue_map = {}

        for i in range(size):
            # Initially, all indices are free
            self.free_indices.append(i)

    # Enqueue a value in the specified queue
    def enqueue(self, queue_num, value):
        if len(self.free_indices) == 0:
            print("Queue Overflow")
            return

        # Get an available index from free_indices
        index = self.free_indices[-1]
        self.free_indices.pop()

        # Place the value in vec and record the index in queue_map
        self.vec[index] = value
        if queue_num not in self.queue_map:
            self.queue_map[queue_num] = deque()
        # Using deque for O(1) enqueue at back
        self.queue_map[queue_num].append(index)

    # Dequeue a value from the specified queue
    def dequeue(self, queue_num):
        if queue_num not in self.queue_map or len(self.queue_map[queue_num]) == 0:
            print("Queue Underflow")
            return -1

        # Get the first index for this queue
        front_index = self.queue_map[queue_num][0]
        # O(1) with deque
        self.queue_map[queue_num].popleft()

        # Retrieve the value at this index
        value = self.vec[front_index]
        # Optional: reset the value
        self.vec[front_index] = -1

        # Mark this index as free
        self.free_indices.append(front_index)

        return value

    # Get the front value of the specified queue
    def front(self, queue_num):
        if queue_num not in self.queue_map or len(self.queue_map[queue_num]) == 0:
            print("Queue is Empty")
            return -1

        front_index = self.queue_map[queue_num][0]
        return self.vec[front_index]


queues = NQueuesInArray(10)
queues.enqueue(1, 10)
queues.enqueue(2, 20)
queues.enqueue(1, 15)

print("Front of queue 1:", queues.front(1))
print("Dequeued from queue 1:", queues.dequeue(1))
print("Front of queue 1:", queues.front(1))
print("Dequeued from queue 2:", queues.dequeue(2))
print("Dequeued from queue 2:", queues.dequeue(2))


'''
Time Complexity: O(1) average for enqueue, dequeue, and front

Reason:
The implementation uses a free-index list and deque for each queue, so adding
at the back and removing from the front are O(1). Dictionary lookup is O(1)
on average.

Space Complexity: O(size)

Reason:
The shared array, free index list, and queue index deques store information
for the fixed number of available slots.
'''
