typedef pair<int, pair<int, int>> p;  // First: value, second: (array index(row), element index(col))

pair<int, int> findSmallestRange(int arr[][N], int n, int k) {
    priority_queue<p, vector<p>, greater<p>> q;
    pair<int, int> ans;
    int range = INT_MAX;
    int mini = INT_MAX;
    int maxi = INT_MIN;

    // Push the first element of each array into the heap
    for (int i = 0; i < k; i++) {
        q.push({arr[i][0], {i, 0}});
        maxi = max(maxi, arr[i][0]);
    }

    // Process the heap
    while (!q.empty()) {
        p temp = q.top();
        q.pop();
        int start = temp.first;
        int end = maxi;
        int dis = end - start;

        // Update the result if a smaller range is found
        if (range > dis) {
            ans = {start, end};
            range = dis;
        }

        // Get the next element in the same array
        int row = temp.second.first;
        int col = temp.second.second;
        col++;
        if (col < n) {
            q.push({arr[row][col], {row, col}});
            maxi = max(maxi, arr[row][col]);
        } else {
            // If any array runs out of elements, break
            break;
        }
    }

    return ans;  // Return the smallest range found
}
