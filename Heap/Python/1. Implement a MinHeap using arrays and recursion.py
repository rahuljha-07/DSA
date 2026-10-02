class MinHeap:
    def __init__(self, arr):
        self.heap = list(arr)
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.minHeapify(i)

    def minHeapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.minHeapify(smallest)

    def insert(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i != 0 and self.heap[(i - 1) // 2] > self.heap[i]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def removeMin(self):
        if not self.heap:
            return
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.minHeapify(0)

    def getMin(self):
        if self.heap:
            return self.heap[0]
        return -1

    def printHeap(self):
        for val in self.heap:
            print(val, end=" ")
        print()


def main():
    arr = [40, 30, 15, 20, 10]
    minHeap = MinHeap(arr)
    print("MinHeap elements after building from array: ", end="")
    minHeap.printHeap()
    print("Minimum element:", minHeap.getMin())
    minHeap.removeMin()
    print("After removing minimum element: ", end="")
    minHeap.printHeap()


if __name__ == "__main__":
    main()


'''
Let n be the number of stored elements.
Time: insert/removeMin are O(log n) amortized/worst-case respectively:
a value moves through at most the heap's O(log n) levels. Python list
append is amortized O(1); an individual resize can cost O(n).
getMin is O(1); printHeap is O(n).
Constructor build is O(n): most nodes are near the leaves and need little
sifting; summing work by node height is linear, not O(n log n).
Space: O(n) for heap storage, copied from arr; heapify adds O(log n) recursive
auxiliary space, while insert uses O(1) auxiliary space.
'''
