def topoSort(node, adj, visited, st):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            topoSort(neighbor, adj, visited, st)
    st.append(node)


def dfs(node, transpose, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in transpose[node]:
        if not visited[neighbor]:
            dfs(neighbor, transpose, visited, component)


def kosaraju(V, adj):
    st = []
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            topoSort(i, adj, visited, st)
    transpose = [[] for _ in range(V)]
    for i in range(V):
        for neighbor in adj[i]:
            transpose[neighbor].append(i)
    visited[:] = [False] * V
    sccCount = 0
    while st:
        node = st.pop()
        if not visited[node]:
            component = []
            dfs(node, transpose, visited, component)
            sccCount += 1
            print(f"Strongly Connected Component {sccCount}:", *component)
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
