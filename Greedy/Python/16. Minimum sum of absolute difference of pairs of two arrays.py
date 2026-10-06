# Function to calculate the minimum sum of absolute differences
def minimumSumOfDifferences(a, b):
    n = len(a)
    # Step 1: Sort both arrays
    a.sort()
    b.sort()
    # Step 2: Calculate the sum of absolute differences
    minSum = 0
    for i in range(n):
        minSum += abs(a[i] - b[i])
    return minSum


def main():
    a = [4, 1, 8, 7]
    b = [2, 3, 6, 5]
    print(minimumSumOfDifferences(a, b))


if __name__ == "__main__":
    main()


'''
Let n be the common length of a and b.
Time: O(n log(n+1)): two sorts cost O(n log(n+1)) in total, followed
by an O(n) scan pairing elements at the same sorted index.
Space: O(n) auxiliary worst case for Python's sort workspace. Both input
arrays are sorted in place; only a running sum is stored during pairing.
'''
