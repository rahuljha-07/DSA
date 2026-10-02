// DFS

#include <vector>
using namespace std;

void dfs(vector<vector<int>>& image, int x, int y, int newColor, int originalColor) {
    // Boundary and color check
    if (x < 0 || x >= image.size() || y < 0 || y >= image[0].size() || image[x][y] != originalColor || image[x][y] == newColor) {
        return;
    }

    // Change the color
    image[x][y] = newColor;

    // Perform DFS in all 4 directions
    dfs(image, x + 1, y, newColor, originalColor); // Down
    dfs(image, x - 1, y, newColor, originalColor); // Up
    dfs(image, x, y + 1, newColor, originalColor); // Right
    dfs(image, x, y - 1, newColor, originalColor); // Left
}

vector<vector<int>> floodFillDFS(vector<vector<int>>& image, int sr, int sc, int color) {
    int originalColor = image[sr][sc];
    if (originalColor != color) {
        dfs(image, sr, sc, color, originalColor);
    }
    return image;
}

// BFS
#include <vector>
#include <queue>
using namespace std;

vector<vector<int>> floodFillBFS(vector<vector<int>>& image, int sr, int sc, int color) {
    int originalColor = image[sr][sc];
    if (originalColor == color) {
        return image;
    }

    int rows = image.size();
    int cols = image[0].size();
    queue<pair<int, int>> q;

    // Start BFS from the given pixel
    q.push({sr, sc});
    image[sr][sc] = color;

    // Directions for 4-connected neighbors
    vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        // Process all 4 neighbors
        for (auto dir : directions) {
            int nx = x + dir.first;
            int ny = y + dir.second;

            // Boundary and color check
            if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && image[nx][ny] == originalColor) {
                image[nx][ny] = color; // Change the color
                q.push({nx, ny});     // Add the neighbor to the queue
            }
        }
    }

    return image;
}
