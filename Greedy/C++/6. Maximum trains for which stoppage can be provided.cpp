#include <bits/stdc++.h>
using namespace std;

// Comparator function to sort trains by departure time
bool comp(vector<int> &a, vector<int> &b) {
    return a[1] < b[1]; // Sort by departure time
}

// Function to find the maximum number of trains that can be stopped
void maxStops(vector<vector<int>> &trains, int n, int m) {
    // Step 1: Sort the trains using the comparator
    sort(trains.begin(), trains.end(), comp);

    // Step 2: Track the last departure time for each platform
    vector<int> lastDeparture(n + 1, -1); // Platforms are 1-based
    int count = 0; // To count the number of accommodated trains

    // Step 3: Process each train
    for (int i = 0; i < m; i++) {
        int platform = trains[i][2]; // Platform number
        int arrival = trains[i][0];
        int departure = trains[i][1];

        // If platform is empty or the train can fit after the last train
        if (lastDeparture[platform] == -1 || lastDeparture[platform] <= arrival) {
            count++; // Train is accommodated
            lastDeparture[platform] = departure; // Update the last departure time for the platform
        }
    }

    // Output the result
    cout << "Maximum Stopped Trains = " << count << endl;
}

// Main function
int main() {
    // Example 1
    int n = 3; // Number of platforms
    int m = 6; // Number of trains
    vector<vector<int>> trains = {
        {1000, 1030, 1}, // Train 1
        {1010, 1030, 1}, // Train 2
        {1000, 1020, 2}, // Train 3
        {1030, 1200, 2}, // Train 4
        {1200, 1230, 3}, // Train 5
        {900, 1005, 1}   // Train 6
    };

    maxStops(trains, n, m); // Output: Maximum Stopped Trains = 5

    // Example 2
    n = 1; // Number of platforms
    m = 3; // Number of trains
    trains = {
        {1000, 1030, 1}, // Train 1
        {1110, 1130, 1}, // Train 2
        {1200, 1220, 1}  // Train 3
    };

    maxStops(trains, n, m); // Output: Maximum Stopped Trains = 3

    return 0;
}
