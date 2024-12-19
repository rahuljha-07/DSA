// this also works for same size
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

double median(vector<int>& a, vector<int>& b) {
    int n1 = a.size();
    int n2 = b.size();

    // Ensure that `a` is the smaller array to minimize binary search range
    if (n1 > n2) return median(b, a);

    int low = 0, high = n1;
    int left = (n1 + n2 + 1) / 2; // Mid-point for partitioning both arrays
    int n = n1 + n2;

    while (low <= high) {
        // Partition positions for both arrays
        int mid1 = (low + high) >> 1;
        int mid2 = left - mid1;

        // Edge cases for left and right elements on both sides of the partitions
        int l1 = (mid1 == 0) ? INT_MIN : a[mid1 - 1]; // Left element from `a`
        int l2 = (mid2 == 0) ? INT_MIN : b[mid2 - 1]; // Left element from `b`
        int r1 = (mid1 == n1) ? INT_MAX : a[mid1];    // Right element from `a`
        int r2 = (mid2 == n2) ? INT_MAX : b[mid2];    // Right element from `b`

        // Check if we found the correct partition
        if (l1 <= r2 && l2 <= r1) {
            // If total length is odd, median is max of left partition
            if (n % 2 == 1) return max(l1, l2);
            // If total length is even, median is average of max left and min right
            return ((double)(max(l1, l2) + min(r1, r2))) / 2.0;
        }
        // Adjust search range based on partition conditions
        else if (l1 > r2) {
            high = mid1 - 1; // Move left in `a`
        } else {
            low = mid1 + 1;  // Move right in `a`
        }
    }
    return 0.0; // In case no median is found, though logically unreachable
}
