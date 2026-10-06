# Helper function to perform DFS traversal
def dfsUtil(node, adj, visited):
    # Mark the current node as visited
    visited[node] = True
    # Visit all neighbors of the current node
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfsUtil(neighbor, adj, visited)


# Function to count connected components and determine redundancy
def makeConnected(n, connections):
    if n <= 1:
        return 0
    # Not enough connections to connect all nodes
    if len(connections) < n - 1:
        return -1
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for conn in connections:
        adj[conn[0]].append(conn[1])
        adj[conn[1]].append(conn[0])
    # Count connected components using DFS
    visited = [False] * n
    components = 0
    for i in range(n):
        if not visited[i]:
            components += 1
            # Perform DFS from this node
            dfsUtil(i, adj, visited)
    # Total number of existing cables
    totalEdges = len(connections)
    # The existing components need n - components edges; any others are spare cables.
    minEdgesNeeded = n - components
    # connections.size() - (n - 1)
    # This gives you how many extra (redundant) wires you have - ones forming cycles. These
    # are free to move.
    # Counted earlier: 'components' = number of separate groups (disconnected parts)
    # To connect all components into one group, we need (components - 1) connections
    # (bridges)
    neededBridges = components - 1
    # Any cables beyond the minimum are extra, meaning they form cycles and can be reused
    # elsewhere
    extraEdges = totalEdges - minEdgesNeeded
    # If we have enough extra cables to connect the groups, return how many bridges we need
    # Otherwise, return -1 because we can't connect everything
    return neededBridges if extraEdges >= neededBridges else -1


def main():
    n1 = 4
    connections1 = [[0, 1], [0, 2], [1, 2]]
    print("Output:", makeConnected(n1, connections1))
    n2 = 6
    connections2 = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
    print("Output:", makeConnected(n2, connections2))
    n3 = 6
    connections3 = [[0, 1], [0, 2], [0, 3], [1, 2]]
    print("Output:", makeConnected(n3, connections3))


if __name__ == "__main__":
    main()


'''
Let n be computer count and E cable count.
Time: O(n + E): build adjacency lists, then count components by DFS.
Space: O(n + E) auxiliary for adjacency/visited and up to n recursive calls.
A forest spanning c existing components uses n-c cables, not n-1;
this corrects the source's spare-cable count without changing its approach.
'''
