MOD = 1000000007


# Function to calculate the maximum value of arr[i]*i
def maximizeValuePermutation(arr):
    # Step 1: Sort the array in ascending order
    arr.sort()
    # Step 2: Calculate the sum of arr[i] * i
    result = 0
    for i in range(len(arr)):
        # Add product modulo MOD
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
