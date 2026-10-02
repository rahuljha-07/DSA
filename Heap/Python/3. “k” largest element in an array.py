import heapq


def findKthLargest(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("k must be between 1 and the array length")
    minHeap = []
    counter = 0
    for num in nums:
        heapq.heappush(minHeap, num)
        counter += 1
        if counter > k:
            heapq.heappop(minHeap)
    return minHeap[0]


def main():
    arr = [3, 2, 1, 5, 6, 4]
    k = 2
    kthLargest = findKthLargest(arr, k)
    print(f"The {k}th largest element is: {kthLargest}")


if __name__ == "__main__":
    main()


'''
Let n be the array length and 1 <= k <= n.
Time: O(n log(k+1)): each value is pushed once and at most one minimum
is popped, with heap size at most k+1. For k=1 this is O(n).
Space: O(k) auxiliary: the min-heap keeps the k largest seen values;
its minimum is the kth largest. No sorted n-value copy is made.
'''
