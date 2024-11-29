#include <iostream>
#include <vector>
using namespace std;

// Adjacency List Representation
/*
Adjacency List:
0 -> 1 4 
1 -> 0 2 3 4 
2 -> 1 3 
3 -> 1 2 4 
4 -> 0 1 3 

*/
class AdjacencyList {
private:
    int vertices; // Number of vertices
    vector<vector<int>> list; // Vector of vectors for adjacency list

public:
    // Constructor to initialize the list
    AdjacencyList(int v) {
        vertices = v;
        list.resize(v);
    }

    // Add an edge between two vertices
    void addEdge(int u, int v) {
        list[u].push_back(v);
        list[v].push_back(u); // Assuming an undirected graph
    }

    // Print the adjacency list
    void printList() {
        cout << "Adjacency List:" << endl;
        for (int i = 0; i < vertices; i++) {
            cout << i << " -> ";
            for (int neighbor : list[i]) {
                cout << neighbor << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    int vertices = 5; // Number of vertices
    AdjacencyList graph(vertices);

    // Adding edges
    graph.addEdge(0, 1);
    graph.addEdge(0, 4);
    graph.addEdge(1, 2);
    graph.addEdge(1, 3);
    graph.addEdge(1, 4);
    graph.addEdge(2, 3);
    graph.addEdge(3, 4);

    // Print the adjacency list
    graph.printList();

    return 0;
}



// Adjacency Matrix Representation:
/*
    Adjacency Matrix:
    0 1 0 0 1 
    1 0 1 1 1 
    0 1 0 1 0 
    0 1 1 0 1 
    1 1 0 1 0 
*/
class AdjacencyMatrix {
private:
    int vertices; // Number of vertices
    vector<vector<int>> matrix; // 2D vector for adjacency matrix

public:
    // Constructor to initialize the matrix
    AdjacencyMatrix(int v) {
        vertices = v;
        matrix = vector<vector<int>>(v, vector<int>(v, 0));
    }

    // Add an edge between two vertices
    void addEdge(int u, int v) {
        matrix[u][v] = 1;
        matrix[v][u] = 1; // Assuming an undirected graph
    }

    // Print the adjacency matrix
    void printMatrix() {
        cout << "Adjacency Matrix:" << endl;
        for (int i = 0; i < vertices; i++) {
            for (int j = 0; j < vertices; j++) {
                cout << matrix[i][j] << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    int vertices = 5; // Number of vertices
    AdjacencyMatrix graph(vertices);

    // Adding edges
    graph.addEdge(0, 1);
    graph.addEdge(0, 4);
    graph.addEdge(1, 2);
    graph.addEdge(1, 3);
    graph.addEdge(1, 4);
    graph.addEdge(2, 3);
    graph.addEdge(3, 4);

    // Print the adjacency matrix
    graph.printMatrix();

    return 0;
}
