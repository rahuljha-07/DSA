def candyStore(candies, n, k):
    candies.sort()
    minCost = 0
    left, right = 0, n - 1
    while left <= right:
        minCost += candies[left]
        left += 1
        right -= k
    maxCost = 0
    left, right = 0, n - 1
    while left <= right:
        maxCost += candies[right]
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
