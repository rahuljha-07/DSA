def minSwaps(nums):
    # Step 1: Get the size of the input array
    n = len(nums)
    # Step 2: Create a list of pairs to store numbers and their original indices
    v = [None] * n

    # Step 3: Fill the list with pairs of (element value, original index)
    # Step 6: Iterate through the sorted array to find misplaced elements
    for i in range(n):
        v[i] = [nums[i], i]

    # Step 4: Sort the list based on the first element of the pairs (the original numbers)
    v.sort()

    # Step 5: Initialize a counter for swaps
    c = 0
    i = 0
    while i < n:
        # If the current element is in its correct position
        if v[i][1] == i:
            # Move to the next element
            i += 1
        else:
            # If the current element is not in the correct position, perform a swap
            # Increment the swap counter
            c += 1
            swapIndex = v[i][1]
            v[i], v[swapIndex] = v[swapIndex], v[i]

    # Note: Do not increment i here to check the new element at the current position
    # Step 7: Return the total number of swaps required
    return c


nums = [10, 19, 6, 3, 5]
print(minSwaps(nums))


'''
Time Complexity: O(n log n)

Reason:
The value/index pairs are sorted first, which takes O(n log n). The cycle
fixing loop performs at most O(n) swaps, so sorting dominates.

Space Complexity: O(n)

Reason:
The pair list v stores each element with its original index.
'''
