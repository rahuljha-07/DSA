from collections import deque


# DFS
# Utility function to perform DFS and detect cycle
def dfsUtil(node, adj, visited, order):
    # Mark the node as visited
    visited[node] = True
    # Add the node to the current recursion stack
    order[node] = True
    # Explore all neighbors
    for neighbor in adj[node]:
        # If the neighbor is not visited, perform DFS on it
        if not visited[neighbor]:
            if dfsUtil(neighbor, adj, visited, order):
                # Cycle detected
                return True
        # If the neighbor is already in the recursion stack, a cycle exists
        elif order[neighbor]:
            return True
    # Remove the node from the recursion stack
    order[node] = False
    # No cycle detected from this node
    return False


# Function to detect a cycle in a directed graph
def isCyclic(adj):
    # Number of vertices
    V = len(adj)
    # To track visited nodes
    visited = [False] * V
    # To track nodes in the current recursion stack
    order = [False] * V
    # Check for cycles in all components of the graph
    for i in range(V):
        if not visited[i]:
            if dfsUtil(i, adj, visited, order):
                return True
    # No cycle detected
    return False


# Function to perform topological sort using BFS and detect a cycle
def hasCycleWithBFS(adj):
    V = len(adj)
    # To store in-degrees of all nodes
    indegree = [0] * V
    # Calculate in-degrees of all nodes
    for i in range(V):
        for neighbor in adj[i]:
            indegree[neighbor] += 1
    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    # To store the topological order
    topoOrder = []
    # Count of processed nodes
    count = 0
    while q:
        node = q.popleft()
        # Add the node to topological order
        topoOrder.append(node)
        count += 1
        # Decrease the in-degree of neighbors
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                # Add neighbors with in-degree 0 to the queue
                q.append(neighbor)
    # If the count of processed nodes is less than the number of vertices, there is a cycle
    if count != V:
        return True
    # Print the topological order if no cycle
    print("Topological Order:", *topoOrder)
    return False


def main():
    directedAdj = [[1, 2], [3], [3, 4], [], [5], [2]]
    print("The graph contains a cycle." if hasCycleWithBFS(directedAdj)
          else "The graph does not contain a cycle.")


if __name__ == "__main__":
    main()


'''
Let V/E be vertex/edge counts.
Time: O(V + E): each visited vertex is processed once and each adjacency
entry is examined once (twice per undirected edge).
Space: O(V) auxiliary for visited and traversal stack/queue; supplied
adjacency storage is O(V + E).
DFS distinguishes visited nodes from the current recursion path.
BFS counts indegrees and removes each edge once; fewer than V removals
means a cycle. topoOrder adds O(V) storage but not a higher space bound.
'''
