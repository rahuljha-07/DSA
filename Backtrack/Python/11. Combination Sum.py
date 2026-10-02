import sys


def knapsackApproach(index, candidates, target, currentCombination, result):
    if target == 0:
        result.append(list(currentCombination))
        return
    if index == len(candidates):
        return
    if candidates[index] <= target:
        currentCombination.append(candidates[index])
        knapsackApproach(index, candidates, target - candidates[index], currentCombination, result)
        currentCombination.pop()
    knapsackApproach(index + 1, candidates, target, currentCombination, result)


def findCombinations(index, candidates, target, currentCombination, result):
    if target == 0:
        result.append(list(currentCombination))
        return
    for i in range(index, len(candidates)):
        if candidates[i] > target:
            break
        currentCombination.append(candidates[i])
        findCombinations(i, candidates, target - candidates[i], currentCombination, result)
        currentCombination.pop()


def combinationSum(arr, target):
    arr.sort()
    arr[:] = list(dict.fromkeys(arr))
    if any(value <= 0 for value in arr):
        raise ValueError("Candidates must be positive")
    result = []
    currentCombination = []
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
