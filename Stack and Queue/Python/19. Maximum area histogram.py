def getMaxArea(arr, n):
    left = [0] * n
    right = [0] * n

    area = -10**18
    s = []

    for i in range(n):
        if len(s) == 0:
            left[i] = -1
        elif s[-1][0] < arr[i]:
            left[i] = s[-1][1]
        else:
            while len(s) != 0 and s[-1][0] >= arr[i]:
                s.pop()
            left[i] = -1 if len(s) == 0 else s[-1][1]
        s.append((arr[i], i))

    s.clear()

    for i in range(n - 1, -1, -1):
        if len(s) == 0:
            right[i] = n
        elif s[-1][0] < arr[i]:
            right[i] = s[-1][1]
        else:
            while len(s) != 0 and s[-1][0] >= arr[i]:
                s.pop()
            right[i] = n if len(s) == 0 else s[-1][1]
        s.append((arr[i], i))

    for i in range(n):
        area = max(area, (right[i] - left[i] - 1) * arr[i])

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
