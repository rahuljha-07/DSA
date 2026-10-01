#include <vector>
#include <algorithm> // For upper_bound
using namespace std;

int median(vector<vector<int>> &A, int n, int m) {
    // Step 1: Initialize min and max to the first element
    int min = A[0][0], max = A[0][0];
    
    // Step 2: Find the overall minimum and maximum values in the matrix
    for (int i = 0; i < n; i++) {
        // Update min to the smallest element in the first column
        if (A[i][0] < min) min = A[i][0];
        // Update max to the largest element in the last column
        if (A[i][m - 1] > max) max = A[i][m - 1];
    }
    
    // Step 3: Calculate the position of the median element
    int desired_element = (1 + n * m) / 2; // Median position

    // Step 4: Perform binary search for the median
    while (min < max) {
        // Step 4.1: Find the middle value
        int mid = (max + min) / 2;
        int count = 0;

        // Step 4.2: Count elements less than or equal to mid
        for (int i = 0; i < n; i++) {
            // Use upper_bound to count elements <= mid in each row
            count += upper_bound(A[i].begin(), A[i].end(), mid) - A[i].begin();
        }

        // Step 4.3: Adjust min and max based on the count
        if (count < desired_element) {
            // If count is less than desired, increase min
            min = mid + 1;
        } else {
            // If count is greater or equal, decrease max
            max = mid;
        }
    }

    // Step 5: Return the median value, which is now min
    return min;
}
