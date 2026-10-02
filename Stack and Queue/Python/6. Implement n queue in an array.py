from collections import deque


class NQueuesInArray:
    def __init__(self, size):
        self.vec = [-1] * size
        self.free_indices = []
        self.queue_map = {}

        for i in range(size):
            self.free_indices.append(i)

    def enqueue(self, queue_num, value):
        if len(self.free_indices) == 0:
            print("Queue Overflow")
            return

        index = self.free_indices[-1]
        self.free_indices.pop()

        self.vec[index] = value
        if queue_num not in self.queue_map:
            self.queue_map[queue_num] = deque()
        self.queue_map[queue_num].append(index)

    def dequeue(self, queue_num):
        if queue_num not in self.queue_map or len(self.queue_map[queue_num]) == 0:
            print("Queue Underflow")
            return -1

        front_index = self.queue_map[queue_num][0]
        self.queue_map[queue_num].popleft()

        value = self.vec[front_index]
        self.vec[front_index] = -1

        self.free_indices.append(front_index)

        return value

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
