#include <iostream>
#include <unordered_map>
#include <queue>
#include <string>
using namespace std;

int minValue(string s, int k) {
    int ans = 0; // Variable to store the minimized sum of squares
    unordered_map<char, int> freqMap; // Map to store the frequency of each character
    priority_queue<int> maxHeap; // Max-heap to store character frequencies in descending order

    // Step 1: Count the frequency of each character in the string
    for (char c : s) {
        freqMap[c]++;
    }

    // Step 2: Push all frequencies into the max-heap
    for (auto& entry : freqMap) {
        maxHeap.push(entry.second);
    }

    // Step 3: Reduce the highest frequency `k` times
    while (k-- > 0 && !maxHeap.empty()) {
        int topFreq = maxHeap.top(); // Get the highest frequency
        maxHeap.pop(); // Remove it from the heap

        // Reduce the frequency by 1 if it's greater than 1
        if (topFreq > 1) {
            maxHeap.push(topFreq - 1); // Push the updated frequency back to the heap
        }
    }

    // Step 4: Calculate the minimized value as the sum of squares of all remaining frequencies
    while (!maxHeap.empty()) {
        int freq = maxHeap.top();
        ans += freq * freq; // Add the square of each frequency to ans
        maxHeap.pop();
    }

    return ans; // Return the minimized value
}

int main() {
    string str = "abccc";
    int k = 1;
    cout << "Minimized value: " << minValue(str, k) << endl;

    str = "aaab";
    k = 2;
    cout << "Minimized value: " << minValue(str, k) << endl;

    return 0;
}
