# Function to perform DFS and check if there's a path with length >= k
def dfs(adj, visited, src, k):
    # If the current distance becomes more than or equal to k, return true
    if k <= 0:
        return True
    # Mark the current node as visited
    visited[src] = True
    # Explore all neighbors of the current node
    for neighbor in adj[src]:
        v, weight = neighbor
        # If the neighbor is not visited, recurse
        if not visited[v]:
            # Check if there's a path with length >= k from this neighbor
            if dfs(adj, visited, v, k - weight):
                return True
    # Backtrack: Unmark the current node
    visited[src] = False
    return False


# Function to check if there is a simple path with length >= k
def pathMoreThanK(V, adj, src, k):
    # Create a visited array to keep track of visited nodes
    visited = [False] * V
    # Call the helper function to start the DFS
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
