import heapq
import builtins


# Function to find the smallest range that includes at least one element from each list
def findSmallestRange(arr, n, k):
    if k <= 0 or n <= 0 or any(len(arr[i]) < n for i in builtins.range(k)):
        raise ValueError("Each of the k lists must contain at least n values")
    minHeap = []
    ans = None
    range = float("inf")
    maxi = float("-inf")
    # Step 1: Push the first element of each array into the heap
    for i in builtins.range(k):
        # (value, (row, col))
        heapq.heappush(minHeap, (arr[i][0], (i, 0)))
        maxi = max(maxi, arr[i][0])
    # Step 2: Process the heap
    while minHeap:
        temp = heapq.heappop(minHeap)
        # Current min element in the heap
        mini = temp[0]
        row = temp[1][0]
        col = temp[1][1]
        # Update range if a smaller range is found
        if maxi - mini < range:
            range = maxi - mini
            ans = (mini, maxi)
        # Step 3: Get the next element in the same row
        col += 1
        if col < n:
            heapq.heappush(minHeap, (arr[row][col], (row, col)))
            maxi = max(maxi, arr[row][col])
        else:
            # If any row runs out of elements, stop the process
            break
    # Return the smallest range found
    return ans


def main():
    arr = [[1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [2, 3, 5, 7, 11]]
    n = len(arr[0])
    k = len(arr)
    result = findSmallestRange(arr, n, k)
    print("Smallest Range:", result[0], result[1])


if __name__ == "__main__":
    main()


'''
Let k be the number of sorted lists, each with n considered elements.
Time: O(n*k log(k+1)) worst case: one candidate per list is kept, and
at most n*k candidates are popped/replaced before a list is exhausted.
Space: O(k) auxiliary for the heap; ans has O(1) output space.
maxi tracks the greatest candidate without rescanning all k candidates.
Only the first n elements of each list are considered, as in the source.
'''
