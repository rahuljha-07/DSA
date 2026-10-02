class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit


def compare(a, b):
    return a.profit > b.profit


def JobScheduling(arr, n):
    arr[:n] = sorted(arr[:n], key=lambda a: a.profit, reverse=True)
    maxDeadline = 0
    for i in range(n):
        maxDeadline = max(maxDeadline, arr[i].deadline)
    slot = [False] * (maxDeadline + 1)
    totalProfit = 0
    jobCount = 0
    for i in range(n):
        for j in range(arr[i].deadline, 0, -1):
            if not slot[j]:
                slot[j] = True
                totalProfit += arr[i].profit
                jobCount += 1
                break
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
