#include <bits/stdc++.h>
using namespace std;

#define MAX 1000

// Function to calculate the Maximum Area Histogram (MAH) for a given array
int MAH(vector<int>& arr, int n) {
    vector<int> left;  // stores indices of nearest smaller elements to the left
    vector<int> right; // stores indices of nearest smaller elements to the right
    stack<pair<int, int>> s; // stack to help find nearest smaller elements
    int area = INT_MIN;

    // Fill left vector with indices of nearest smaller element to the left
    for (int i = 0; i < n; i++) {
        if (s.empty()) {
            left.push_back(-1);
        } else if (s.size() > 0 && s.top().first < arr[i]) {
            left.push_back(s.top().second);
        } else if (s.size() > 0 && s.top().first >= arr[i]) {
            while (s.size() > 0 && s.top().first >= arr[i]) {
                s.pop();
            }
            if (s.empty()) left.push_back(-1);
            else left.push_back(s.top().second);
        }
        s.push({arr[i], i});
    }

    // Clear stack to reuse it for the right calculation
    while (!s.empty()) s.pop();

    // Fill right vector with indices of nearest smaller element to the right
    for (int i = n - 1; i >= 0; i--) {
        if (s.empty()) {
            right.push_back(n);
        } else if (s.size() > 0 && s.top().first < arr[i]) {
            right.push_back(s.top().second);
        } else if (s.size() > 0 && s.top().first >= arr[i]) {
            while (s.size() > 0 && s.top().first >= arr[i]) {
                s.pop();
            }
            if (s.empty()) right.push_back(n);
            else right.push_back(s.top().second);
        }
        s.push({arr[i], i});
    }
    reverse(right.begin(), right.end());

    // Calculate the maximum area using left and right boundaries for each bar
    for (int i = 0; i < n; i++) {
        area = max(area, (right[i] - left[i] - 1) * arr[i]);
    }

    return area;
}

// Function to find the maximum rectangular area of 1's in a binary matrix
int maxArea(int M[MAX][MAX], int n, int m) {
    vector<int> v(m, 0); // vector to store histogram heights row by row
    int ans = 0;

    // Process the first row as initial histogram heights
    for (int j = 0; j < m; j++) v[j] = M[0][j];
    ans = MAH(v, m);

    // Process subsequent rows
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < m; j++) {
            // Update histogram heights: if cell is 0, reset height to 0; otherwise, add 1
            if (M[i][j] == 0) v[j] = 0;
            else v[j] += M[i][j];
        }
        // Calculate maximum area for the updated histogram
        ans = max(ans, MAH(v, m));
    }

    return ans;
}

// Example usage
int main() {
    int n = 4, m = 4;
    int M[MAX][MAX] = {
        {0, 1, 1, 0},
        {1, 1, 1, 1},
        {1, 1, 1, 0},
        {1, 1, 0, 0}
    };

    cout << "Maximum rectangular area of 1's is: " << maxArea(M, n, m) << endl;
    return 0;
}
