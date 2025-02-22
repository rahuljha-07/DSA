#include <iostream>
#include <queue>
#include <set>
#include <stack>
#include <utility>
using namespace std;

// BFS approach
int waterJugBFS(int m, int n, int d) {
    if (d > max(m, n) || d % __gcd(m, n) != 0) return -1;

    set<pair<int, int>> visited;
    queue<pair<pair<int, int>, int>> q; // ((jug1, jug2), steps)
    q.push({{0, 0}, 0}); // Initially both jugs are empty

    while (!q.empty()) {
        auto current = q.front();
        q.pop();
        int jug1 = current.first.first;
        int jug2 = current.first.second;
        int steps = current.second;

        if (jug1 == d || jug2 == d) {
            return steps;
        }

        if (visited.find({jug1, jug2}) != visited.end()) {
            continue;
        }
        visited.insert({jug1, jug2});

        // Possible operations
        q.push({{m, jug2}, steps + 1}); // Fill jug1
        q.push({{jug1, n}, steps + 1}); // Fill jug2
        q.push({{0, jug2}, steps + 1}); // Empty jug1
        q.push({{jug1, 0}, steps + 1}); // Empty jug2
        q.push({{min(jug1 + jug2, m), jug1 + jug2 > m ? jug1 + jug2 - m : 0}, steps + 1}); // Pour jug2 -> jug1
        q.push({{jug1 + jug2 > n ? jug1 + jug2 - n : 0, min(jug1 + jug2, n)}, steps + 1}); // Pour jug1 -> jug2
    }
    return -1;
}

// DFS approach
bool dfsHelper(int jug1, int jug2, int m, int n, int d, set<pair<int, int>> &visited, int &steps) {
    if (jug1 == d || jug2 == d) {
        return true;
    }
    if (visited.find({jug1, jug2}) != visited.end()) {
        return false;
    }
    visited.insert({jug1, jug2});
    steps++;

    // Perform all operations and recurse
    if (dfsHelper(m, jug2, m, n, d, visited, steps)) return true; // Fill jug1
    if (dfsHelper(jug1, n, m, n, d, visited, steps)) return true; // Fill jug2
    if (dfsHelper(0, jug2, m, n, d, visited, steps)) return true; // Empty jug1
    if (dfsHelper(jug1, 0, m, n, d, visited, steps)) return true; // Empty jug2
    if (dfsHelper(min(jug1 + jug2, m), jug1 + jug2 > m ? jug1 + jug2 - m : 0, m, n, d, visited, steps)) return true; // Pour jug2 -> jug1
    if (dfsHelper(jug1 + jug2 > n ? jug1 + jug2 - n : 0, min(jug1 + jug2, n), m, n, d, visited, steps)) return true; // Pour jug1 -> jug2

    steps--;
    return false;
}

int waterJugDFS(int m, int n, int d) {
    if (d > max(m, n) || d % __gcd(m, n) != 0) return -1;

    set<pair<int, int>> visited;
    int steps = 0;
    if (dfsHelper(0, 0, m, n, d, visited, steps)) {
        return steps;
    }
    return -1;
}

// Main function
int main() {
    int m = 3, n = 5, d = 4;

    cout << "Using BFS: " << waterJugBFS(m, n, d) << " steps" << endl;
    cout << "Using DFS: " << waterJugDFS(m, n, d) << " steps" << endl;

    return 0;
}
