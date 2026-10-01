def MAH(arr, n):
    left = []          # Stores indices of nearest smaller elements to the left
    right = []         # Stores indices of nearest smaller elements to the right
    s = []             # Stack storing (value, index)

    area = float('-inf')

    # Fill left vector with indices of nearest smaller element to the left
    for i in range(n):

        if len(s) == 0:
            left.append(-1)

        elif len(s) > 0 and s[-1][0] < arr[i]:
            left.append(s[-1][1])

        elif len(s) > 0 and s[-1][0] >= arr[i]:

            while len(s) > 0 and s[-1][0] >= arr[i]:
                s.pop()

            if len(s) == 0:
                left.append(-1)
            else:
                left.append(s[-1][1])

        s.append((arr[i], i))

    # Clear stack to reuse it for right calculation
    s.clear()

    # Fill right vector with indices of nearest smaller element to the right
    for i in range(n - 1, -1, -1):

        if len(s) == 0:
            right.append(n)

        elif len(s) > 0 and s[-1][0] < arr[i]:
            right.append(s[-1][1])

        elif len(s) > 0 and s[-1][0] >= arr[i]:

            while len(s) > 0 and s[-1][0] >= arr[i]:
                s.pop()

            if len(s) == 0:
                right.append(n)
            else:
                right.append(s[-1][1])

        s.append((arr[i], i))

    # Reverse because right boundaries were calculated from right to left
    right.reverse()

    # Calculate maximum area
    for i in range(n):
        area = max(area, (right[i] - left[i] - 1) * arr[i])

    return area


def maxArea(M, n, m):
    # Store histogram heights row by row
    v = [0] * m

    ans = 0

    # Process first row
    for j in range(m):
        v[j] = M[0][j]

    ans = MAH(v, m)

    # Process subsequent rows
    for i in range(1, n):

        for j in range(m):

            # If cell is 0, reset histogram height
            if M[i][j] == 0:
                v[j] = 0

            # Otherwise increase height
            else:
                v[j] += M[i][j]

        # Find maximum histogram area for current row
        ans = max(ans, MAH(v, m))

    return ans


# Example usage
n = 4
m = 4

M = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 0],
    [1, 1, 0, 0]
]

print("Maximum rectangular area of 1's is:", maxArea(M, n, m))


'''
Time Complexity:
O(n * m)

Reason:

For each row of the matrix, we create/update a histogram.

Updating the histogram takes:
O(m)

Then we call MAH().

Inside MAH():

1. Finding nearest smaller element to the left takes O(m)
2. Finding nearest smaller element to the right takes O(m)
3. Calculating the maximum area takes O(m)

Even though there is a while loop inside the for loops,
each element is pushed and popped from the stack at most once.

Therefore, MAH() takes O(m).

Since MAH() is called for all n rows:

O(n * m)


Space Complexity:
O(m)

Reason:

We use:

v     -> O(m)
left  -> O(m)
right -> O(m)
stack -> O(m)

Therefore, total auxiliary space is:

O(m)
'''