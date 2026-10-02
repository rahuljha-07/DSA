MOD = 1000000007


def maximizeValuePermutation(arr):
    arr.sort()
    result = 0
    for i in range(len(arr)):
        result = (result + arr[i] * i) % MOD
    return result


def main():
    arr = [5, 3, 2, 4, 1]
    print(maximizeValuePermutation(arr))


if __name__ == "__main__":
    main()


'''
Let n be element count.
Time: O(n log(n+1)): sorting dominates the subsequent O(n) scan.
Space: O(n) auxiliary worst case for Python's sorting workspace, even
when the input list is sorted in place; no full result array is returned.
'''
