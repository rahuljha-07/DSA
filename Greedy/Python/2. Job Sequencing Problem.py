class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit


# Comparator function to sort jobs by profit in descending order
def compare(a, b):
    return a.profit > b.profit


# Function to find the maximum profit and the number of jobs done
def JobScheduling(arr, n):
    arr[:n] = sorted(arr[:n], key=lambda a: a.profit, reverse=True)
    # Step 2: Find the maximum deadline among all jobs
    maxDeadline = 0
    for i in range(n):
        maxDeadline = max(maxDeadline, arr[i].deadline)
    # Array to track free slots (initialized to false)
    # 1-based indexing
    slot = [False] * (maxDeadline + 1)
    # Variables to store the total profit and count of jobs done
    totalProfit = 0
    jobCount = 0
    # Step 3: Assign jobs to available slots
    for i in range(n):
        # Find a slot for the current job, starting from its deadline
        for j in range(arr[i].deadline, 0, -1):
            # If slot is free
            if not slot[j]:
                # Mark slot as occupied
                slot[j] = True
                # Add profit of the job
                totalProfit += arr[i].profit
                # Increment job count
                jobCount += 1
                # Job is scheduled, break the loop
                break
    # Step 4: Return the number of jobs done and total profit
    return [jobCount, totalProfit]


def main():
    arr = [Job(1, 4, 20), Job(2, 1, 1), Job(3, 1, 40), Job(4, 1, 30)]
    n = len(arr)
    result = JobScheduling(arr, n)
    print("Number of jobs done:", result[0])
    print("Total profit:", result[1])


if __name__ == "__main__":
    main()


'''
Let n be jobs and D the largest nonnegative deadline.
Time: O(n log(n+1) + D + n*D): sort profits, allocate D+1 slots, and
scan backward through up to D slots per job. No DSU optimization is used.
Space: O(n + D) auxiliary sorting copies/workspace and slot array;
the returned count/profit needs O(1) output space.
Jobs take one time unit and profits are assumed nonnegative.
'''
