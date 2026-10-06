# Function to find the smallest subset with a sum greater than the rest
def smallestSubset(arr):
    arr.sort(reverse=True)
    # Step 2: Calculate the total sum of the array
    totalSum = 0
    for num in arr:
        totalSum += num
    # Step 3: Find the smallest subset
    subsetSum = 0
    count = 0
    for num in arr:
        subsetSum += num
        count += 1
        if subsetSum > totalSum - subsetSum:
            break
    return count


def main():
    arr1 = [3, 1, 7, 1]
    arr2 = [2, 1, 2]
    print(smallestSubset(arr1))
    print(smallestSubset(arr2))


if __name__ == "__main__":
    main()


'''
Let n be the number of positive input values.
Time: O(n log(n+1)): descending sorting dominates summing all n values
and taking the largest values until the selected sum exceeds the rest.
Space: O(n) auxiliary worst case for Python's sorting workspace; the
running sums and count use O(1) space. The input order is modified.
As in the source, if no strict majority exists, the scan returns n.
'''
