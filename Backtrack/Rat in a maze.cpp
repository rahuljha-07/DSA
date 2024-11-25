// Global vector to store all paths from start to end
vector<string> v;

// Recursive DFS function to explore all possible paths
void dfs(int i, int j, string s, vector<vector<int>> &m, int n) {
    // Boundary and obstacle checks
    if (i < 0 || j < 0 || i >= n || j >= n || m[i][j] == 0) return;
    
    // If the destination (bottom-right corner) is reached
    if (i == n - 1 && j == n - 1) {
        v.push_back(s); // Add the current path to the list of paths
        return;
    }

    // Mark the current cell as visited
    m[i][j] = 0;

    // Recursive calls for all four possible directions
    dfs(i - 1, j, s + 'U', m, n); // Move Up
    dfs(i + 1, j, s + 'D', m, n); // Move Down
    dfs(i, j - 1, s + 'L', m, n); // Move Left
    dfs(i, j + 1, s + 'R', m, n); // Move Right

    // Backtrack by marking the cell as unvisited
    m[i][j] = 1;
}

// Main function to find all possible paths
vector<string> findPath(vector<vector<int>> &m, int n) {
    v.clear(); // Clear previous results
    // Check if start or end cells are blocked
    if (m[0][0] == 0 || m[n - 1][n - 1] == 0) return v;

    string s = ""; // Initial empty path
    dfs(0, 0, s, m, n); // Start DFS from the top-left corner

    sort(v.begin(), v.end()); // Sort paths lexicographically
    return v;
}

//bfs
// Main function to find all possible paths using BFS
vector<string> findPathBFS(vector<vector<int>> &m, int n) {
    vector<string> paths; // Store all paths from start to end
    if (m[0][0] == 0 || m[n - 1][n - 1] == 0) return paths;

    // Directions as tuples of (row_offset, col_offset, direction_character)
    vector<tuple<int, int, char>> directions = {
        {-1, 0, 'U'},  // Up
        {1, 0, 'D'},   // Down
        {0, -1, 'L'},  // Left
        {0, 1, 'R'}    // Right
    };

    // Queue stores tuples: (current_row, current_col, current_path)
    queue<pair<pair<int, int>, string>> q;
    q.push({{0, 0}, ""});
    m[0][0] = 0; // Mark the starting cell as visited

    // BFS loop
    while (!q.empty()) {
        int i = q.front().first.first;
        int j = q.front().first.second;
        string path = q.front().second;
        q.pop();

        // If the destination is reached, save the path
        if (i == n - 1 && j == n - 1) {
            paths.push_back(path);
            continue;
        }

        // Explore each direction
        for (const auto& [di, dj, dir] : directions) {
            int ni = i + di;
            int nj = j + dj;

            // Check boundaries and if the cell is unvisited
            if (ni >= 0 && nj >= 0 && ni < n && nj < n && m[ni][nj] == 1) {
                q.push({{ni, nj}, path + dir});
                m[ni][nj] = 0; // Mark as visited
            }
        }
    }

    sort(paths.begin(), paths.end()); // Sort paths lexicographically
    return paths;
}
