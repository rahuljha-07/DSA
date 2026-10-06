def minSubsetSumDifference(arr, n):
    # Calculate the total sum of the array
    sum = 0
    for i in range(n):
        sum += arr[i]
    # Create a DP table `t` with dimensions (n+1) x (sum+1)
    t = [[False] * (sum + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        # No items => no subset for sum > 0
        # Subset with sum 0 always exists (empty subset)
        t[i][0] = True
    # Fill the table iteratively
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
            else:
                # Exclude the current element
                t[i][j] = t[i - 1][j]
    # Find all subset sums possible for the last row
    validSums = []
    for j in range(sum // 2 + 1):
        if t[n][j]:
            # Store all reachable subset sums
            validSums.append(j)
    mini = float("inf")
    for s1 in validSums:
        # Complementary subset sum
        s2 = sum - s1
        # Minimize the difference
        mini = min(mini, abs(s2 - s1))
    # or mini = min(mini, sum - 2 * s1);
    return mini


'''
Let n be elements and S their total nonnegative sum.
Time: O((n+1)*(S+1)): fill all subset-sum states, then scan up to S/2
reachable sums to minimize S-2*s1; these extra O(S) scans do not dominate.
Space: O((n+1)*(S+1)) DP table plus O(S+1) validSums storage.
'''
