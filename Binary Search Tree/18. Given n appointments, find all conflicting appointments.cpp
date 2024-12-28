#include <bits/stdc++.h>
using namespace std;

// Structure to represent an interval
struct Interval {
    int low, high;
};

// Function to check if two intervals overlap
bool doOverlap(Interval i1, Interval i2) {
    // Check if intervals i1 and i2 overlap
    return !(i1.high <= i2.low || i2.high <= i1.low);
}

// Function to print conflicting intervals
void printConflicting(vector<Interval>& intervals) {
    int n = intervals.size();

    // Check each pair of intervals
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (doOverlap(intervals[i], intervals[j])) {
                cout << "[" << intervals[i].low << ", " << intervals[i].high
                     << "] Conflicts with [" << intervals[j].low << ", " << intervals[j].high << "]\n";
            }
        }
    }
}

// Driver function to test the above code
int main() {
    vector<Interval> appointments = { {1, 5}, {3, 7}, {2, 6}, {10, 15}, {5, 6}, {4, 100} };
    cout << "Following are conflicting intervals:\n";
    printConflicting(appointments);
    return 0;
}
