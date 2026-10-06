from collections import deque


# Function to calculate the sum of minimum and maximum elements of all subarrays of size k
def sumOfMinAndMax(arr, k):
    n = len(arr)
    # Return 0 if k is greater than n or non-positive
    if n < k or k <= 0:
        return 0

    # Deque to store indices of maximum elements
    maxDeque = deque()
    # Deque to store indices of minimum elements
    minDeque = deque()
    # Variable to store the total sum
    sum = 0

    # Initialize two pointers
    i = 0
    j = 0

    while j < n:
        # For max deque
        while len(maxDeque) != 0 and maxDeque[-1] < arr[j]:
            maxDeque.pop()
        # Add current element
        maxDeque.append(arr[j])

        # For min deque
        while len(minDeque) != 0 and minDeque[-1] > arr[j]:
            minDeque.pop()
        minDeque.append(arr[j])

        # If we have processed at least k elements
        if j - i + 1 == k:
            # The front of the maxDeque is the maximum for the current window
            # The front of the minDeque is the minimum for the current window
            # Add to sum
            sum += maxDeque[0] + minDeque[0]

            # Move the window forward: remove the element going out of the window
            if maxDeque[0] == arr[i]:
                # Remove from max deque
                maxDeque.popleft()
            if minDeque[0] == arr[i]:
                # Remove from min deque
                minDeque.popleft()

            # Move the start of the window
            i += 1
        # Move the end of the window
        j += 1

    # Return the total sum
    return sum


arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = sumOfMinAndMax(arr, k)
print("Sum of min and max of all subarrays of size", str(k) + ":", result)


'''
Time Complexity: O(n)

Reason:
Each element is inserted and removed from the max deque and min deque at most
once while the sliding window moves.

Space Complexity: O(k)

Reason:
Each deque stores candidates from the current window, bounded by k elements.
'''
