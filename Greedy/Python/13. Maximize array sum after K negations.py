# Function to maximize the sum of the array after K negations
def maximizeSum(arr, n, k):
    if n == 0:
        return 0
    # Step 1: Sort the array to prioritize negations on smallest (negative) elements
    arr.sort()
    # Step 2: Negate the smallest elements (negative ones) k times
    for i in range(n):
        if k == 0:
            break
        if arr[i] < 0:
            arr[i] = -arr[i]
            k -= 1
    # Step 3: If k is still greater than 0, and it's odd, negate the smallest element
    if k % 2 != 0:
        # Re-sort to ensure the smallest element is at the beginning
        arr.sort()
        arr[0] = -arr[0]
    # Step 4: Calculate and return the sum of the array
    sum = 0
    for i in range(n):
        sum += arr[i]
    return sum


def main():
    n = 5
    k = 1
    arr = [1, 2, -3, 4, 5]
    print(maximizeSum(arr, n, k))


if __name__ == "__main__":
    main()


'''
Let n be the array length; k is the number of allowed negations.
Time: O(n log(n+1)): there are at most two sorts and two O(n) scans.
The loop visits each element once rather than performing k separate passes.
Space: O(n) auxiliary worst case for Python's sorting workspace. Negations
modify arr in place; the scans themselves need O(1) additional space.
'''
