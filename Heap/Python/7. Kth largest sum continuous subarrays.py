import heapq


def kthLargestSum(arr, k):
    n = len(arr)
    if not 1 <= k <= n * (n + 1) // 2:
        raise ValueError("k must be between 1 and the number of subarrays")
    # Keep the source variable name, but use a min-heap to retain LARGEST sums.
    maxHeap = []
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            heapq.heappush(maxHeap, sum)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
    return maxHeap[0]


def main():
    arr = [1, 2, 3, 4, 5]
    k = 3
    print(f"The {k}-th largest sum is:", kthLargestSum(arr, k))


if __name__ == "__main__":
    main()


'''
Let n be the array length and k a valid subarray-sum rank.
Time: O(n^2 log(k+1)): nested loops enumerate n*(n+1)/2 sums; each
running-sum update is O(1), followed by bounded-heap push/pop operations.
Space: O(k) auxiliary: only k best sums are retained, not all O(n^2) sums.
The C++ max-heap discards largest values and returns kth SMALLEST; heap
direction is corrected while preserving the enumeration/bounded-heap approach.
'''
