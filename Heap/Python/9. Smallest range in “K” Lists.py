import heapq
import builtins


def findSmallestRange(arr, n, k):
    if k <= 0 or n <= 0 or any(len(arr[i]) < n for i in builtins.range(k)):
        raise ValueError("Each of the k lists must contain at least n values")
    minHeap = []
    ans = None
    range = float("inf")
    maxi = float("-inf")
    for i in builtins.range(k):
        heapq.heappush(minHeap, (arr[i][0], (i, 0)))
        maxi = max(maxi, arr[i][0])
    while minHeap:
        temp = heapq.heappop(minHeap)
        mini = temp[0]
        row = temp[1][0]
        col = temp[1][1]
        if maxi - mini < range:
            range = maxi - mini
            ans = (mini, maxi)
        col += 1
        if col < n:
            heapq.heappush(minHeap, (arr[row][col], (row, col)))
            maxi = max(maxi, arr[row][col])
        else:
            break
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
