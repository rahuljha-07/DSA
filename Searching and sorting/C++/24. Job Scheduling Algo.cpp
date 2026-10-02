#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Job structure
struct Job {
    int start, finish, profit;
};

// Comparator function for sorting jobs based on finish time
bool compare(const Job &a, const Job &b) {
    return a.finish < b.finish;
}

// Function to find the next job that can be scheduled after the current job
int findNextJob(const vector<Job>& jobs, int currentIndex) {
    for (int j = currentIndex + 1; j < jobs.size(); j++) {
        if (jobs[j].start >= jobs[currentIndex].finish) {
            return j; // Return the index of the next job that can be included
        }
    }
    return -1; // Return -1 if no compatible job is found
}

// Recursive function with memoization to find the maximum profit
int findMaxProfit(const vector<Job>& jobs, int currentIndex, vector<int>& memo) {
    // Base case: No jobs left
    if (currentIndex >= jobs.size()) {
        return 0;
    }

    // Check if we have already computed the maximum profit for this job index
    if (memo[currentIndex] != -1) {
        return memo[currentIndex]; // Return the cached result
    }

    // Exclude current job and move to the next
    int excludeProfit = findMaxProfit(jobs, currentIndex + 1, memo);

    // Include current job and find next compatible job
    int includeProfit = jobs[currentIndex].profit; // Start with current job's profit
    int nextJobIndex = findNextJob(jobs, currentIndex); // Find the next job

    if (nextJobIndex != -1) {
        includeProfit += findMaxProfit(jobs, nextJobIndex, memo); // Add profit of next job
    }

    // Store the maximum profit for the current job index in memoization array
    return memo[currentIndex] = max(includeProfit, excludeProfit);
   
}

// Wrapper function to sort jobs and initiate the recursive call with memoization
int jobScheduling(vector<Job>& jobs) {
    // Sort jobs based on finish time
    sort(jobs.begin(), jobs.end(), compare);

    // Create a memoization array initialized to -1
    vector<int> memo(jobs.size(), -1);

    // Start recursive profit calculation from the first job
    return findMaxProfit(jobs, 0, memo);
}

// Main function
int main() {
    // Example jobs
    vector<Job> jobs = {{1, 2, 50}, {3, 5, 20}, {6, 19, 100}, {2, 100, 200}};
    
    // Calculate and output the maximum profit
    int maxProfit = jobScheduling(jobs);
    cout << "The maximum profit is: " << maxProfit << endl;

    return 0;
}
