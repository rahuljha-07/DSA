import sys


# Helper function to find combinations using knapsack-like approach
def knapsackApproach(index, candidates, target, currentCombination, result):
    # Base case: If the target becomes zero, we have found a valid combination
    if target == 0:
        result.append(list(currentCombination))
        return
    # Base case: If index is out of bounds, stop recursion
    if index == len(candidates):
        return
    # If the current candidate is less than or equal to the target
    if candidates[index] <= target:
        # Option 1: Pick the current element
        currentCombination.append(candidates[index])
        # Since repetition is allowed, do not increment the index
        knapsackApproach(index, candidates, target - candidates[index], currentCombination, result)
        currentCombination.pop()
    # Option 2: Do not pick the current element and move to the next index
    knapsackApproach(index + 1, candidates, target, currentCombination, result)


def findCombinations(index, candidates, target, currentCombination, result):
    if target == 0:
        result.append(list(currentCombination))
        return
    # Iterate over the candidates array starting from the current index
    for i in range(index, len(candidates)):
        # If the current number exceeds the target, skip further processing
        if candidates[i] > target:
            break
        currentCombination.append(candidates[i])
        # Since the same number can be used multiple times, call the function with the same
        # index
        findCombinations(i, candidates, target - candidates[i], currentCombination, result)
        currentCombination.pop()


def combinationSum(arr, target):
    # Sort the array to ensure combinations are generated in non-descending order
    arr.sort()
    arr[:] = list(dict.fromkeys(arr))
    if any(value <= 0 for value in arr):
        raise ValueError("Candidates must be positive")
    # Result container to store all unique combinations
    result = []
    # Temporary container to store a single combination
    currentCombination = []
    # Start finding combinations from index 0
    findCombinations(0, arr, target, currentCombination, result)
    knapsackApproach(0, arr, target, currentCombination, result)
    return result


def main():
    tokens = iter(sys.stdin.read().split())
    print("Enter the number of elements in the array: ", end="")
    N = int(next(tokens))
    print("Enter the elements of the array: ", end="")
    arr = [int(next(tokens)) for _ in range(N)]
    print("Enter the target sum: ", end="")
    target = int(next(tokens))
    result = combinationSum(arr, target)
    if not result:
        print("Empty")
    else:
        for combination in result:
            print("(" + " ".join(map(str, combination)) + ")")


if __name__ == "__main__":
    main()


'''
Let n be unique positive candidates, T>=0 target, a smallest candidate,
and d=floor(T/a) maximum combination length.
Time: exponential in d/n: loop recursion has a conservative
O((n+1)^(d+1)) bound; include/exclude recursion has O(2^(n+d+1)) bound.
Sorting costs O(n log n); copying result combinations costs their total length.
Space: O(n+d) auxiliary deduplication/current path/recursion, plus output.
The source wrapper deliberately runs BOTH methods into result, so each
combination appears twice. Helpers can be called separately for one enumeration.
Zero/negative candidates are rejected to prevent nonterminating reuse.
'''
