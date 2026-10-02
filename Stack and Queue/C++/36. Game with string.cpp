#include <iostream>
#include <unordered_map>
#include <queue>
#include <string>
using namespace std;

// Function to calculate the minimized value of the string
int minValue(string s, int k) {
    int ans = 0; // Variable to store the final minimized value
    unordered_map<char, int> m; // Map to store the frequency of each character
    priority_queue<int> q; // Max-heap to store character frequencies in descending order

    // Step 1: Count the frequency of each character in the string
    for (int i = 0; i < s.length(); i++) {
        m[s[i]]++;
    }

    // Step 2: Push all frequencies into the max-heap
    for (auto i = m.begin(); i != m.end(); i++) {
        q.push(i->second);
    }

    // Step 3: Reduce the frequency of the most frequent characters k times
    while (k-- && !q.empty()) {
        int temp = q.top(); // Get the highest frequency
        q.pop(); // Remove it from the heap
        if (temp > 1) {
            temp--; // Reduce this frequency by 1
            q.push(temp); // Push the updated frequency back to the heap if > 0
        }
    }

    // Step 4: Calculate the minimized value as the sum of squares of all remaining frequencies
    while (!q.empty()) {
        ans += q.top() * q.top(); // Square the frequency and add to ans
        q.pop(); // Remove frequency from the heap
    }

    return ans; // Return the minimized value
}

int main() {
    string str = "abccc";
    int k = 1;
    cout << "Minimized value: " << minValue(str, k) << endl;
    return 0;
}
