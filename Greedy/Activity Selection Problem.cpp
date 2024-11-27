 #include <bits/stdc++.h>
using namespace std;

// Comparator function to sort meetings by their end time
bool comp(pair<int, int>& a, pair<int, int>& b) {
    return a.second < b.second;
}

int maxMeetings(vector<int>& start, vector<int>& end) {
    int n = start.size();

    // Create a vector of pairs to store start and end times of meetings
    vector<pair<int, int>> meetings(n);
    for (int i = 0; i < n; i++) {
        meetings[i] = {start[i], end[i]};
    }

    // Sort the meetings based on their end times
    sort(meetings.begin(), meetings.end(), comp);

    // Initialize variables
    int count = 1; // Count of meetings that can be held (start with the first meeting)
    int lastEndTime = meetings[0].second; // End time of the last selected meeting

    // Iterate through the sorted meetings to select non-overlapping meetings
    for (int i = 1; i < n; i++) {
        // If the current meeting starts after the last selected meeting ends
        if (meetings[i].first > lastEndTime) {
            count++; // Increment count of meetings
            lastEndTime = meetings[i].second; // Update the last end time
        }
    }

    return count; // Return the maximum number of meetings
}

// Example usage
int main() {
    vector<int> start = {1, 3, 0, 5, 8, 5};
    vector<int> end = {2, 4, 6, 7, 9, 9};

    cout << "Maximum number of meetings: " << maxMeetings(start, end) << endl;

    return 0;
}
