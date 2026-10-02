def hasEulerianPath(graph, startNode):
    oddDegreeCount = 0
    n = len(graph)
    active = []
    for i in range(n):
        degree = 0
        for j in range(n):
            degree += graph[i][j]
        if degree:
            active.append(i)
        if degree % 2 != 0:
            oddDegreeCount += 1
            startNode[0] = i
    if oddDegreeCount not in (0, 2):
        return False
    if not active:
        return True
    if oddDegreeCount == 0:
        startNode[0] = active[0]
    # Parity alone is insufficient: all non-isolated vertices must connect.
    visited = {startNode[0]}
    st = [startNode[0]]
    while st:
        node = st.pop()
        for neighbor in range(n):
            if graph[node][neighbor] and neighbor not in visited:
                visited.add(neighbor)
                st.append(neighbor)
    return all(node in visited for node in active)


def findEulerianPath(graph, startNode):
    currentPath = [startNode] if graph else []
    eulerPath = []
    while currentPath:
        currentNode = currentPath[-1]
        edgeFound = False
        for nextNode in range(len(graph)):
            if graph[currentNode][nextNode] > 0:
                graph[currentNode][nextNode] -= 1
                graph[nextNode][currentNode] -= 1
                currentPath.append(nextNode)
                edgeFound = True
                break
        if not edgeFound:
            eulerPath.append(currentNode)
            currentPath.pop()
    for i in range(len(eulerPath) - 1, -1, -1):
        print(eulerPath[i] + 1, end="")
        if i != 0:
            print(" -> ", end="")
    print()


def main():
    graph = [[0, 1, 0, 0, 1], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0],
             [0, 1, 1, 0, 0], [1, 0, 0, 0, 0]]
    startNode = [0]
    if hasEulerianPath(graph, startNode):
        print("Eulerian Path: ", end="")
        findEulerianPath(graph, startNode[0])
    else:
        print("No Solution")


if __name__ == "__main__":
    main()


'''
Let V/E be vertex/undirected edge counts, including parallel edges.
Time: O(V^2) parity/connectivity checking; Hierholzer traversal uses
O(V*(E+1)) because each edge advance/stack pop rescans a matrix row.
Space: O(V) auxiliary checking state and O(E+1) traversal stack/path.
Graph is consumed in place. Assumes a symmetric nonnegative matrix
without self-loops. startNode is a one-item C++ reference holder; connectivity
and choosing a non-isolated start fix false/partial Eulerian paths.
'''
