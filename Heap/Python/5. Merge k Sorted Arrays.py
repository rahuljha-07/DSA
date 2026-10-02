import heapq


def mergeKArrays(arr, k):
    ans = []
    q = []
    for i in range(k):
        if arr[i]:
            heapq.heappush(q, (arr[i][0], i, 0))
    while q:
        temp = heapq.heappop(q)
        ans.append(temp[0])
        row = temp[1]
        col = temp[2]
        col += 1
        if col < len(arr[row]):
            heapq.heappush(q, (arr[row][col], row, col))
    return ans


def mergeKArraysUsingPairs(arr, k):
    ans = []
    q = []
    for i in range(k):
        if arr[i]:
            heapq.heappush(q, (arr[i][0], (i, 0)))
    while q:
        temp = heapq.heappop(q)
        ans.append(temp[0])
        row = temp[1][0]
        col = temp[1][1]
        col += 1
        if col < len(arr[row]):
            heapq.heappush(q, (arr[row][col], (row, col)))
    return ans


def main():
    arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    result = mergeKArrays(arrays, len(arrays))
    print(*result)


if __name__ == "__main__":
    main()


'''
Let N be the total element count and k the number of sorted arrays.
Time: O(k + N log(k+1)): inspect each array, then push/pop each element
once in a heap containing at most one candidate per nonempty array.
The O(k) term also covers many empty arrays.
Space: O(k) auxiliary heap, plus O(N) output. Both tuple representations
retain the same value/row/column merge logic and accept empty arrays.
'''
