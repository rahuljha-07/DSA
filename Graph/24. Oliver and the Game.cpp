#include <bits/stdc++.h>
using namespace std;

vector<int> inTime, outTime; // Vectors to store entry and exit times
int timer; // Global timer variable

void resize(int n) {
    inTime.resize(n + 1);
    outTime.resize(n + 1);
}

void dfs(int src, int par, vector<int> g[]) {
    inTime[src] = timer++; // Record entry time
    for (auto x : g[src]) {
        if (x != par) { // Avoid going back to the parent
            dfs(x, src, g);
        }
    }
    outTime[src] = timer++; // Record exit time
}

bool check(int x, int y) {
    // Check if x is an ancestor of y
    if (inTime[x] <= inTime[y] && outTime[x] >= outTime[y]) {
        return true;
    }
    return false;
}

int main() {

    int n;
    cin >> n;

    timer = 1;
    resize(n);

    vector<int> g[n + 1]; // Adjacency list for the tree

    // Reading the edges
    for (int i = 0; i < n - 1; i++) {
        int x, y;
        cin >> x >> y;
        g[x].push_back(y);
        g[y].push_back(x);
    }

    // Preprocessing with DFS
    dfs(1, 0, g);

    int q;
    cin >> q;

    // Answering queries
    for (int i = 0; i < q; i++) {
        int type, x, y;
        cin >> type >> x >> y;

        // If neither x is an ancestor of y nor y is an ancestor of x, answer "NO"
        if (!check(x, y) && !check(y, x)) {
            cout << "NO\n";
            continue;
        }

        if (type == 0) {
            // Bob moves toward the King's Mansion
            if (check(y, x)) {
                cout << "YES\n";
            } else {
                cout << "NO\n";
            }
        } else {
            // Bob moves away from the King's Mansion
            if (check(x, y)) {
                cout << "YES\n";
            } else {
                cout << "NO\n";
            }
        }
    }

    return 0;
}
