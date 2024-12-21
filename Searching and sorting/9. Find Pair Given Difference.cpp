#include <algorithm> // for std::sort
#include <iostream>  // for std::cout
#include <vector>    // for std::vector

using namespace std;

// Function to find a pair in the vector with a given difference
bool findPair(vector<int>& arr, int targetDiff) {
    // Sort the vector to use the two-pointer technique
    sort(arr.begin(), arr.end());
    
    int leftIndex = 0;    // Left pointer
    int rightIndex = 1;   // Right pointer

    // Iterate until left and right pointers are within bounds
    while (leftIndex < arr.size() && rightIndex < arr.size()) {
        // Calculate the current difference
        int currentDiff = arr[rightIndex] - arr[leftIndex];

        // Check if the current difference matches the target difference
        if (currentDiff == targetDiff) {
            return true; // Found a pair with the specified difference
        }
        // If the current difference is less than the target difference, move the right pointer to the right
        else if (currentDiff < targetDiff) {
            rightIndex++;
        }
        // If the current difference is greater than the target difference, move the left pointer to the right
        else {
            leftIndex++;
        }
    }
    return false; // No pair found with the specified difference
}

// Example usage
int main() {
    vector<int> arr = {1, 5, 3, 4, 2};
    int targetDiff = 3;

    if (findPair(arr, targetDiff)) {
        cout << "Pair found with the given difference." << endl;
    } else {
        cout << "No pair found with the given difference." << endl;
    }

    return 0;
}

1 1 1 2 7 10
