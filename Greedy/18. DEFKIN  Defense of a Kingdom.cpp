#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int largestUndefendedRectangle(int w, int h, vector<pair<int, int>>& towers) {
    vector<int> x_coords, y_coords;

    // Add border coordinates (0 and max width/height)
    x_coords.push_back(0);
    y_coords.push_back(0);
    for (auto& tower : towers) {
        x_coords.push_back(tower.first);
        y_coords.push_back(tower.second);
    }
    x_coords.push_back(w + 1);
    y_coords.push_back(h + 1);

    // Sort the coordinates
    sort(x_coords.begin(), x_coords.end());
    sort(y_coords.begin(), y_coords.end());

    // Find the maximum gaps between consecutive x and y coordinates
    int max_x_gap = 0, max_y_gap = 0;
    for (size_t i = 1; i < x_coords.size(); i++) {
        max_x_gap = max(max_x_gap, x_coords[i] - x_coords[i - 1] - 1);
    }
    for (size_t i = 1; i < y_coords.size(); i++) {
        max_y_gap = max(max_y_gap, y_coords[i] - y_coords[i - 1] - 1);
    }

    // The largest undefended rectangle is the product of the largest gaps
    return max_x_gap * max_y_gap;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int w, h, n;
        cin >> w >> h >> n;

        vector<pair<int, int>> towers(n);
        for (int i = 0; i < n; i++) {
            cin >> towers[i].first >> towers[i].second;
        }

        cout << largestUndefendedRectangle(w, h, towers) << endl;
    }

    return 0;
}
