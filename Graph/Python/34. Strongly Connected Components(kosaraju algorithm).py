# Function to perform DFS and fill the stack for topo sort
def topoSort(node, adj, visited, st):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            topoSort(neighbor, adj, visited, st)
    st.append(node)


# Function to perform DFS and collect nodes of a strongly connected component
def dfs(node, transpose, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in transpose[node]:
        if not visited[neighbor]:
            dfs(neighbor, transpose, visited, component)


def kosaraju(V, adj):
    # Step 1: Toposort
    st = []
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            topoSort(i, adj, visited, st)
    # Step 2: Reverse the graph
    transpose = [[] for _ in range(V)]
    for i in range(V):
        for neighbor in adj[i]:
            transpose[neighbor].append(i)
    visited[:] = [False] * V
    # Count of strongly connected components
    sccCount = 0
    while st:
        node = st.pop()
        if not visited[node]:
            # To store the current SCC
            component = []
            dfs(node, transpose, visited, component)
            sccCount += 1
            # Print the current SCC
            print(f"Strongly Connected Component {sccCount}:", *component)
    # Return the number of SCCs
    return sccCount


def main():
    V = 5
    adj = [[1], [2, 3], [0], [4], []]
    count = kosaraju(V, adj)
    print("Number of Strongly Connected Components:", count)


if __name__ == "__main__":
    main()


'''
Let V/E be directed vertex/edge counts.
Time: O(V + E): finishing-order DFS, transpose construction, and reversed-
graph DFS each visit all vertices/edges at most once.
Space: O(V + E) auxiliary transpose plus O(V) visited/stacks/component.
Components are printed rather than accumulated as a separate result graph.
'''
