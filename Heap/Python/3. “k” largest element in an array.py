import heapq


def findKthLargest(nums, k):
    if not 1 <= k <= len(nums):
        raise ValueError("k must be between 1 and the array length")
    minHeap = []
    # Counter to track the number of elements added to the heap
    counter = 0
    # Iterate through all elements in the array
    for num in nums:
        heapq.heappush(minHeap, num)
        # Increment counter after adding an element
        counter += 1
        # Once we have more than k elements, remove the smallest element
        if counter > k:
            heapq.heappop(minHeap)
    # The root of the heap now contains the k-th largest element
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
