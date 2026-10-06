from bisect import bisect_right


# Function to process queries on an array
def bishopandsoldier(n, q, a, queries):
    # Sort the array in ascending order
    a.sort()

    # Create a prefix sum array
    # Use long long to handle large sums
    pre = [0] * (n + 1)

    # Calculate the prefix sums
    for i in range(1, n + 1):
        # Cumulative sum up to index i
        pre[i] = pre[i - 1] + a[i - 1]

    for x in queries:
        # Find the index of the first element greater than x
        # bisect_right directly returns the first index whose value is greater than x.
        idx = bisect_right(a, x)
        # Output the index and the prefix sum at that index
        print(idx, pre[idx])


n = 7
a = [1, 2, 3, 4, 5, 6, 7]
queries = [3, 10]
bishopandsoldier(n, len(queries), a, queries)


'''
Time Complexity: O(n log n + q log n)

Reason:
The soldiers array is sorted once. Prefix sum construction is O(n). Each
query uses upper_bound/bisect_right, which is O(log n).

Space Complexity: O(n)

Reason:
The prefix sum list stores n + 1 values.
'''
