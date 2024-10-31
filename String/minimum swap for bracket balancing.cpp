int minimumNumberOfSwaps(string str) {
     int ans = 0; // Variable to store the number of swaps needed
    int bracketCount = 0; // To count the open brackets

    for (int i = 0; i < str.length(); i++) {
        if (str[i] == '[') {
            bracketCount++; // Increment for an open bracket
        } else {
            bracketCount--; // Decrement for a close bracket
            if (bracketCount < 0) { // If there are more close brackets
                ans = ans - bracketCount;
            }
        }
    }

    return ans; // Return the total number of swaps needed
}