INT_MAX = float("inf")


def minJumpsHelper(arr, index, n, dp):
    if index >= n - 1:
        return 0
    if arr[index] == 0:
        return INT_MAX
    if dp[index] != -1:
        return dp[index]
    minJumps = INT_MAX
    for step in range(1, arr[index] + 1):
        nextJumps = minJumpsHelper(arr, index + step, n, dp)
        if nextJumps != INT_MAX:
            minJumps = min(minJumps, 1 + nextJumps)
    dp[index] = minJumps
    return dp[index]


def minJumps(arr):
    n = len(arr)
    dp = [-1] * n
    result = minJumpsHelper(arr, 0, n, dp)
    return -1 if result == INT_MAX else result


def main():
    arr1 = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    arr2 = [1, 0, 3, 2]
    arr3 = [0]
    for arr in (arr1, arr2, arr3):
        print("Minimum jumps:", minJumps(arr))


if __name__ == "__main__":
    main()


'''
Let n be length and J=sum(arr[i]) over nonnegative jump capacities.
Time: O(n+J) upper bound: each reachable index is memoized once, but
its loop tries ALL arr[index] steps, including steps beyond the end.
Thus O(n^2) applies only when capacities are O(n); huge capacities can
make this source loop slower. No greedy replacement or loop cap is added.
Space: O(n) auxiliary memo array and deepest advancing recursion chain.
'''
