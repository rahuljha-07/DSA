#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int findUnion(vector<int>& a, vector<int>& b) {
    unordered_set<int> set; // To store the unique elements
    int i = 0, j = 0;       // Two pointers to traverse arrays
    
    // Traverse both arrays simultaneously
    while (i < a.size() && j < b.size()) {
        set.insert(a[i]); // Add element from array a
        set.insert(b[j]); // Add element from array b
        i++;              // Move pointer for array a
        j++;              // Move pointer for array b
    }
    
    // Add remaining elements from array a (if any)
    while (i < a.size()) {
        set.insert(a[i]);
        i++;
    }
    
    // Add remaining elements from array b (if any)
    while (j < b.size()) {
        set.insert(b[j]);
        j++;
    }
    
    return set.size(); // Return the size of the union
}

int main() {
    vector<int> a = {1, 2, 3, 4, 5};
    vector<int> b = {3, 4, 5, 6, 7};
    
    cout << "Union size: " << findUnion(a, b) << endl;
    return 0;
}
