import sys


# Function to perform DFS and find bridges using Tarjan's Algorithm
def dfs(u, timer, disc, low, g, parent, bridges):
    # Initialize discovery and low values
    disc[u] = low[u] = timer[0]
    # Increment the timer for the next call
    timer[0] += 1
    # Explore all the adjacent vertices of u
    for v in g[u]:
        if v == parent:
            # Ignore the edge to the parent vertex
            continue
        # If v is not visited
        if disc[v] == -1:
            # Recur for the child vertex
            dfs(v, timer, disc, low, g, u, bridges)
            # After recursion, update the low-link value of u
            low[u] = min(low[u], low[v])
            # Check if the edge u-v is a bridge
            if low[v] > disc[u]:
                bridges.append((u, v))
        else:
            # If v is already visited and is not the parent, update low[u]
            low[u] = min(low[u], disc[v])


# Function to perform DFS and find articulation points using Tarjan's Algorithm
def dfsWithArticulation(u, timer, disc, low, g, parent, bridges, articulationPoints):
    disc[u] = low[u] = timer[0]
    timer[0] += 1
    # Count of children in the DFS tree
    children = 0
    for v in g[u]:
        if v == parent:
            continue
        if disc[v] == -1:
            dfsWithArticulation(v, timer, disc, low, g, u, bridges, articulationPoints)
            # Increase child count for u
            children += 1
            low[u] = min(low[u], low[v])
            if low[v] > disc[u]:
                bridges.append((u, v))
            # Check if u is an articulation point (excluding the root case separately)
            if parent != -1 and low[v] >= disc[u]:
                articulationPoints.add(u)
        else:
            low[u] = min(low[u], disc[v])
    # Special case for the root vertex
    if parent == -1 and children > 1:
        articulationPoints.add(u)


def mainWithArticulation():
    tokens = iter(sys.stdin.read().split())
    n = int(next(tokens))
    m = int(next(tokens))
    g = [[] for _ in range(n)]
    for i in range(m):
        u = int(next(tokens))
        v = int(next(tokens))
        g[u].append(v)
        g[v].append(u)
    for i in range(n):
        g[i].sort()
    disc = [-1] * n
    low = [-1] * n
    bridges = []
    timer = [0]
    articulationPoints = set()
    for i in range(n):
        if disc[i] == -1:
            dfsWithArticulation(i, timer, disc, low, g, -1, bridges, articulationPoints)
    bridges = sorted((min(u, v), max(u, v)) for u, v in bridges)
    print(len(bridges))
    for e in bridges:
        print(e[0], e[1])
    print(len(articulationPoints))
    for u in sorted(articulationPoints):
        print(u)


def main():
    tokens = iter(sys.stdin.read().split())
    n = int(next(tokens))
    m = int(next(tokens))
    g = [[] for _ in range(n)]
    for i in range(m):
        u = int(next(tokens))
        v = int(next(tokens))
        g[u].append(v)
        g[v].append(u)
    for i in range(n):
        g[i].sort()
    disc = [-1] * n
    low = [-1] * n
    bridges = []
    timer = [0]
    for i in range(n):
        if disc[i] == -1:
            dfs(i, timer, disc, low, g, -1, bridges)
    bridges = sorted((min(u, v), max(u, v)) for u, v in bridges)
    print(len(bridges))
    for e in bridges:
        print(e[0], e[1])


if __name__ == "__main__":
    main()


'''
Let V/E be vertex/edge counts and B reported bridges.
Time: O(V + E) for either low-link DFS: each vertex/edge is examined once.
Drivers additionally sort adjacency lists and bridge output, costing
O(sum(deg(v)*log(deg(v)+1)) + B log(B+1)); articulation output also sorts.
Space: O(V) auxiliary disc/low/DFS stack, plus O(B) bridge output and
O(V) articulation set. Input adjacency uses O(V + E).
Both source variants are retained. Assumes a SIMPLE undirected graph:
skipping every parent adjacency is not correct for parallel edges.
'''
