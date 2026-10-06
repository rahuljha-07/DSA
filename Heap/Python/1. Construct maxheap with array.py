class MaxHeap:
    def __init__(self):
        self.heap = []

    # Recursive function to heapify a subtree rooted at index i
    def maxHeapify(self, i):
        largest = i
        # Left child
        left = 2 * i + 1
        # Right child
        right = 2 * i + 2
        # If left child is larger than root
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        # If right child is larger than largest so far
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        # If largest is not root
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            # Recursively heapify the affected subtree
            self.maxHeapify(largest)

    # Insert a new element into the heap
    def insert(self, val):
        # Add the new element to the end of the heap
        self.heap.append(val)
        i = len(self.heap) - 1
        # Up-heapify (bubble up) to maintain the heap property
        while i != 0 and self.heap[(i - 1) // 2] < self.heap[i]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    # Remove the maximum element (root of the heap)
    def removeMax(self):
        if not self.heap:
            print("Heap is empty!")
            return
        # Move the last element to the root and remove the last element
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        # Heapify the root to restore the heap property
        self.maxHeapify(0)

    # Get the maximum element in the heap
    def getMax(self):
        if self.heap:
            return self.heap[0]
        # Indicate that the heap is empty
        return -1

    # Print all elements in the heap
    def printHeap(self):
        for val in self.heap:
            print(val, end=" ")
        print()


def main():
    maxHeap = MaxHeap()
    maxHeap.insert(10)
    maxHeap.insert(20)
    maxHeap.insert(15)
    maxHeap.insert(30)
    maxHeap.insert(40)
    print("MaxHeap elements: ", end="")
    maxHeap.printHeap()
    print("Maximum element:", maxHeap.getMax())
    maxHeap.removeMax()
    print("After removing maximum element: ", end="")
    maxHeap.printHeap()


if __name__ == "__main__":
    main()


'''
Let n be the number of stored elements.
Time: insert/removeMax are O(log n) amortized/worst-case respectively:
a value moves through at most the heap's O(log n) levels. Python list
append is amortized O(1); an individual resize can cost O(n).
getMax is O(1); printHeap is O(n).
Building by n inserts is O(n log n) worst case.
Space: O(n) for heap storage; heapify adds O(log n) recursive
auxiliary space, while insert uses O(1) auxiliary space.
'''
