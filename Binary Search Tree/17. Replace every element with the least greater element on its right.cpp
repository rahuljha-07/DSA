#include <iostream>
#include <vector>
#include <set>
using namespace std;

vector<int> replaceWithLeastGreater(vector<int>& arr) {
    int n = arr.size();
    vector<int> result(n, -1);  // Initialize the result with -1
    
    set<int> s;  // Sorted set to keep track of elements we've processed
    
    // Traverse the array from right to left
    for (int i = n - 1; i >= 0; --i) {
        auto it = s.upper_bound(arr[i]);  // Find the first element greater than arr[i]
        
        // If a greater element is found, it will be the least greater element
        if (it != s.end()) {
            result[i] = *it;  // Assign the least greater element
        }
        
        // Insert the current element into the set
        s.insert(arr[i]);
    }
    
    return result;
}

int main() {
    vector<int> arr = {8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28};
    vector<int> result = replaceWithLeastGreater(arr);
    
    for (int num : result) {
        cout << num << " ";
    }
    
    return 0;
}
