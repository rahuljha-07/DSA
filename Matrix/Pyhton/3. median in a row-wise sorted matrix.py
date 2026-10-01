from bisect import bisect_right


def median(A, n, m):
    # Step 1: Initialize min and max to the first element
    min = A[0][0]
    max = A[0][0]

    # Step 2: Find the overall minimum and maximum values in the matrix
    for i in range(n):
        # Update min to the smallest element in the first column
        if A[i][0] < min:
            min = A[i][0]

        # Update max to the largest element in the last column
        if A[i][m - 1] > max:
            max = A[i][m - 1]

    # Step 3: Calculate the position of the median element
    desired_element = (1 + n * m) // 2

    # Step 4: Perform binary search for the median
    while min < max:

        # Step 4.1: Find the middle value
        mid = (max + min) // 2
        count = 0

        # Step 4.2: Count elements less than or equal to mid
        for i in range(n):
            # bisect_right works like upper_bound in C++
            count += bisect_right(A[i], mid)

        # Step 4.3: Adjust min and max based on the count
        if count < desired_element:
            # If count is less than desired, increase min
            min = mid + 1
        else:
            # If count is greater or equal, decrease max
            max = mid

    # Step 5: Return the median value
    return min


'''
Time Complexity:
O(n * log(m) * log(max - min))

Reason:
We perform binary search on the value range from the minimum element
to the maximum element.

For every middle value, we go through all n rows.

For each row, bisect_right performs binary search in O(log(m)) time.

Therefore:
O(log(max - min) * n * log(m))

So the overall time complexity is:
O(n * log(m) * log(max - min))


Space Complexity:
O(1)

Reason:
We only use variables such as min, max, mid, count, and desired_element.

bisect_right does not create any extra data structure.

Therefore, auxiliary space complexity is O(1).
'''