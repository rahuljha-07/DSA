import sys


def dfs(u, timer, disc, low, g, parent, bridges):
    disc[u] = low[u] = timer[0]
    timer[0] += 1
    for v in g[u]:
        if v == parent:
            continue
        if disc[v] == -1:
            dfs(v, timer, disc, low, g, u, bridges)
            low[u] = min(low[u], low[v])
            if low[v] > disc[u]:
                bridges.append((u, v))
        else:
            low[u] = min(low[u], disc[v])


def dfsWithArticulation(u, timer, disc, low, g, parent, bridges, articulationPoints):
    disc[u] = low[u] = timer[0]
    timer[0] += 1
    children = 0
    for v in g[u]:
        if v == parent:
            continue
        if disc[v] == -1:
            dfsWithArticulation(v, timer, disc, low, g, u, bridges, articulationPoints)
            children += 1
            low[u] = min(low[u], low[v])
            if low[v] > disc[u]:
                bridges.append((u, v))
            if parent != -1 and low[v] >= disc[u]:
                articulationPoints.add(u)
        else:
            low[u] = min(low[u], disc[v])
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
