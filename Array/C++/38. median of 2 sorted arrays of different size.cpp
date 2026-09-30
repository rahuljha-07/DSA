#include <iostream>
#include <vector>
#include <climits>
using namespace std;

double findMedian(vector<int>& a, vector<int>& b) {
    int n1 = a.size();
    int n2 = b.size();

    // Ensure `a` is the smaller array to minimize binary search range
    if (n1 > n2) return findMedian(b, a); 

    int low = 0, high = n1; // Binary search range in `a`
    int total = (n1 + n2 + 1) / 2; // Total elements in the left partition

    while (low <= high) {
        int mid1 = (low + high) / 2; // Partition index for `a`
        int mid2 = total - mid1;     // Partition index for `b` (remaining elements)

        // Edge cases: Handle when the partition is at the start or end of an array
        int leftA = (mid1 == 0) ? INT_MIN : a[mid1 - 1]; // Last element in left half of `a`
        int leftB = (mid2 == 0) ? INT_MIN : b[mid2 - 1]; // Last element in left half of `b`
        int rightA = (mid1 == n1) ? INT_MAX : a[mid1];   // First element in right half of `a`
        int rightB = (mid2 == n2) ? INT_MAX : b[mid2];   // First element in right half of `b`

        // Check if partitioning is correct
        if (leftA <= rightB && leftB <= rightA) {
            // If total size is odd, median is the max of the left partition
            if ((n1 + n2) % 2 == 1) return max(leftA, leftB);
            // If total size is even, median is the average of max left and min right
            return (max(leftA, leftB) + min(rightA, rightB)) / 2.0;
        }
        // If leftA is greater, move left in `a`
        else if (leftA > rightB) {
            high = mid1 - 1;
        }
        // If leftB is greater, move right in `a`
        else {
            low = mid1 + 1;
        }
    }
    return 0.0; // Should never reach here
}

int main() {
    vector<int> a = {1, 3, 8}; 
    vector<int> b = {7, 9, 10, 11}; 

    cout << "Median: " << findMedian(a, b) << endl;
    return 0;
}
