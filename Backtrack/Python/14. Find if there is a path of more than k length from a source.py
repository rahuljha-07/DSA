def dfs(adj, visited, src, k):
    if k <= 0:
        return True
    visited[src] = True
    for neighbor in adj[src]:
        v, weight = neighbor
        if not visited[v]:
            if dfs(adj, visited, v, k - weight):
                return True
    visited[src] = False
    return False


def pathMoreThanK(V, adj, src, k):
    visited = [False] * V
    return dfs(adj, visited, src, k)


def main():
    V = 9
    adj = [[] for _ in range(V)]
    for u, v, weight in [(0,1,4), (0,7,8), (1,7,11), (1,2,8), (2,8,2),
                         (2,5,4), (2,3,7), (3,4,9), (3,5,14), (4,5,10),
                         (5,6,2), (6,8,6), (6,7,1), (7,8,7)]:
        adj[u].append((v, weight))
        adj[v].append((u, weight))
    src = 0
    k = 58
    print("True" if pathMoreThanK(V, adj, src, k) else "False")


if __name__ == "__main__":
    main()


'''
Let V be vertices and Delta maximum degree.
Time: exponential, bounded conservatively by O(Delta^V), or O(V*V!)
for a dense simple graph including neighbor scans: vertices are unmarked
on backtracking, so many simple paths revisit the same vertex.
Space: O(V) auxiliary visited and recursion, excluding input adjacency.
As in the source, success means path weight AT LEAST k, not strictly
more than k. Assumes nonnegative edge weights and a valid source.
'''
