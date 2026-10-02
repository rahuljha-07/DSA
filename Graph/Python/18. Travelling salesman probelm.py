def tspBacktrack(cost, visited, currCity, n, count, currCost, minCost):
    if count == n:
        if n == 1 or cost[currCity][0] > 0:
            currCost += cost[currCity][0]
            minCost[0] = min(minCost[0], currCost)
        return
    for nextCity in range(n):
        if not visited[nextCity] and cost[currCity][nextCity] > 0:
            visited[nextCity] = True
            tspBacktrack(cost, visited, nextCity, n, count + 1,
                         currCost + cost[currCity][nextCity], minCost)
            visited[nextCity] = False


def travellingSalesman(cost):
    n = len(cost)
    if n == 0:
        return 0
    visited = [False] * n
    visited[0] = True
    minCost = [float("inf")]
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
