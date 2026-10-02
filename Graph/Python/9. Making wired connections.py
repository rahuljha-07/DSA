def dfsUtil(node, adj, visited):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfsUtil(neighbor, adj, visited)


def makeConnected(n, connections):
    if n <= 1:
        return 0
    if len(connections) < n - 1:
        return -1
    adj = [[] for _ in range(n)]
    for conn in connections:
        adj[conn[0]].append(conn[1])
        adj[conn[1]].append(conn[0])
    visited = [False] * n
    components = 0
    for i in range(n):
        if not visited[i]:
            components += 1
            dfsUtil(i, adj, visited)
    totalEdges = len(connections)
    minEdgesNeeded = n - components
    neededBridges = components - 1
    extraEdges = totalEdges - minEdgesNeeded
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
