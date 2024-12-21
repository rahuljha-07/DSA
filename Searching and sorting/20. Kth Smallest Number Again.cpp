#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Range {
    long long start, end;
};

long long findKthSmallestNumber(vector<Range>& intervals, long long k) {
    // Step 1: Sort intervals based on their starting points
    sort(intervals.begin(), intervals.end()); // Automatically sorts by `start` first, then by `end` if `start`s are equal

    // Step 2: Merge overlapping or contiguous intervals
    int idx = 0;  // Pointer to the last merged interval
    for (int i = 1; i < intervals.size(); i++) {
        if (intervals[idx].end >= intervals[i].start - 1) {
            // If intervals overlap or are contiguous, merge them
            intervals[idx].end = max(intervals[idx].end, intervals[i].end);
        } else {
            // Move to the next interval in the merged list
            idx++;
            intervals[idx] = intervals[i];
        }
    }

    // Step 3: Iterate over merged intervals to find the K-th smallest number
    long long answer = -1;
    for (int i = 0; i <= idx; i++) {
        // Calculate the size of the current interval
        long long intervalSize = intervals[i].end - intervals[i].start + 1;

        if (intervalSize >= k) {
            // K-th smallest number falls within this interval
            answer = intervals[i].start + k - 1;
            break;
        } else {
            // Move to the next interval by reducing K
            k -= intervalSize;
        }
    }

    return answer; // If K-th smallest is not found, answer will be -1
}

int main() {
    vector<Range> intervals = {{1, 5}, {3, 8}, {10, 12}};
    long long k = 6;
    cout << "K-th smallest number: " << findKthSmallestNumber(intervals, k) << endl;
    return 0;
}
