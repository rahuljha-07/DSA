import heapq


class MedianFinder:
    def __init__(self):
        self.r = []
        self.l = []

    # Function to insert a new number into the heaps
    def insertHeap(self, x):
        # If the new number is larger than the top of the right half (min-heap), it belongs
        # to the right half
        if self.r and x > self.r[0]:
            heapq.heappush(self.r, x)
        else:
            # Store negated values so heapq's min-heap behaves as a max-heap.
            heapq.heappush(self.l, -x)
        # Balance the heaps if their sizes differ by more than 1
        self.balanceHeaps()

    # Function to balance the two heaps (left max-heap and right min-heap)
    def balanceHeaps(self):
        # If the left heap has more than 1 extra element, move the top element to the right
        # heap
        if len(self.l) - len(self.r) == 2:
            # Store negated values so heapq's min-heap behaves as a max-heap.
            heapq.heappush(self.r, -heapq.heappop(self.l))
        # If the right heap has more than 1 extra element, move the top element to the left
        # heap
        elif len(self.r) - len(self.l) == 2:
            heapq.heappush(self.l, -heapq.heappop(self.r))

    # Function to return the median of the current numbers
    def getMedian(self):
        # If both heaps are empty, return -1 (this should not happen in normal usage)
        if not self.l and not self.r:
            return -1
        # If the left heap has more elements, the median is the top of the left heap
        # (max-heap)
        if len(self.l) > len(self.r):
            return -self.l[0]
        # If the right heap has more elements, the median is the top of the right heap
        # (min-heap)
        elif len(self.r) > len(self.l):
            return self.r[0]
        # If both heaps are of the same size, the median is the average of the tops of both
        # heaps
        else:
            # Return as float/double
            return (-self.l[0] + self.r[0]) / 2.0


def main():
    finder = MedianFinder()
    finder.insertHeap(1)
    print("Median after inserting 1:", finder.getMedian())
    finder.insertHeap(2)
    print("Median after inserting 2:", finder.getMedian())
    finder.insertHeap(3)
    print("Median after inserting 3:", finder.getMedian())


if __name__ == "__main__":
    main()


'''
Let n be the number of values inserted so far.
Time: O(log n) amortized per insertion: push into one heap, then at most
one pop/push moves a value to balance sizes. getMedian is O(1) because
the middle value(s) are heap roots. Processing n values is O(n log n).
Space: O(n) storage across both heaps; no values are discarded.
Negated l values implement the max-heap for the lower half.
'''
