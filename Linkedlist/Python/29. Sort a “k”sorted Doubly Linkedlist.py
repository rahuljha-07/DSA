import heapq


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


# Function to sort a nearly sorted doubly linked list
def sortNearlySortedDLL(head, k):
    if not head:
        return None
    if k < 0:
        raise ValueError("k must be nonnegative")
    minHeap = []
    newHead = None
    lastSorted = None
    curr = head
    # Traverse the list and maintain the min-heap with a max size of `k+1`
    while curr:
        heapq.heappush(minHeap, curr.data)
        # If heap size exceeds `k`, pop the minimum element and add it to the sorted list
        if len(minHeap) > k:
            minData = heapq.heappop(minHeap)
            # Create new node and add to sorted list
            newNode = Node(minData)
            if not newHead:
                newHead = newNode
                lastSorted = newHead
            else:
                lastSorted.next = newNode
                newNode.prev = lastSorted
                lastSorted = newNode
        curr = curr.next
    # Empty the remaining elements in the heap
    while minHeap:
        minData = heapq.heappop(minHeap)
        newNode = Node(minData)
        if not newHead:
            newHead = newNode
            lastSorted = newHead
        else:
            lastSorted.next = newNode
            newNode.prev = lastSorted
            lastSorted = newNode
    return newHead


'''
Let n be the node count and h = min(n, k + 1), with k >= 0.
Time: O(n log(h + 1)): every value is pushed and popped once, and the
heap contains at most h values. The +1 keeps the bound valid for k = 0,
when heap operations are constant-time and total work is O(n).
Space: O(h) auxiliary for the heap; O(n) output for a newly allocated DLL.
The input must be k-sorted (each value at most k positions from its place).
'''
