#include <bits/stdc++.h>
using namespace std;

// Helper function to find combinations
void findCombinations(int index, vector<int>& candidates, int target, vector<int>& currentCombination, vector<vector<int>>& result) {
    // If the target becomes zero, we have found a valid combination
    if (target == 0) {
        result.push_back(currentCombination);
        return;
    }

    // Iterate over the candidates array starting from the current index
    for (int i = index; i < candidates.size(); i++) {
        // If the current number exceeds the target, skip further processing
        if (candidates[i] > target) 
            break;

        // Include the current number in the combination
        currentCombination.push_back(candidates[i]);

        // Since the same number can be used multiple times, call the function with the same index
        findCombinations(i, candidates, target - candidates[i], currentCombination, result);

        // Backtrack and remove the last number from the combination
        currentCombination.pop_back();
    }
}

// Main function to find all unique combinations
vector<vector<int>> combinationSum(vector<int>& arr, int target) {
    // Sort the array to ensure combinations are generated in non-descending order
    sort(arr.begin(), arr.end());

    // Remove duplicates from the array
    arr.erase(unique(arr.begin(), arr.end()), arr.end());

    // Result container to store all unique combinations
    vector<vector<int>> result;

    // Temporary container to store a single combination
    vector<int> currentCombination;

    // Start finding combinations from index 0
    findCombinations(0, arr, target, currentCombination, result);

    return result;
}

// Driver code
int main() {
    int N, target;
    cout << "Enter the number of elements in the array: ";
    cin >> N;

    vector<int> arr(N);
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    cout << "Enter the target sum: ";
    cin >> target;

    vector<vector<int>> result = combinationSum(arr, target);

    // If no combinations found, print "Empty"
    if (result.empty()) {
        cout << "Empty" << endl;
    } else {
        // Print all combinations
        for (auto& combination : result) {
            cout << "(";
            for (int i = 0; i < combination.size(); i++) {
                cout << combination[i];
                if (i < combination.size() - 1)
                    cout << " ";
            }
            cout << ")" << endl;
        }
    }

    return 0;
}
