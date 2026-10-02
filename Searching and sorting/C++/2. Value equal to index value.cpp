#include <vector>
using namespace std;

vector<int> valueEqualToIndex(int arr[], int n) {
    vector<int> ans;  // Initialize an empty vector to store the result

    // Loop through the array to check each element
    for (int i = 0; i < n; i++) {
        // Since it's 1-based indexing, compare arr[i] with i + 1
        if (arr[i] == i + 1) {
            // If element matches its index value, add it to the result
            ans.push_back(arr[i]);
        }
    }

    // Return the vector containing elements that matched their indices
    return ans;
}
