# Comparator function for sorting jobs based on finish time
def compare(job):
    return job[1]


# Function to find the next job that can be scheduled after the current job
def findNextJob(jobs, currentIndex):
    for j in range(currentIndex + 1, len(jobs)):
        if jobs[j][0] >= jobs[currentIndex][1]:
            # Return the index of the next job that can be included
            return j
    # Return -1 if no compatible job is found
    return -1


# Recursive function with memoization to find the maximum profit
def findMaxProfit(jobs, currentIndex, memo):
    # Base case: No jobs left
    if currentIndex >= len(jobs):
        return 0

    # Check if we have already computed the maximum profit for this job index
    if memo[currentIndex] != -1:
        # Return the cached result
        return memo[currentIndex]

    # Exclude current job and move to the next
    excludeProfit = findMaxProfit(jobs, currentIndex + 1, memo)

    # Start with current job's profit
    includeProfit = jobs[currentIndex][2]
    # Find the next job
    nextJobIndex = findNextJob(jobs, currentIndex)

    if nextJobIndex != -1:
        # Add profit of next job
        includeProfit += findMaxProfit(jobs, nextJobIndex, memo)

    # Store the maximum profit for the current job index in memoization array
    memo[currentIndex] = max(includeProfit, excludeProfit)
    return memo[currentIndex]


# Wrapper function to sort jobs and initiate the recursive call with memoization
def jobScheduling(jobs):
    # Sort jobs based on finish time
    jobs.sort(key=compare)
    # Create a memoization array initialized to -1
    memo = [-1] * len(jobs)
    # Start recursive profit calculation from the first job
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
