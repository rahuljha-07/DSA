#include <bits/stdc++.h>
using namespace std;

void findKthPermutation(vector<int>& nums, vector<bool>& visited, string& current, int& count, int K, string& result) {
    // Base case: If the current permutation is of length N
    if (current.length() == nums.size()) {
        count++; // Increment the count of generated permutations
        if (count == K) { // If this is the K-th permutation
            result = current; // Store the result
        }
        return;
    }

    // Explore all unused numbers for the current position
    for (int i = 0; i < nums.size(); i++) {
        if (!visited[i]) {
            visited[i] = true; // Mark the number as used
            current += to_string(nums[i]); // Add the number to the current permutation

            findKthPermutation(nums, visited, current, count, K, result);

            if (!result.empty()) return; // Stop recursion once we find the K-th permutation

            current.pop_back(); // Backtrack
            visited[i] = false; // Mark the number as unused
        }
    }
}

string getKthPermutation(int N, int K) {
    vector<int> nums;
    for (int i = 1; i <= N; i++) {
        nums.push_back(i); // Generate numbers from 1 to N
    }

    vector<bool> visited(N, false); // To track used numbers
    string current = ""; // Current permutation being built
    string result = ""; // K-th permutation result
    int count = 0; // To track how many permutations have been generated

    findKthPermutation(nums, visited, current, count, K, result);

    return result;
}

int main() {
    int N, K;
    cout << "Enter N (number of elements): ";
    cin >> N;
    cout << "Enter K (desired permutation): ";
    cin >> K;

    string result = getKthPermutation(N, K);
    cout << "The " << K << "-th permutation is: " << result << endl;

    return 0;
}
/*
Recursive Backtracking:

The function findKthPermutation generates all permutations recursively by trying every unused number at each position.
If a number has already been used in the current permutation, it is skipped.
Base Case:

When the current permutation's length equals 
𝑁
N, it is a valid permutation.
Increment the count of generated permutations.
If this is the 
𝐾
K-th permutation, store it in result.
Stopping Early:

Once the 
𝐾
K-th permutation is found, the recursion stops to save unnecessary computations.
Backtracking:

After adding a number to the current permutation, the function backtracks by removing the number and marking it as unused for the next iterations.

*/