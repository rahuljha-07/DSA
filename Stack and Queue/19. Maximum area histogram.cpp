#include <vector>
#include <stack>
#include <algorithm>
#include <limits.h>

using namespace std;

long long getMaxArea(long long arr[], int n) {
    // Vectors to store the indices of the previous smaller and next smaller elements
    vector<long> left(n);   // For the nearest smaller element on the left
    vector<long> right(n);  // For the nearest smaller element on the right
    
    long long area = INT_MIN; // Initialize the maximum area variable
    stack<pair<long, long>> s; // Stack to keep track of the histogram bars
    
    // Fill the left vector with indices of the nearest smaller elements on the left
    for (long long i = 0; i < n; i++) {
        // If the stack is empty, no smaller element exists on the left
        if (s.empty()) {
            left[i] = -1;
        } else if (s.top().first < arr[i]) {
            // Current bar is taller than the top of the stack
            left[i] = s.top().second;
        } else {
            // Current bar is shorter or equal to the top of the stack
            while (!s.empty() && s.top().first >= arr[i]) {
                s.pop(); // Pop until a smaller element is found
            }
            left[i] = (s.empty()) ? -1 : s.top().second; // -1 if no smaller element found
        }
        s.push({arr[i], i}); // Push current bar height and its index onto the stack
    }
    
    // Clear the stack to reuse it for the right vector
    while (!s.empty()) {
        s.pop();
    }
    
    // Fill the right vector with indices of the nearest smaller elements on the right
    for (long i = n - 1; i >= 0; i--) {
        // If the stack is empty, no smaller element exists on the right
        if (s.empty()) {
            right[i] = n; // n represents the boundary for the right side
        } else if (s.top().first < arr[i]) {
            right[i] = s.top().second;
        } else {
            // Current bar is shorter or equal to the top of the stack
            while (!s.empty() && s.top().first >= arr[i]) {
                s.pop(); // Pop until a smaller element is found
            }
            right[i] = (s.empty()) ? n : s.top().second; // n if no smaller element found
        }
        s.push({arr[i], i}); // Push current bar height and its index onto the stack
    }
    
    // Reverse the right vector to match the order of the histogram bars
    reverse(right.begin(), right.end());
    
    // Calculate the maximum area using the left and right vectors
    for (long long i = 0; i < n; i++) {
        area = max(area, (right[i] - left[i] - 1) * arr[i]); // Area = width * height
    }
    
    return area; // Return the maximum area found
}
