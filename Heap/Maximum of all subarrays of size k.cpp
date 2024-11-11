#include <iostream>
#include <vector>
#include <list>
using namespace std;

vector<int> maximumOfAllSubarrays(const vector<int>& arr, int k) {
    vector<int> ans;  // To store the results (maximum of each window)
    list<int> window; // List to store values in the current sliding window

    int i = 0, j = 0, size = arr.size();

    while (j < size) {
        // If the size of the window is less than k
        if (j - i + 1 < k) {
            // Maintain elements in the list in decreasing order
            while (!window.empty() && window.back() <= arr[j]) {
                window.pop_back();
            }
            window.push_back(arr[j]);

            // Expand the window by moving 'j' forward
            j++;
        }
        // When the window size reaches k
        else if (j - i + 1 == k) {
            // The element at the front of the list is the maximum for this window
            ans.push_back(window.front());

            // If the element at the front of the list is out of the window, pop it
            if (arr[i] == window.front()) {
                window.pop_front();
            }

            // Slide the window by incrementing 'i' and 'j'
            i++;
            j++;  // This should be outside the `else if` block to ensure it's executed in every loop
        }
    }

    return ans;
}

int main() {
    vector<int> arr = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    vector<int> result = maximumOfAllSubarrays(arr, k);

    cout << "Maximums of all subarrays of size " << k << ": ";
    for (int max : result) {
        cout << max << " ";
    }
    cout << endl;

    return 0;
}
