import heapq


# Function to calculate the minimum cost of combining the elements in the array
def minCost(arr, n):
    minHeap = []
    # Variable to store the total cost
    totalCost = 0
    # Push all elements of the array into the min heap
    for i in range(n):
        heapq.heappush(minHeap, arr[i])
    # While there is more than one element in the heap, we keep combining the smallest two
    while len(minHeap) > 1:
        firstMin = heapq.heappop(minHeap)
        secondMin = heapq.heappop(minHeap)
        # Calculate the cost to combine these two elements and add it to the total cost
        cost = firstMin + secondMin
        totalCost += cost
        heapq.heappush(minHeap, cost)
    # Return the total cost of combining the elements
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
