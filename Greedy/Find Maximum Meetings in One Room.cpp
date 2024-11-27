#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to find and print the maximum meetings
void maxMeetings(vector<int>& start, vector<int>& end, int n) {
    // Vector to store meeting details: start time, end time, and index
    vector<vector<int>> meetings;

    // Populate the meetings vector
    for (int i = 0; i < n; i++) {
        meetings.push_back({start[i], end[i], i + 1});
    }

    // Sort meetings based on end time
    sort(meetings.begin(), meetings.end(), [](vector<int>& a, vector<int>& b) {
        return a[1] < b[1]; // Sort by end time
    });

    // To store the selected meetings
    vector<int> selectedMeetings;
    selectedMeetings.push_back(meetings[0][2]); // Select the first meeting
    int timeLimit = meetings[0][1]; // Set the time limit to the end time of the first meeting

    // Traverse through the meetings and select the ones that can be attended
    for (int i = 1; i < n; i++) {
        // If the start time of the current meeting is greater than the time limit
        if (meetings[i][0] > timeLimit) {
            selectedMeetings.push_back(meetings[i][2]); // Select the meeting
            timeLimit = meetings[i][1]; // Update the time limit
        }
    }

    // Print the selected meeting numbers
    for (int meeting : selectedMeetings) {
        cout << meeting << " ";
    }
    cout << endl;
}

// Driver code
int main() {
    vector<int> start = {1, 3, 0, 5, 8, 5}; // Start times of meetings
    vector<int> end = {2, 4, 6, 7, 9, 9};   // End times of meetings
    int n = start.size(); // Number of meetings

    // Call the function to find and print the maximum meetings
    maxMeetings(start, end, n);

    return 0;
}
