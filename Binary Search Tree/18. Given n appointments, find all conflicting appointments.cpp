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


//nlogn solution sweep solution gpt
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

// Define an interval (start to end time)
struct Interval {
    int low, high;
    int id; // Used just to uniquely identify intervals
};

// Define an event (either start or end of an interval)
struct Event {
    int time;        // Time of event
    bool isStart;    // true = start of interval, false = end
    Interval interval;

    // Sorting rule: earlier time comes first.
    // If same time, start comes before end.
    bool operator<(const Event& other) const {
        if (time == other.time)
            return isStart > other.isStart;
        return time < other.time;
    }
};

void printConflicting(vector<Interval>& intervals) {
    vector<Event> events;

    // Step 1: Convert each interval into start and end events
    for (int i = 0; i < intervals.size(); ++i) {
        intervals[i].id = i;
        events.push_back({intervals[i].low, true, intervals[i]});  // start event
        events.push_back({intervals[i].high, false, intervals[i]}); // end event
    }

    // Step 2: Sort all events by time
    sort(events.begin(), events.end());

    // Step 3: Sweep line: store active intervals
    set<int> active; // store interval IDs that are currently running

    for (const auto& event : events) {
        if (event.isStart) {
            // A new interval is starting — check for conflicts
            for (int id : active) {
                const Interval& other = intervals[id];
                cout << "[" << event.interval.low << ", " << event.interval.high << "]"
                     << " conflicts with [" << other.low << ", " << other.high << "]\n";
            }
            // Add this interval to the active set
            active.insert(event.interval.id);
        } else {
            // An interval is ending — remove it from active
            active.erase(event.interval.id);
        }
    }
}
