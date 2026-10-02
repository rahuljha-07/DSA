def helper(startIndex, arr, visited, k, currentSum, targetSum, n):
    if k == 1:
        return True
    if currentSum == targetSum:
        return helper(0, arr, visited, k - 1, 0, targetSum, n)
    for i in range(startIndex, n):
        if not visited[i]:
            visited[i] = True
            if helper(i + 1, arr, visited, k, currentSum + arr[i], targetSum, n):
                return True
            visited[i] = False
    return False


def helperUsingIncludeExclude(n, arr, visited, k, currentSum, targetSum):
    if k == 1:
        return True
    if currentSum == targetSum:
        # Each new subset must reconsider ALL still-unvisited positions.
        return helperUsingIncludeExclude(len(visited), arr, visited, k - 1, 0, targetSum)
    if n <= 0:
        return False
    if helperUsingIncludeExclude(n - 1, arr, visited, k, currentSum, targetSum):
        return True
    if not visited[n - 1] and currentSum + arr[n - 1] <= targetSum:
        visited[n - 1] = True
        if helperUsingIncludeExclude(n - 1, arr, visited, k, currentSum + arr[n - 1], targetSum):
            return True
        visited[n - 1] = False
    return False


def isKPartitionPossible(arr, n, k):
    sum = 0
    for i in range(n):
        sum += arr[i]
    if k <= 0 or k > n or sum % k != 0:
        return False
    targetSum = sum // k
    visited = [False] * n
    return helper(0, arr, visited, k, 0, targetSum, n)


def isKPartitionPossibleUsingIncludeExclude(arr, n, k):
    sum = 0
    for i in range(n):
        sum += arr[i]
    if k <= 0 or k > n or sum % k != 0:
        return False
    targetSum = sum // k
    visited = [False] * n
    return helperUsingIncludeExclude(n, arr, visited, k, 0, targetSum)


def main():
    arr = [2, 1, 4, 5, 6]
    n = len(arr)
    k = 3
    print("1 (Partitioning is possible)" if isKPartitionPossible(arr, n, k)
          else "0 (Partitioning is not possible)")


if __name__ == "__main__":
    main()


'''
Let n be elements and k requested nonempty subsets, with nonnegative values.
Time: exponential: the loop method explores disjoint subset assignments;
O(n*(k+1)^n) is a conservative bound including scans. Include/exclude
has a loose O(2^(n*k)) search bound because each subset can rescan n items.
Space: O(n+k) auxiliary loop recursion/visited; include/exclude may retain
O(n*k) calls across subset transitions.
Both helpers are exposed: the source's second return was unreachable and
its include/exclude call had the wrong argument count. New-group scanning
resets to the full array. k>n is rejected; zero target is feasible for
nonnegative all-zero input when k<=n.
'''
