memo = {}


def countSubsets(index, currentSum, nums, A, B):
    # Base case
    if index == len(nums):
        return 1 if currentSum >= A and currentSum <= B else 0

    # Generate a unique key for memoization
    key = str(index) + "_" + str(currentSum)

    if key in memo:
        return memo[key]

    include = countSubsets(index + 1, currentSum + nums[index], nums, A, B)
    # Exclude current element
    exclude = countSubsets(index + 1, currentSum, nums, A, B)

    # Memoize and return
    memo[key] = include + exclude
    return memo[key]


nums = [1, 2, 3]
A = 2
B = 4
print(countSubsets(0, 0, nums, A, B))


'''
Time Complexity: O(n * S)

Reason:
The memoized state is based on index and currentSum. If S different sums are
reachable, each index/sum state is solved once.

Space Complexity: O(n * S)

Reason:
The memo dictionary stores one value for each reachable index/sum state.
The recursion stack can also reach O(n).
'''
