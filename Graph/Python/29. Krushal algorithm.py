import heapq
import sys


# using loop
def findparent(element, ds):
    while element != ds[element]:
        ds[element] = ds[ds[element]]
        element = ds[element]
    return element


# Function to find the parent of a node using path compression
def findparentRecursive(element, ds):
    if element == ds[element]:
        return element
    ds[element] = findparentRecursive(ds[element], ds)
    return ds[element]


# Function to execute Kruskal's Algorithm and return the total weight of the MST
def kruskal_mst(V, adj):
    # Disjoint set for union-find
    ds = list(range(V))
    # Rank array for union by rank
    rank = [1] * V
    pq = []
    # Input graph edges from the adjacency list into the priority queue
    for u in range(V):
        for edge in adj[u]:
            v, weight = edge
            heapq.heappush(pq, (weight, (u, v)))
    # Count of edges in the MST
    count = 0
    # Sum of weights of edges in the MST
    sum = 0
    # While MST does not contain V-1 edges
    while count < V - 1 and pq:
        dist, (u, v) = heapq.heappop(pq)
        # Find the parent of u
        p1 = findparent(u, ds)
        # Find the parent of v
        p2 = findparent(v, ds)
        # If u and v belong to different sets, add the edge to MST
        # parents are different, so they are not in the same set i.e no cycle
        if p1 != p2:
            # Union by rank
            if rank[p1] < rank[p2]:
                # Make p2 the parent of p1
                ds[p1] = p2
            elif rank[p2] < rank[p1]:
                # Make p1 the parent of p2
                ds[p2] = p1
            else:
                ds[p1] = p2
                # Increase rank of p2 as both were same rank
                rank[p2] += 1
            # Add edge weight to the total sum
            sum += dist
            # Increase the edge count for MST
            count += 1
            # Output the edge added to the MST
            print(f"Edge included in MST: {u} -> {v} with weight {dist}")
    # Return the total weight of the MST
    return sum


class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


class Solution:
    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        edges = []
        for i in range(V):
            for it in adj[i]:
                adjNode, wt = it
                node = i
                edges.append((wt, (node, adjNode)))
        ds = DisjointSet(V)
        edges.sort()
        mstWt = 0
        for wt, (u, v) in edges:
            if ds.findUPar(u) != ds.findUPar(v):
                mstWt += wt
                ds.unionBySize(u, v)
        return mstWt


def mainDisjointSet():
    V = 5
    edges = [[0, 1, 2], [0, 2, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 2, 2]]
    adj = [[] for _ in range(V)]
    for it in edges:
        tmp = [it[1], it[2]]
        adj[it[0]].append(tmp)
        tmp = [it[0], it[2]]
        adj[it[1]].append(tmp)
    obj = Solution()
    mstWt = obj.spanningTree(V, adj)
    print("The sum of all the edge weights:", mstWt)


def main():
    tokens = iter(sys.stdin.read().split())
    print("Enter the number of vertices: ", end="")
    V = int(next(tokens))
    print("Enter the number of edges: ", end="")
    E = int(next(tokens))
    adj = [[] for _ in range(V)]
    print("Enter edges in the format (u v weight):")
    for i in range(E):
        u = int(next(tokens))
        v = int(next(tokens))
        weight = int(next(tokens))
        adj[u].append([v, weight])
        adj[v].append([u, weight])
    mstWeight = kruskal_mst(V, adj)
    print("Total weight of the Minimum Spanning Tree:", mstWeight)


if __name__ == "__main__":
    main()


'''
Let V/E be vertex/undirected edge counts; each edge appears twice in adj.
Time: O(V + E log(E+1)) for both variants: heap insertion/removal or
sorting dominates union-find operations, amortized O(alpha(V)) each
with path compression and rank/size balancing.
Space: O(V + E) auxiliary DSU arrays and edge heap/list; recursive find
adds O(log V) stack under balanced unions, iterative find uses O(1).
Disconnected graphs return the minimum spanning FOREST weight, as in source.
Both find alternatives and both Kruskal implementations are preserved.
'''
