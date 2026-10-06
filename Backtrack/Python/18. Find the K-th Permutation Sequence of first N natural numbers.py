import sys


def findKthPermutation(nums, visited, current, count, K, result):
    # Base case: If the current permutation is of length N
    if len(current) == len(nums):
        # Increment the count of generated permutations
        count[0] += 1
        # If this is the K-th permutation
        if count[0] == K:
            result[:] = current
        return
    # Explore all unused numbers for the current position
    for i in range(len(nums)):
        if not visited[i]:
            # Mark the number as used
            visited[i] = True
            # Add the number to the current permutation
            current.append(nums[i])
            findKthPermutation(nums, visited, current, count, K, result)
            # Stop recursion once we find the K-th permutation
            if result:
                return
            current.pop()
            # Mark the number as unused
            visited[i] = False


def getKthPermutation(N, K):
    nums = []
    for i in range(1, N + 1):
        # Generate numbers from 1 to N
        nums.append(i)
    # To track used numbers
    visited = [False] * N
    # Current permutation being built
    current = []
    # K-th permutation result
    result = []
    # To track how many permutations have been generated
    count = [0]
    findKthPermutation(nums, visited, current, count, K, result)
    return result


def main():
    tokens = iter(sys.stdin.read().split())
    print("Enter N (number of elements): ", end="")
    N = int(next(tokens))
    print("Enter K (desired permutation): ", end="")
    K = int(next(tokens))
    result = getKthPermutation(N, K)
    print(f"The {K}-th permutation is: ", end="")
    for num in result:
        print(num, end="")
    print()


if __name__ == "__main__":
    main()


'''
Let N be element count and K the 1-based requested permutation rank.
Time: O(N*N!) conservative worst case: enumerate lexicographically
ordered permutations, scanning N positions at recursive nodes, until K
is reached (or all permutations are exhausted). Earlier K stops sooner.
Space: O(N) auxiliary nums/visited/current/recursion, plus O(N) result.
The inconsistent C++ string/vector types are translated to mutable lists
of integers, preserving permutation backtracking rather than factorial indexing.
'''
