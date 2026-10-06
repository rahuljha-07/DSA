class MaxHeap:
    def __init__(self, arr):
        # Copy the array into the heap
        self.heap = list(arr)
        n = len(self.heap)
        # Perform bottom-up heap construction
        for i in range(n // 2 - 1, -1, -1):
            self.maxHeapify(i)

    # Recursive function to heapify a subtree rooted at index i
    def maxHeapify(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        # Compare with left child
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        # Compare with right child
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        # If root is not largest, swap with largest and continue heapifying
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.maxHeapify(largest)

    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        # Up-heapify (bubble up)
        while i != 0 and self.heap[(i - 1) // 2] < self.heap[i]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def removeMax(self):
        if not self.heap:
            return
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.maxHeapify(0)

    def getMax(self):
        if self.heap:
            return self.heap[0]
        # Indicate heap is empty
        return -1

    def printHeap(self):
        for val in self.heap:
            print(val, end=" ")
        print()


def main():
    arr = [10, 20, 15, 30, 40]
    maxHeap = MaxHeap(arr)
    print("MaxHeap elements after building from array: ", end="")
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
Constructor build is O(n): most nodes are near the leaves and need little
sifting; summing work by node height is linear, not O(n log n).
Space: O(n) for heap storage, copied from arr; heapify adds O(log n) recursive
auxiliary space, while insert uses O(1) auxiliary space.
'''
