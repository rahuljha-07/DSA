#include <bits/stdc++.h>
using namespace std;

// Structure to represent a Job
struct Job {
    int id;      // Job ID
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

    // Step 2: Initialize variables
    int maxDeadline = 0; // Find the maximum deadline among all jobs
    for (int i = 0; i < n; i++) {
        maxDeadline = max(maxDeadline, arr[i].deadline);
    }

    // Array to track free slots (initialized to false)
    vector<bool> slot(maxDeadline, false);

    // Variables to store the total profit and count of jobs done
    int totalProfit = 0;
    int jobCount = 0;

    // Step 3: Assign jobs to available slots
    for (int i = 0; i < n; i++) {
        // Find a slot for the current job, starting from its deadline
        for (int j = min(maxDeadline - 1, arr[i].deadline - 1); j >= 0; j--) {
            if (!slot[j]) { // If slot is free
                slot[j] = true;         // Mark slot as occupied
                totalProfit += arr[i].profit; // Add profit of the job
                jobCount++;             // Increment job count
                break;                  // Job is scheduled, break the loop
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

/*
Let's go through an example walkthrough step by step for the **Job Sequencing Problem** using the code provided:

---

### Example Input:
```plaintext
jobs[] = [(1, 4, 20), (2, 1, 1), (3, 1, 40), (4, 1, 30)]
```
Here:
- Job 1: ID = 1, Deadline = 4, Profit = 20
- Job 2: ID = 2, Deadline = 1, Profit = 1
- Job 3: ID = 3, Deadline = 1, Profit = 40
- Job 4: ID = 4, Deadline = 1, Profit = 30

---

### Step 1: Sort Jobs by Profit in Descending Order
After sorting based on profit:

```plaintext
Sorted jobs[] = [(3, 1, 40), (4, 1, 30), (1, 4, 20), (2, 1, 1)]
```

---

### Step 2: Determine Maximum Deadline
From the sorted jobs, find the maximum deadline:

```plaintext
Maximum Deadline = max(1, 1, 4, 1) = 4
```

This means we need to allocate a `slot` array of size 4 (for deadlines 1 to 4):

```plaintext
slot[] = [false, false, false, false]
```

---

### Step 3: Schedule Jobs
We will now iterate over the sorted jobs and try to schedule each job in the latest available slot before its deadline.

---

#### Job 3: (ID = 3, Deadline = 1, Profit = 40)
- **Deadline:** 1
- Check slot 0 (0-based index for deadline 1): `slot[0]` is `false`.
- Schedule Job 3 in slot 0.
- Mark `slot[0]` as `true`.
- **Profit:** Add 40 to the total profit.
  
```plaintext
slot[] = [true, false, false, false]
Total profit = 40
Job count = 1
```

---

#### Job 4: (ID = 4, Deadline = 1, Profit = 30)
- **Deadline:** 1
- Check slot 0: `slot[0]` is `true`.
- No available slots before the deadline. Skip Job 4.

```plaintext
slot[] = [true, false, false, false]
Total profit = 40
Job count = 1
```

---

#### Job 1: (ID = 1, Deadline = 4, Profit = 20)
- **Deadline:** 4
- Check slot 3 (0-based index for deadline 4): `slot[3]` is `false`.
- Schedule Job 1 in slot 3.
- Mark `slot[3]` as `true`.
- **Profit:** Add 20 to the total profit.

```plaintext
slot[] = [true, false, false, true]
Total profit = 60
Job count = 2
```

---

#### Job 2: (ID = 2, Deadline = 1, Profit = 1)
- **Deadline:** 1
- Check slot 0: `slot[0]` is `true`.
- No available slots before the deadline. Skip Job 2.

```plaintext
slot[] = [true, false, false, true]
Total profit = 60
Job count = 2
```

---

### Step 4: Final Result
After processing all jobs:

```plaintext
Number of jobs done = 2
Total profit = 60
```

---

### Output:
```plaintext
Result: [2, 60]
```

---

### Explanation of Scheduled Jobs:
- **Job 3 (Profit = 40):** Scheduled in slot 0 (Deadline 1).
- **Job 1 (Profit = 20):** Scheduled in slot 3 (Deadline 4).
- Other jobs could not be scheduled due to unavailable slots.

This walkthrough matches the example provided and demonstrates the process clearly!
*/