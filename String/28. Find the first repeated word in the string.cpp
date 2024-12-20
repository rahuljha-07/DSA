#include <unordered_map>
#include <string>
#include <limits.h> // For INT_MIN

using namespace std;

/*
 * Function to find the second most repeated string in an array of strings.
 * Parameters:
 * - arr: An array of strings.
 * - n: The number of strings in the array.
 *
 * Returns:
 * - The second most repeated string in the array.
 */
string findSecondMostFrequentString(string arr[], int n) {
    // Map to store the frequency of each string
    unordered_map<string, int> frequencyMap;

    // Count the frequency of each string in the array
    for (int i = 0; i < n; i++) {
        frequencyMap[arr[i]]++;
    }

    // Variables to track the first and second maximum frequencies
    int maxFreq1 = INT_MIN; // First maximum frequency
    int maxFreq2 = INT_MIN; // Second maximum frequency

    // Variables to store the corresponding strings
    string resultMax1; // String with the first maximum frequency
    string resultMax2; // String with the second maximum frequency

    // Iterate through the frequency map to find the first and second most frequent strings
    for (const auto& entry : frequencyMap) {
        int currentFreq = entry.second; // Current frequency of the string

        // Check if current frequency is greater than the first maximum
        if (currentFreq > maxFreq1) {
            maxFreq2 = maxFreq1; // Update second maximum to first maximum
            maxFreq1 = currentFreq; // Update first maximum

            resultMax2 = resultMax1; // Update the second result to the first result
            resultMax1 = entry.first; // Update the first result to the current string
        }
        // Check if current frequency is the second maximum and not equal to the first maximum
        else if (currentFreq > maxFreq2 && currentFreq != maxFreq1) {
            maxFreq2 = currentFreq; // Update second maximum frequency
            resultMax2 = entry.first; // Update second result to the current string
        }
    }

    // Return the string with the second maximum frequency
    return resultMax2;
}

// Example usage
int main() {
    string arr[] = {"aaa", "bbb", "ccc", "bbb", "aaa", "aaa"};
    int n = sizeof(arr) / sizeof(arr[0]);
    string secondMostFrequent = findSecondMostFrequentString(arr, n);
    cout << "The second most repeated string is: " << secondMostFrequent << endl; // Output: bbb
    return 0;
}
