#include <vector>
using namespace std;

vector<int> spirallyTraverse(vector<vector<int>> matrix, int rows, int cols) {
    vector<int> result;
    int top = 0, bottom = rows - 1;
    int left = 0, right = cols - 1;
    int dir = 0; // 0: left-to-right, 1: top-to-bottom, 2: right-to-left, 3: bottom-to-top

    while (top <= bottom && left <= right) {
        if (dir == 0) { // Traverse left to right
            for (int i = left; i <= right; i++) result.push_back(matrix[top][i]);
            top++;
        } 
        else if (dir == 1) { // Traverse top to bottom
            for (int i = top; i <= bottom; i++) result.push_back(matrix[i][right]);
            right--;
        } 
        else if (dir == 2) { // Traverse right to left
            for (int i = right; i >= left; i--) result.push_back(matrix[bottom][i]);
            bottom--;
        } 
        else if (dir == 3) { // Traverse bottom to top
            for (int i = bottom; i >= top; i--) result.push_back(matrix[i][left]);
            left++;
        }
        dir = (dir + 1) % 4; // Change direction in a cyclic manner
    }

    return result;
}
