// Function to check if it's possible to cut wood to achieve at least 'm' amount of wood
bool canAchieveWoodAmount(const vector<int>& lengths, int requiredAmount, int cutHeight) {
    int totalWood = 0; // Initialize the total wood collected

    // Loop through each tree length in the array
    for (int length : lengths) {
        // If the tree is taller than the cut height, we can collect some wood
        if (length > cutHeight) {
            totalWood += (length - cutHeight); // Add the collected wood
        }
    }

    // Check if the total collected wood is at least the required amount
    return totalWood >= requiredAmount;
}

// Function to find the maximum height at which to cut wood to achieve the required amount
int findMaxCutHeight(const vector<int>& lengths, int requiredAmount) {
    int low = 0; // Minimum possible cut height
    int high = *max_element(lengths.begin(), lengths.end()); // Maximum possible cut height
    int optimalHeight = -1; // Variable to store the optimal cut height

    // Perform binary search to find the optimal cut height
    while (low <= high) {
        int mid = low + (high - low) / 2; // Calculate the mid cut height

        // Check if we can achieve the required amount of wood with the current cut height
        if (canAchieveWoodAmount(lengths, requiredAmount, mid)) {
            optimalHeight = mid; // Update the optimal height
            low = mid + 1; // Try to find a higher cut height
        } else {
            high = mid - 1; // Reduce the cut height
        }
    }

    return optimalHeight; // Return the optimal cut height found
}