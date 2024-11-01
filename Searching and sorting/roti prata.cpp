// Function to determine if it's possible to make 'par' parathas within 'timeLimit'
int canMakeParathas(const vector<int>& cookingTimes, int par, int timeLimit) {
    int totalParathas = 0; // Count of total parathas made

    // Loop through each cook's speed
    for (size_t i = 0; i < cookingTimes.size(); i++) {
        int time = cookingTimes[i]; // Time taken by the current cook to make the first paratha
        int multiplier = 2; // Multiplier for subsequent parathas

        // While the time required is within the time limit
        while (time <= timeLimit) {
            totalParathas++; // Increment the count of parathas made
            time += (cookingTimes[i] * multiplier); // Calculate the time for the next paratha
            multiplier++; // Increase the multiplier for the next paratha
        }

        // If the total number of parathas made meets or exceeds the required amount
        if (totalParathas >= par) {
            return 1; // Return success
        }
    }

    return 0; // Return failure
}

// Function to find the minimum time required to make 'par' parathas using binary search
int findMinimumTime(const vector<int>& cookingTimes, int par) {
    int lowerBound = 0; // Lower bound for binary search
    int upperBound = 1e8; // Upper bound for binary search (large enough to cover max time)
    int ans = 0; // Variable to store the final answer

    // Perform binary search to find the minimum time required to make 'par' parathas
    while (lowerBound <= upperBound) {
        int mid = (lowerBound + upperBound) / 2; // Calculate the mid point
        
        // Check if it's possible to make 'par' parathas in 'mid' time
        if (canMakeParathas(cookingTimes, par, mid)) {
            ans = mid; // Update the answer to the current mid time
            upperBound = mid - 1; // Try for a smaller time
        } else {
            lowerBound = mid + 1; // Increase time limit to try again
        }
    }

    return ans; // Return the minimum time required
}