import heapq


def mergeKArrays(arr, k):
    # list to store the result
    ans = []
    q = []
    # Step 1: Push the first element of each array into the priority queue
    for i in range(k):
        if arr[i]:
            # Push (value, row index, column index) into the heap
            heapq.heappush(q, (arr[i][0], i, 0))
    # Step 2: Process the priority queue
    while q:
        temp = heapq.heappop(q)
        # Add the smallest element to the result list
        # Get the value from the tuple
        ans.append(temp[0])
        # Extract the row index and column index from the tuple
        # Row index (which array the element came from)
        row = temp[1]
        # Column index (position in the array)
        col = temp[2]
        # Step 3: If there are more elements in the current array, push the next element to
        # the heap
        # Move to the next element in the array
        col += 1
        # If the index is within the bounds of the array, push the next element into the
        # heap
        if col < len(arr[row]):
            heapq.heappush(q, (arr[row][col], row, col))
    # Step 4: Return the merged sorted array
    return ans


def mergeKArraysUsingPairs(arr, k):
    # This will store the final merged array
    ans = []
    q = []
    for i in range(k):
        if arr[i]:
            # Push the first element of each array, along with its array index and element
            # index
            heapq.heappush(q, (arr[i][0], (i, 0)))
    while q:
        temp = heapq.heappop(q)
        ans.append(temp[0])
        # Extract array index and element index from the pair
        # The index of the array
        row = temp[1][0]
        # The index of the element in the array
        col = temp[1][1]
        col += 1
        # If the index is within the array bounds, push the next element into the priority
        # queue
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
