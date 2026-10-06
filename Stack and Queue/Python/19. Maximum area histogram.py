def getMaxArea(arr, n):
    # lists to store the indices of the previous smaller and next smaller elements
    # For the nearest smaller element on the left
    left = [0] * n
    # For the nearest smaller element on the right
    right = [0] * n

    area = -10**18
    # Stack to keep track of the histogram bars
    s = []

    # Fill the left list with indices of the nearest smaller elements on the left
    for i in range(n):
        # If the stack is empty, no smaller element exists on the left
        if len(s) == 0:
            left[i] = -1
        elif s[-1][0] < arr[i]:
            # Current bar is taller than the top of the stack
            # -1 if no smaller element found
            left[i] = s[-1][1]
        else:
            # Current bar is shorter or equal to the top of the stack
            while len(s) != 0 and s[-1][0] >= arr[i]:
                # Pop until a smaller element is found
                s.pop()
            left[i] = -1 if len(s) == 0 else s[-1][1]
        # Push current bar height and its index onto the stack
        s.append((arr[i], i))

    s.clear()

    # Fill the right list with indices of the nearest smaller elements on the right
    for i in range(n - 1, -1, -1):
        # If the stack is empty, no smaller element exists on the right
        if len(s) == 0:
            # n represents the boundary for the right side
            right[i] = n
        elif s[-1][0] < arr[i]:
            right[i] = s[-1][1]
        else:
            while len(s) != 0 and s[-1][0] >= arr[i]:
                s.pop()
            # n if no smaller element found
            right[i] = n if len(s) == 0 else s[-1][1]
        s.append((arr[i], i))

    # Calculate the maximum area using the left and right lists
    for i in range(n):
        # Area = width * height
        area = max(area, (right[i] - left[i] - 1) * arr[i])

    # Return the maximum area found
    return area


arr = [6, 2, 5, 4, 5, 1, 6]
print(getMaxArea(arr, len(arr)))


'''
Time Complexity: O(n)

Reason:
Each bar is pushed and popped at most once while finding previous and next
smaller elements. The final area scan is also linear.

Space Complexity: O(n)

Reason:
The left, right, and stack structures can each store up to n entries.
'''
