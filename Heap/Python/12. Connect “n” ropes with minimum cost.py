import heapq


def minCost(arr, n):
    minHeap = []
    totalCost = 0
    for i in range(n):
        heapq.heappush(minHeap, arr[i])
    while len(minHeap) > 1:
        firstMin = heapq.heappop(minHeap)
        secondMin = heapq.heappop(minHeap)
        cost = firstMin + secondMin
        totalCost += cost
        heapq.heappush(minHeap, cost)
    return totalCost


def main():
    arr = [4, 3, 2, 6]
    n = len(arr)
    result = minCost(arr, n)
    print("The minimum cost to combine all elements is:", result)


if __name__ == "__main__":
    main()


'''
Let n be the number of ropes.
Time: O(n log(n+1)): n individual heap pushes, then n-1 merges, each
using two pops and one push costing O(log n). Each merge reduces count by 1.
Space: O(n) auxiliary for heap entries. Zero or one rope costs zero;
the lengths are assumed nonnegative.
'''
