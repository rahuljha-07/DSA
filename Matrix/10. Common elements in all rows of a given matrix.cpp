#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> commonElements(vector<vector<int>>& matrix) {
    vector<int> result;
    if (matrix.empty()) return result; // Return if the matrix is empty

    unordered_map<int, int> elementCount; // Map to store the count of each element
    int n = matrix.size(); // Number of rows

    // Initialize the map with elements from the first row
    for (int num : matrix[0]) {
        elementCount[num] = 1; // Set count to 1 for elements in the first row
    }

    // Iterate through the remaining rows
    for (int i = 1; i < n; i++) {
        for (int num : matrix[i]) {
            // Check if the element exists in the map and its count matches the current row index
            if (elementCount[num] == i) {
                elementCount[num]++; // Increment count for this row
            }
        }
    }

    // Collect elements that appear in all rows
    for (const auto& entry : elementCount) {
        if (entry.second == n) { // If the count equals the number of rows
            result.push_back(entry.first); // Add to the result
        }
    }

    return result; // Return the list of common elements
}



vector<int> commonElements(vector<vector<int>>& matrix) { // using map
    vector<int> result;
    if (matrix.empty()) return result; // Return if the matrix is empty

    unordered_map<int, int> elementCount; // Map to store the count of each element
    int n = matrix.size(); // Number of rows

    // Iterate over the first row to initialize the map
    for (int num : matrix[0]) {
        elementCount[num] = 1; // Initialize count for elements in the first row
    }

    // Iterate through the remaining rows
    for (int i = 1; i < n; i++) {
        unordered_map<int, bool> seenInCurrentRow; // Map to track seen elements in the current row

        for (int j = 0; j < matrix[i].size(); j++) {
            int num = matrix[i][j]; // Get the current element

            // Check if the element is in the count map and not seen before in the current row
            if (elementCount.find(num) != elementCount.end() && !seenInCurrentRow[num]) {
                elementCount[num]++; // Increment count in the map
                seenInCurrentRow[num] = true; // Mark this element as seen in the current row
            }
        }
    }

    // Check which elements appear in all rows (count equals number of rows)
    for (const auto& entry : elementCount) {
        if (entry.second == n) { // If count equals number of rows
            result.push_back(entry.first); // Add to result
        }
    }

    return result; // Return the list of common elements
}

vector<int> commonElements(vector<vector<int>>& matrix) { //using set
    vector<int> result;
    if (matrix.empty()) return result; // Return empty if the matrix is empty

    // Step 1: Store elements of the first row in a set
    set<int> commonElementsSet(matrix[0].begin(), matrix[0].end());

    // Step 2: Iterate over the rest of the rows
    for (int i = 1; i < matrix.size(); i++) {
        set<int> currentRowElements(matrix[i].begin(), matrix[i].end());
        set<int> intersection;

        // Step 3: Find common elements between the current row and the common set
        for (int num : commonElementsSet) {
            if (currentRowElements.find(num) != currentRowElements.end()) {
                intersection.insert(num); // Insert common elements
            }
        }

        // Update the common elements set
        commonElementsSet = intersection;
    }

    // Step 4: Convert the set to a vector for the result
    for (int num : commonElementsSet) {
        result.push_back(num);
    }

    return result;
}


int main() {
    // Example usage
    vector<vector<int>> matrix = {
        {1, 2, 3, 4},
        {2, 3, 5, 6},
        {2, 3, 7, 8}
    };

    vector<int> common = commonElements(matrix);
    
    cout << "Common elements in all rows: ";
    for (int num : common) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}

