#include <bits/stdc++.h>
using namespace std;

void printSortedMatrix(vector<vector<int>>& matrix) { // using tuple
    int n = matrix.size();
    if (n == 0) return; // Handle empty matrix case
    int m = matrix[0].size();

    // Create a priority queue (min-heap)
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> minHeap;

    // Push the first element of each row into the min-heap
    for (int i = 0; i < n; i++) {
         minHeap.push(make_tuple(matrix[i][0], i, 0)); // Push value, row index, column index

    }

    // Process the min-heap
    while (!minHeap.empty()) {
        // Get the smallest element
        auto current = minHeap.top();
        minHeap.pop();

        // Print the smallest element
        cout << get<0>(current) << " "; // Access the value using get<0>

        // If there is a next element in the same row, push it into the heap
        if (get<2>(current) + 1 < m) {
            minHeap.push(make_tuple(matrix[get<1>(current)][get<2>(current) + 1], get<1>(current), get<2>(current) + 1));
        }
    }
}


void printSortedMatrix(vector<vector<int>>& matrix) { // using pair
    int n = matrix.size();
    if (n == 0) return; // Handle empty matrix case
    int m = matrix[0].size();

    // Create a priority queue (min-heap)
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> minHeap;

    // Push the first element of each row into the min-heap
    for (int i = 0; i < n; i++) {
        if (m > 0) { // Check if the row is not empty
            minHeap.push({matrix[i][0], {i, 0}}); // Push value, row index, column index
        }
    }

    // Process the min-heap
    while (!minHeap.empty()) {
        // Get the smallest element
        auto current = minHeap.top();
        minHeap.pop();

        // Print the smallest element
        cout << current.first << " ";

        // If there is a next element in the same row, push it into the heap
        if (current.second.second + 1 < m) {
            minHeap.push({matrix[current.second.first][current.second.second + 1], {current.second.first, current.second.second + 1}});
        }
    }
}

//using your own strucutre

// Structure to hold the value and its position (row and column)
struct Element {
    int value; // The value of the element
    int row;   // The row index of the element
    int col;   // The column index of the element

    // Custom comparison operator for the priority queue
    bool operator>(const Element &other) const {
        return value > other.value; // Min-heap based on the value
    }
};

void printSortedMatrix(vector<vector<int>>& matrix) {
    // Get the number of rows and columns
    int n = matrix.size();
    if (n == 0) return; // Handle empty matrix case
    int m = matrix[0].size();

    // Create a priority queue (min-heap)
    priority_queue<Element, vector<Element>, greater<Element>> minHeap;

    // Push the first element of each row into the min-heap
    for (int i = 0; i < n; i++) {
        if (m > 0) { // Check if the row is not empty
            minHeap.push({matrix[i][0], i, 0}); // Push value, row index, column index
        }
    }

    // Process the min-heap
    while (!minHeap.empty()) {
        // Get the smallest element
        Element current = minHeap.top();
        minHeap.pop();

        // Print the smallest element
        cout << current.value << " ";

        // If there is a next element in the same row, push it into the heap
        if (current.col + 1 < m) {
            minHeap.push({matrix[current.row][current.col + 1], current.row, current.col + 1});
        }
    }
}

int main() {
    // Example matrix input
    vector<vector<int>> matrix = {
        {10, 20, 30},
        {5, 15, 25},
        {1, 2, 3}
    };

    // Function call to print elements in sorted order
    cout << "Sorted elements in row-column wise: ";
    printSortedMatrix(matrix);

    return 0;
}
