import heapq


def findKthSmallestAndLargest(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("k must be between 1 and the array length")
    minHeap = []
    maxHeap = []
    counter = 0
    for num in nums:
        heapq.heappush(minHeap, num)
        heapq.heappush(maxHeap, -num)
        counter += 1
        if counter > k:
            heapq.heappop(minHeap)
            heapq.heappop(maxHeap)
    return -maxHeap[0], minHeap[0]


def main():
    arr = [3, 2, 1, 5, 6, 4]
    k = 2
    result = findKthSmallestAndLargest(arr, k)
    print(f"The {k}th smallest element is: {result[0]}")
    print(f"The {k}th largest element is: {result[1]}")


if __name__ == "__main__":
    main()


'''
Let n be the array length and 1 <= k <= n.
Time: O(n log(k+1)): every value enters both bounded heaps and triggers
at most two pops; the constant factor of two does not change the bound.
Space: O(k) auxiliary for two heaps of at most k+1 values.
Negation implements a max-heap with Python heapq: it keeps the k smallest,
while minHeap keeps the k largest. Returned pair uses O(1) output space.
'''
