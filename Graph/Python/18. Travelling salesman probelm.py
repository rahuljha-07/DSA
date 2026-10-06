def tspBacktrack(cost, visited, currCity, n, count, currCost, minCost):
    # Base case: If all cities are visited, return to the starting city
    if count == n:
        if n == 1 or cost[currCity][0] > 0:
            # Add the cost to return to the starting city (0)
            currCost += cost[currCity][0]
            minCost[0] = min(minCost[0], currCost)
        return
    # Explore all possible cities
    for nextCity in range(n):
        # Check if city is unvisited and valid
        if not visited[nextCity] and cost[currCity][nextCity] > 0:
            # Mark the city as visited
            visited[nextCity] = True
            # Recur with the next city
            tspBacktrack(cost, visited, nextCity, n, count + 1,
                         currCost + cost[currCity][nextCity], minCost)
            # Backtrack: Mark the city as unvisited
            visited[nextCity] = False


def travellingSalesman(cost):
    n = len(cost)
    if n == 0:
        return 0
    # To keep track of visited cities
    visited = [False] * n
    # Start from city 0
    visited[0] = True
    minCost = [float("inf")]
    # Start from city 0 with 0 cost
    tspBacktrack(cost, visited, 0, n, 1, 0, minCost)
    return minCost[0]


def main():
    cost = [[0, 10, 15, 20], [10, 0, 35, 25],
            [15, 35, 0, 30], [20, 25, 30, 0]]
    print("The minimum cost of the tour is:", travellingSalesman(cost))


if __name__ == "__main__":
    main()


'''
Let n be city count.
Time: O(n!): fixing city 0 leaves up to (n-1)! tours; scanning n potential
next cities at recursive nodes gives a factorial upper bound.
Space: O(n) auxiliary for visited and recursive depth, excluding O(n^2)
input costs. Positive entries mean edges; no tour returns infinity.
The closing edge is checked too, avoiding a false tour through a missing edge.
'''
