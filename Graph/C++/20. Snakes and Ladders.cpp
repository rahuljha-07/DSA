#include<bits/stdc++.h>
using namespace std;

int snakesAndLadders(vector<vector<int>>& board) {
    int n = board.size();
    map<int, int> lad;  // Ladder map
    map<int, int> sna;  // Snake map
    
    // Create the snake and ladder maps
    int sq = 1;  // Square number
    bool leftToRight = true;
    for (int i = n - 1; i >= 0; i--) {
        if (leftToRight) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] != -1) {
                    if (board[i][j] > sq) lad[sq] = board[i][j];  // Ladder
                    else sna[sq] = board[i][j];                   // Snake
                }
                sq++;
            }
        } else {
            for (int j = n - 1; j >= 0; j--) {
                if (board[i][j] != -1) {
                    if (board[i][j] > sq) lad[sq] = board[i][j];  // Ladder
                    else sna[sq] = board[i][j];                   // Snake
                }
                sq++;
            }
        }
        leftToRight = !leftToRight;
    }

    // BFS to calculate minimum moves
    int moves = 0;
    queue<int> q;
    q.push(1);  // Start from square 1
    bool found = false;
    vector<int> vis(n * n + 1, 0);  // Visited array
    vis[1] = true;

    while (!q.empty() && !found) {
        int sz = q.size();
        while (sz--) {
            int t = q.front();
            q.pop();

            for (int die = 1; die <= 6; die++) {
                int next = t + die;
                if (next == n * n) {
                    found = true;
                }
                if (next <= n * n && lad[next] && !vis[lad[next]]) {
                    vis[lad[next]] = true;
                    if (lad[next] == n * n) {
                        found = true;
                    }
                    q.push(lad[next]);
                } else if (next <= n * n && sna[next] && !vis[sna[next]]) {
                    vis[sna[next]] = true;
                    if (sna[next] == n * n) {
                        found = true;
                    }
                    q.push(sna[next]);
                } else if (next <= n * n && !vis[next] && !sna[next] && !lad[next]) {
                    vis[next] = true;
                    q.push(next);
                }
            }
        }
        moves++;
    }

    if (found) {
        return moves;
    } else {
        return -1;
    }
}

int main() {
    vector<vector<int>> board = {
        {-1, -1, -1, -1, -1, -1},
        {-1, -1, -1, -1, -1, -1},
        {-1, -1, -1, -1, -1, -1},
        {-1, 35, -1, -1, 13, -1},
        {-1, -1, -1, -1, -1, -1},
        {-1, 15, -1, -1, -1, -1}
    };

    cout << snakesAndLadders(board) << endl;
    return 0;
}
