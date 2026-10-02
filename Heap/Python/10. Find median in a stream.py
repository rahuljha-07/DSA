import heapq


class MedianFinder:
    def __init__(self):
        self.r = []
        self.l = []

    def insertHeap(self, x):
        if self.r and x > self.r[0]:
            heapq.heappush(self.r, x)
        else:
            heapq.heappush(self.l, -x)
        self.balanceHeaps()

    def balanceHeaps(self):
        if len(self.l) - len(self.r) == 2:
            heapq.heappush(self.r, -heapq.heappop(self.l))
        elif len(self.r) - len(self.l) == 2:
            heapq.heappush(self.l, -heapq.heappop(self.r))

    def getMedian(self):
        if not self.l and not self.r:
            return -1
        if len(self.l) > len(self.r):
            return -self.l[0]
        elif len(self.r) > len(self.l):
            return self.r[0]
        else:
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
