# Function to perform DFS
def dfs(node, k, graph, visited):
    # If the accumulated path length exceeds k, return true
    if k <= 0:
        return True
    # Mark the current node as visited
    visited[node] = True
    # Explore all neighbors
    for neighbor in graph[node]:
        nextNode, weight = neighbor
        # If the neighbor is not visited
        if not visited[nextNode]:
            # Recursive call to explore deeper paths
            if dfs(nextNode, k - weight, graph, visited):
                return True
    # Backtrack: Unmark the current node as visited
    visited[node] = False
    # No valid path found
    return False


def isPathMoreThanK(n, k, src, graph):
    # Initialize visited array
    visited = [False] * n
    # Perform DFS from the source
    return dfs(src, k, graph, visited)


def main():
    n = 9
    k = 58
    graph = [[] for _ in range(n)]
    for u, v, weight in [(0, 7, 20), (7, 1, 10), (1, 2, 10), (2, 3, 10),
                         (3, 4, 10), (4, 5, 10), (5, 6, 10), (6, 8, 10)]:
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    print("True" if isPathMoreThanK(n, k, 0, graph) else "False")


if __name__ == "__main__":
    main()


'''
Let n be vertices and Delta maximum degree.
Time: exponential: this explores simple paths rather than marking a
vertex permanently visited. A conservative bound is O(Delta^n), or
O(n*n!) for a dense simple graph including neighbor scans.
Space: O(n) auxiliary visited and depth, excluding the supplied graph.
As in the source, k<=0 succeeds: it tests path weight AT LEAST k, not
strictly greater than k. Weights should be nonnegative.
'''
