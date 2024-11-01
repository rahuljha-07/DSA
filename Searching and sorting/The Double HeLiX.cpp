#include <vector>
#include <algorithm>

using namespace std;

// Function to find the maximum sum from two increasing integer sequences
int maxSumOfSequences(const vector<int>& first, const vector<int>& second) {
    int sum1 = 0; // Sum of the current path in the first sequence
    int sum2 = 0; // Sum of the current path in the second sequence
    int maxSum = 0; // Maximum sum found

    // Pointers for iterating through both sequences
    size_t i = 0, j = 0;
    while (i < first.size() && j < second.size()) {
        if (first[i] < second[j]) {
            sum1 += first[i]; // Add to sum1 if current element in first is smaller
            i++;
        } else if (first[i] > second[j]) {
            sum2 += second[j]; // Add to sum2 if current element in second is smaller
            j++;
        } else {
            // Found an intersection point
            maxSum += max(sum1, sum2) + first[i]; // Add the maximum of both sums plus the intersection value
            sum1 = 0; // Reset sum1 for the next segment
            sum2 = 0; // Reset sum2 for the next segment
            i++;
            j++;
        }
    }

    // Add remaining elements in first sequence
    while (i < first.size()) {
        sum1 += first[i];
        i++;
    }

    // Add remaining elements in second sequence
    while (j < second.size()) {
        sum2 += second[j];
        j++;
    }

    // Add the maximum of the last sums to the total
    maxSum += max(sum1, sum2);

    return maxSum; // Return the maximum sum
}
