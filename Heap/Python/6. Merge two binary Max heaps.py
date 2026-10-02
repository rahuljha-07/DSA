def heapify(arr, n, i):
    if i >= n:
        return
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def buildheap(arr, n):
    start = n // 2 - 1
    for i in range(start, -1, -1):
        heapify(arr, n, i)


def mergeHeaps(merged, a, b, n, m):
    for i in range(n):
        merged[i] = a[i]
    for i in range(m):
        merged[n + i] = b[i]
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
