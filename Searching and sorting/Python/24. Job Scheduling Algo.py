def compare(job):
    return job[1]


def findNextJob(jobs, currentIndex):
    for j in range(currentIndex + 1, len(jobs)):
        if jobs[j][0] >= jobs[currentIndex][1]:
            return j
    return -1


def findMaxProfit(jobs, currentIndex, memo):
    if currentIndex >= len(jobs):
        return 0

    if memo[currentIndex] != -1:
        return memo[currentIndex]

    excludeProfit = findMaxProfit(jobs, currentIndex + 1, memo)

    includeProfit = jobs[currentIndex][2]
    nextJobIndex = findNextJob(jobs, currentIndex)

    if nextJobIndex != -1:
        includeProfit += findMaxProfit(jobs, nextJobIndex, memo)

    memo[currentIndex] = max(includeProfit, excludeProfit)
    return memo[currentIndex]


def jobScheduling(jobs):
    jobs.sort(key=compare)
    memo = [-1] * len(jobs)
    return findMaxProfit(jobs, 0, memo)


jobs = [[1, 2, 50], [3, 5, 20], [6, 19, 100], [2, 100, 200]]
maxProfit = jobScheduling(jobs)
print("The maximum profit is:", maxProfit)


'''
Time Complexity: O(n^2)

Reason:
Sorting jobs takes O(n log n). The memoized recursion solves each index once,
but findNextJob may scan forward O(n) for each index, giving O(n^2).

Space Complexity: O(n)

Reason:
The memo list stores one value per job and recursion depth can reach O(n).
'''
