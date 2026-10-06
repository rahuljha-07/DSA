class AdjacencyList:
    # Constructor to initialize the list
    def __init__(self, v):
        self.vertices = v
        self.list = [[] for _ in range(v)]

    # Add an edge between two vertices
    def addEdge(self, u, v):
        # Assuming an undirected graph
        self.list[u].append(v)
        self.list[v].append(u)

    # Print the adjacency list
    def printList(self):
        print("Adjacency List:")
        for i in range(self.vertices):
            print(f"{i} -> ", end="")
            for neighbor in self.list[i]:
                print(neighbor, end=" ")
            print()


class AdjacencyMatrix:
    # Constructor to initialize the matrix
    def __init__(self, v):
        self.vertices = v
        self.matrix = [[0] * v for _ in range(v)]

    def addEdge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    # Print the adjacency matrix
    def printMatrix(self):
        print("Adjacency Matrix:")
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(self.matrix[i][j], end=" ")
            print()


def mainMatrix():
    vertices = 5
    graph = AdjacencyMatrix(vertices)
    graph.addEdge(0, 1)
    graph.addEdge(0, 4)
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.printMatrix()


def main():
    vertices = 5
    graph = AdjacencyList(vertices)
    graph.addEdge(0, 1)
    graph.addEdge(0, 4)
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.printList()


if __name__ == "__main__":
    main()


'''
Let V/E be vertex/edge counts.
List time: O(V) construction, O(1) amortized per addEdge, O(V + E) printing.
Matrix time: O(V^2) construction/printing, O(1) per addEdge.
Space: O(V + E) list storage versus O(V^2) matrix storage.
Both representations retain undirected edges; list permits duplicates,
whereas matrix stores only whether an edge exists.
'''
