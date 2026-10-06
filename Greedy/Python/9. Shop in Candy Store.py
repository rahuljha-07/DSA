# Function to calculate the minimum and maximum cost
def candyStore(candies, n, k):
    # Sort the candies prices in ascending order
    candies.sort()
    # Calculate minimum cost
    minCost = 0
    left, right = 0, n - 1
    while left <= right:
        # Buy candy from the start
        minCost += candies[left]
        # Move to the next candy to buy
        # Pointer to get candies for free from the start
        left += 1
        # Take k candies for free
        right -= k
    # Calculate maximum cost
    maxCost = 0
    left, right = 0, n - 1
    while left <= right:
        # Buy candy from the end
        maxCost += candies[right]
        # Pointer to buy candies from the end
        right -= 1
        left += k
    return minCost, maxCost


def main():
    n = 4
    k = 2
    candies = [3, 2, 1, 4]
    result = candyStore(candies, n, k)
    print("Minimum cost:", result[0])
    print("Maximum cost:", result[1])


if __name__ == "__main__":
    main()


'''
Let n be element count.
Time: O(n log(n+1)): sorting dominates the subsequent O(n) scan.
Space: O(n) auxiliary worst case for Python's sorting workspace, even
when the input list is sorted in place; no full result array is returned.
Here n=len(candies) and k>=0. Each buying pass uses about ceil(n/(k+1))
iterations, treating up to k opposite-end candies as free.
candies is reordered; returned min/max costs occupy O(1) output space.
'''
