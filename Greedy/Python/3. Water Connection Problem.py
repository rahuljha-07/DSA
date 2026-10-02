class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


def compare(a, b):
    return a.weight < b.weight


class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


def waterConnectionProblem(n, p, a, b, d, wellCost):
    edges = []
    for i in range(p):
        edges.append(Edge(a[i], b[i], d[i]))
    for i in range(1, n + 1):
        edges.append(Edge(0, i, wellCost[i - 1]))
    edges.sort(key=lambda a: a.weight)
    dsu = DSU(n)
    totalCost = 0
    mstEdges = []
    for edge in edges:
        u, v, weight = edge.u, edge.v, edge.weight
        if dsu.find(u) != dsu.find(v):
            dsu.unite(u, v)
            totalCost += weight
            mstEdges.append(edge)
    print("Total cost of water connections:", totalCost)
    print("MST edges (Tank, Tap, Diameter/Cost):")
    for edge in mstEdges:
        if edge.u == 0:
            print(f"Well dug at house {edge.v} with cost {edge.weight}")
        else:
            print(edge.u, edge.v, edge.weight)


def main():
    n = 9
    p = 6
    a = [7, 5, 4, 2, 9, 3]
    b = [4, 9, 6, 8, 7, 1]
    d = [98, 72, 10, 22, 17, 66]
    wellCost = [5, 8, 12, 15, 10, 8, 6, 4, 7]
    waterConnectionProblem(n, p, a, b, d, wellCost)


if __name__ == "__main__":
    main()


'''
Let n be houses, p pipes, and E=n+p including virtual well edges.
Time: O(E log(E+1)): sort E costs, then Kruskal DSU operations take
amortized O(alpha(n)) each with path compression/rank balancing.
Space: O(n+p) auxiliary edges, DSU arrays, chosen edges, and sorting workspace.
Retains the SOURCE problem variant: minimum-cost water supply using wells
and pipes, not the traditional tank/tap chain-diameter problem.
'''
