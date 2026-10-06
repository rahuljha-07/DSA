# Helper function for recursive backtracking
def countSubsequences(idx, product, k, arr, count):
    # Base case: If product exceeds k, stop recursion
    if product > k:
        return
    # Count the current subsequence (valid since product <= k)
    if idx == len(arr):
        count[0] += 1
        return
    countSubsequences(idx + 1, product * arr[idx], k, arr, count)
    # Exclude the current element
    countSubsequences(idx + 1, product, k, arr, count)


def countSubsequencesWithProductLessThanK(arr, k):
    if k < 1:
        return 0
    count = [0]
    countSubsequences(0, 1, k, arr, count)
    # Subtract 1 to exclude the empty subsequence
    return count[0] - 1


def main():
    arr = [1, 2, 3, 4]
    k = 10
    print(f"Number of subsequences with product <= {k}:",
          countSubsequencesWithProductLessThanK(arr, k))


if __name__ == "__main__":
    main()


'''
Let n be array length, with positive integer elements.
Time: O(2^n) worst case: each element has include/exclude choices and
the recursion can visit the full binary tree. product>k prunes branches
but does not improve the worst case. This source uses no DP memoization.
Space: O(n) auxiliary recursion stack plus one counter; subsequences are
counted without being stored. Arithmetic is treated as unit cost; large
Python products add bit-operation costs. The empty subsequence is removed.
Pruning is valid only when multiplying cannot reduce product (values>=1).
'''
