# Function to maintain the max heap property for a given subtree rooted at index 'i'
def heapify(arr, n, i):
    # If index 'i' is out of bounds, return
    if i >= n:
        return
    # Assume the largest element is at the root of the subtree
    largest = i
    # Left child index
    l = 2 * i + 1
    # Right child index
    r = 2 * i + 2
    # If the left child exists and is greater than the root, update 'largest'
    if l < n and arr[l] > arr[largest]:
        largest = l
    # If the right child exists and is greater than the root (or left child), update
    # 'largest'
    if r < n and arr[r] > arr[largest]:
        largest = r
    # If the root is not the largest, swap it with the largest and recursively heapify the
    # affected subtree
    if largest != i:
        # Swap the root with the largest child
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively apply heapify to the affected subtree
        heapify(arr, n, largest)


# Function to build a max heap from an unsorted array
def buildheap(arr, n):
    # Start from the last non-leaf node (n/2 - 1)
    start = n // 2 - 1
    for i in range(start, -1, -1):
        # Apply heapify to each node starting from the last non-leaf node
        heapify(arr, n, i)


# Function to merge two heaps into one heap
def mergeHeaps(merged, a, b, n, m):
    # Copy elements of heap 'a' into the 'merged' array
    for i in range(n):
        merged[i] = a[i]
    for i in range(m):
        merged[n + i] = b[i]
    # Build a max heap from the 'merged' array (after combining both heaps)
    buildheap(merged, n + m)


def main():
    a = [10, 5, 6, 2]
    b = [8, 7, 3, 4]
    n = len(a)
    m = len(b)
    merged = [0] * (n + m)
    mergeHeaps(merged, a, b, n, m)
    print("Merged heap:", *merged)


if __name__ == "__main__":
    main()


'''
Let N = n + m be the combined heap size.
Time: O(N): copying costs O(N); bottom-up heap construction is O(N)
because most nodes sift down very few levels (height-weighted work sums
linearly). It is not equivalent to inserting N elements separately.
Space: O(log N) auxiliary for recursive heapify, plus O(N) output
in the caller-supplied merged array.
'''
