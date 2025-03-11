#include <bits/stdc++.h>
using namespace std;

// Structure to represent a Job
struct Job {
    int id;       // Job ID
    int deadline; // Deadline of job
    int profit;   // Profit if job is completed before or on the deadline
};

// Comparator function to sort jobs by profit in descending order
bool compare(Job a, Job b) {
    return a.profit > b.profit;
}

// Function to find the maximum profit and the number of jobs done
vector<int> JobScheduling(Job arr[], int n) {
    // Step 1: Sort jobs by profit in descending order
    sort(arr, arr + n, compare);

    // Step 2: Find the maximum deadline among all jobs
    int maxDeadline = 0;
    for (int i = 0; i < n; i++) {
        maxDeadline = max(maxDeadline, arr[i].deadline);
    }

    // Array to track free slots (initialized to false)
    vector<bool> slot(maxDeadline + 1, false); // 1-based indexing

    // Variables to store the total profit and count of jobs done
    int totalProfit = 0;
    int jobCount = 0;

    // Step 3: Assign jobs to available slots
    for (int i = 0; i < n; i++) {
        // Find a slot for the current job, starting from its deadline
        for (int j = arr[i].deadline; j > 0; j--) { // 1-based indexing
            if (!slot[j]) { // If slot is free
                slot[j] = true;            // Mark slot as occupied
                totalProfit += arr[i].profit; // Add profit of the job
                jobCount++;                // Increment job count
                break;                      // Job is scheduled, break the loop
            }
        }
    }

    // Step 4: Return the number of jobs done and total profit
    return {jobCount, totalProfit};
}

// Example usage
int main() {
    Job arr[] = {{1, 4, 20}, {2, 1, 1}, {3, 1, 40}, {4, 1, 30}};
    int n = sizeof(arr) / sizeof(arr[0]);

    vector<int> result = JobScheduling(arr, n);
    cout << "Number of jobs done: " << result[0] << endl;
    cout << "Total profit: " << result[1] << endl;

    return 0;
}
