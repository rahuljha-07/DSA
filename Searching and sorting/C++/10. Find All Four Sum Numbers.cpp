#include <algorithm> // for std::sort
#include <vector>    // for std::vector
#include <set>       // for std::set

using namespace std;

// Function to find all unique quadruplets in the array that sum up to a given target value
vector<vector<int>> fourSum(vector<int> &arr, int targetSum) {
    // Sort the input array to facilitate the two-pointer technique
    sort(arr.begin(), arr.end());
    
    vector<vector<int>> result; // To store the unique quadruplets
    set<vector<int>> uniqueQuadruplets; // To avoid duplicates
    int n = arr.size(); // Get the size of the array
    
    // Iterate through the array to find quadruplets
    for (int i = 0; i < n - 3; i++) { // First element
        for (int j = i + 1; j < n - 2; j++) { // Second element
            int left = j + 1; // Left pointer
            int right = n - 1; // Right pointer
            
            // Use two pointers to find the remaining two elements
            while (left < right) {
                int currentSum = arr[i] + arr[j] + arr[left] + arr[right]; // Calculate current sum
                
                // Check if the current sum matches the target
                if (currentSum == targetSum) {
                    // Insert the quadruplet into the set to ensure uniqueness
                    uniqueQuadruplets.insert({arr[i], arr[j], arr[left], arr[right]});
                    left++; // Move the left pointer to the right
                    right--; // Move the right pointer to the left
                } 
                // If the current sum is less than the target, move the left pointer to the right
                else if (currentSum < targetSum) {
                    left++;
                } 
                // If the current sum is greater than the target, move the right pointer to the left
                else {
                    right--;
                }
            }
        }
    }
    
    // Convert the set of unique quadruplets to a vector
    for (const auto &quad : uniqueQuadruplets) {
        result.push_back(quad); // Add each quadruplet to the result vector
    }
    
    return result; // Return the result containing all unique quadruplets
}

// Example usage
int main() {
    vector<int> arr = {1, 0, -1, 0, -2, 2};
    int target = 0;
    
    vector<vector<int>> quadruplets = fourSum(arr, target);
    
    // Print the result
    for (const auto &quad : quadruplets) {
        cout << "{ ";
        for (int num : quad) {
            cout << num << " ";
        }
        cout << "} ";
    }
    
    return 0;
}
