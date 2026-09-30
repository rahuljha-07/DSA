#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    // Function to swap if elements in arr1 and arr2 are out of order
    void swapIfGreater(vector<long long>& arr1, vector<long long>& arr2, int ind1, int ind2) {
        if (arr1[ind1] > arr2[ind2]) {
            swap(arr1[ind1], arr2[ind2]);
        }
    }

    // Function to merge the arrays using the Gap Method
    void merge(vector<long long>& arr1, vector<long long>& arr2, int n, int m) {
        int len = n + m; // Combined length of both arrays
        int gap = (len / 2) + (len % 2); // Initial gap size

        while (gap > 0) {
            int left = 0;
            int right = left + gap;

            while (right < len) {
                // Case 1: Both pointers are in arr1
                if (left < n && right < n) {
                    if (arr1[left] > arr1[right]) {
                        swap(arr1[left], arr1[right]);
                    }
                }
                // Case 2: Pointers are in arr1 and arr2
                else if (left < n && right >= n) {
                    swapIfGreater(arr1, arr2, left, right - n);
                }
                // Case 3: Both pointers are in arr2
                else if (left >= n && right >= n) {
                    if (arr2[left - n] > arr2[right - n]) {
                        swap(arr2[left - n], arr2[right - n]);
                    }
                }

                left++;
                right++;
            }

            // Reduce the gap for the next iteration
            if (gap == 1) break;
            gap = (gap + 1) / 2;
        }
    }
};

int main() {
    vector<long long> arr1 = {1, 4, 7, 8, 10}; // First sorted array
    vector<long long> arr2 = {2, 3, 9};        // Second sorted array

    Solution obj;
    obj.merge(arr1, arr2, arr1.size(), arr2.size());

    cout << "Merged arrays: ";
    for (long long x : arr1) cout << x << " ";
    for (long long x : arr2) cout << x << " ";
    cout << endl;

    return 0;
}
