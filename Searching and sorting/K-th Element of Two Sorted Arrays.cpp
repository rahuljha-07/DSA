// same as median of 2 sorted array
// this also works for same size
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int kthsmallest(vector<int>& a, vector<int>& b) {
    int n1 = a.size();
    int n2 = b.size();

    // Ensure that `a` is the smaller array to minimize binary search range
    if (n1 > n2) return kthsmallest(b, a);

    int low = max(k-n2, 0); // We can't take more than k from b, so we adjust accordingly.
    int high = min(k, n1);  // We can't take more than n1 from a.

    int left = k;
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
            return max(l1, l2);
        }
        // Adjust search range based on partition conditions
        else if (l1 > r2) {
            high = mid1 - 1; // Move left in `a`
        } else {
            low = mid1 + 1;  // Move right in `a`
        }
    }
    return 0; // In case kth smallest is not found, though logically unreachable
}
