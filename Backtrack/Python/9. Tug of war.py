minDifference = float("inf")
bestSet1 = []
bestSet2 = []


# Recursive function to solve the Tug of War problem
def solve(arr, index, set1, set2, sumSet1, sumSet2):
    global minDifference, bestSet1, bestSet2
    # Base case: If all elements are placed
    if index == len(arr):
        # Ensure valid partition size
        if abs(len(set1) - len(set2)) > 1:
            return
        delta = abs(sumSet1 - sumSet2)
        if delta < minDifference:
            minDifference = delta
            bestSet1 = list(set1)
            bestSet2 = list(set2)
        return
    if len(set1) < (len(arr) + 1) // 2:
        set1.append(arr[index])
        solve(arr, index + 1, set1, set2, sumSet1 + arr[index], sumSet2)
        set1.pop()
    if len(set2) < (len(arr) + 1) // 2:
        set2.append(arr[index])
        solve(arr, index + 1, set1, set2, sumSet1, sumSet2 + arr[index])
        set2.pop()


def main():
    global minDifference, bestSet1, bestSet2
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    set1 = []
    set2 = []
    minDifference = float("inf")
    bestSet1 = []
    bestSet2 = []
    solve(arr, 0, set1, set2, 0, 0)
    print("Best Partition:\nSet 1:", *bestSet1)
    print("Set 2:", *bestSet2)
    print("Minimum Difference:", minDifference)


if __name__ == "__main__":
    main()


'''
Let n be element count.
Time: O(n*2^n) conservative upper bound: each item can enter either set,
with size limits pruning branches; copying an improved partition costs O(n).
Space: O(n) auxiliary sets/recursion plus O(n) saved best partition.
Current sets are backtracked in place. Reset minDifference/bestSet1/
bestSet2 before an independent search, as done in main.
'''
