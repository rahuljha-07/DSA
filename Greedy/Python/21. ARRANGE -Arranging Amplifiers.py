import sys





def main():
    tokens = iter(map(int, sys.stdin.read().split()))
    n = next(tokens)
    arr = []
    # Counter for the number of 1s
    countOnes = 0
    for _ in range(n):
        value = next(tokens)
        arr.append(value)
        if value == 1:
            countOnes += 1
    arr.sort(reverse=True)
    for _ in range(countOnes):
        print(1, end=" ")
    # Special case: If there are exactly two elements left and they are 3 and 2
    if n - countOnes == 2 and arr[0] == 3 and arr[1] == 2:
        print("2 3")
    else:
        # Input array and count the number of 1s
        # Output all 1s first
        # Output the remaining elements
        for i in range(n - countOnes):
            print(arr[i], end=" ")
        print()


if __name__ == "__main__":
    main()


'''
Let n be the number of positive integer amplifier values.
Time: O(n log(n+1)): descending sorting dominates reading, counting ones,
and printing the n values. The special remaining pair [3, 2] is reversed
to [2, 3] in constant time, matching the source.
Space: O(n) for arr, buffered input tokens, and Python's sort workspace.
No separate output permutation is allocated.
'''
