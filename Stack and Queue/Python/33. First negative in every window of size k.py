from collections import deque


# Function to find the first negative integer in every window of size k
def printFirstNegativeInteger(arr, n, k):
    # list to store the results
    ans = []
    q = deque()
    # i: start index of the window, j: end index of the window
    i = 0
    j = 0

    # Loop until the end of the array is reached
    while j < n:
        # If the current element is negative, add it to the queue
        if arr[j] < 0:
            q.append(arr[j])

        # If the size of the current window is less than k, just expand the window
        if j - i + 1 < k:
            j += 1
        # When the size of the window reaches k
        elif j - i + 1 == k:
            # If there are no negative integers in the queue
            if len(q) == 0:
                # Add 0 to the answer list
                ans.append(0)
            # If there are negative integers in the queue
            else:
                # Add the first negative integer to the answer
                ans.append(q[0])
                # If the element that is being removed from the window is the same as the
                # front of the queue
                if arr[i] == q[0]:
                    # Remove it from the queue
                    q.popleft()
            # Move the window forward
            # Increment the start index
            i += 1
            # Increment the end index
            j += 1

    # Return the list containing the first negative integers for each window
    return ans


arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
result = printFirstNegativeInteger(arr, len(arr), k)
for x in result:
    print(x, end=" ")
print()


'''
Time Complexity: O(n)

Reason:
The sliding window moves each pointer forward only. Each negative value is
added to and removed from the queue at most once.

Space Complexity: O(k)

Reason:
The queue stores negative values from the current window, at most k values.
'''
