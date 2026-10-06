import heapq


# Function to implement Prim's algorithm and print MST
def primMST(N, adj):
    pq = [(0, (0, -1))] if N else []
    # To track visited nodes
    visited = [False] * N
    print("Edges in the MST:")
    while pq:
        # Extract the element with the smallest weight
        weight, nodePair = heapq.heappop(pq)
        node, parent = nodePair
        # If the node is already visited, skip it
        if visited[node]:
            continue
        # Mark the node as visited
        visited[node] = True
        # Print the edge if parent is not -1 (skip the initial push)
        if parent != -1:
            print(f"{parent} - {node} with weight {weight}")
        # Traverse all adjacent nodes
        for adjNode, adjWeight in adj[node]:
            if not visited[adjNode]:
                # Push {weight, {node, parent}} into the priority queue
                heapq.heappush(pq, (adjWeight, (adjNode, node)))


def main():
    N = 5
    adj = [[(1, 2), (3, 6)], [(0, 2), (2, 3), (3, 8), (4, 5)],
           [(1, 3), (4, 7)], [(0, 6), (1, 8)], [(1, 5), (2, 7)]]
    primMST(N, adj)


if __name__ == "__main__":
    main()


'''
Let V=N and E undirected edges.
Time: O(V + E log(E+1)): each visited node scans its adjacency once;
up to O(E) candidate edges are pushed/popped from the heap.
Space: O(V + E) auxiliary visited/heap, excluding input.
Like the source, starts at vertex 0 only: disconnected input yields the
spanning tree of that component, not a forest of all components.
'''
