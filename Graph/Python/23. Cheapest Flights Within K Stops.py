import heapq


def findCheapestPrice(n, flights, src, dst, K):
    # Step 1: Build the adjacency list
    graph = [[] for _ in range(n)]
    for flight in flights:
        u, v, w = flight
        # Store each directed flight together with its price.
        graph[u].append((v, w))
    # Push initial state (0 cost, src, 0 stops)
    pq = [(0, src, 0)]
    # Different flight counts must remain separate states.
    dist = [[float("inf")] * (K + 2) for _ in range(n)]
    dist[src][0] = 0
    # Explore states in increasing total cost using the priority queue.
    while pq:
        cost, node, stops = heapq.heappop(pq)
        # Ignore a queued state superseded by a cheaper path with the same flight count.
        if cost != dist[node][stops]:
            continue
        # If we reach the destination, return the cost
        if node == dst:
            return cost
        # If stops exceed K, continue to the next iteration
        if stops > K:
            continue
        # Explore neighbors
        for neighbor in graph[node]:
            nextNode, price = neighbor
            # Only proceed if this path offers a cheaper cost
            if cost + price < dist[nextNode][stops + 1]:
                dist[nextNode][stops + 1] = cost + price
                heapq.heappush(pq, (cost + price, nextNode, stops + 1))
    # If no route is found, return -1
    return -1


def main():
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [0, 2, 500]]
    src = 0
    dst = 3
    K = 1
    print("Cheapest Price:", findCheapestPrice(n, flights, src, dst, K))


if __name__ == "__main__":
    main()


'''
Let n be cities, E flights, and K>=0 the maximum intermediate stops.
Time: O(n*(K+2) + (K+1)*E*log((K+1)*E+2)): initialize city/flight-count
distances; each finalized state scans outgoing flights, with at most
O((K+1)*E) heap relaxations. Flight prices must be nonnegative.
Space: O(n*(K+2) + E + (K+1)*E) auxiliary table, graph, and lazy heap.
The original heap approach is retained, but a distance per flight count
is necessary: a cheaper route using too many flights cannot suppress a
costlier state that can still reach dst within the stop limit.
'''
