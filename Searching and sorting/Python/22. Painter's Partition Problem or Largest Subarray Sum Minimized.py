# Function to check if it is possible to paint all boards with the given maximum time
def canPaint(boards, k, maxTime):
    # Start with one painter
    painterCount = 1
    # Time used by current painter
    currentTime = 0

    # Iterate through each board
    for i in range(len(boards)):
        # Add current board's length to current painter's time
        # Start with current board for new painter
        currentTime += boards[i]

        # If total time exceeds allowed maxTime
        if currentTime > maxTime:
            # Allocate to a new painter
            painterCount += 1
            currentTime = boards[i]

            # If painters used exceed allowed limit, return false
            if painterCount > k:
                return False

    # All boards can be painted within maxTime using k painters
    return True


# Function to find the minimum time required to paint all boards with k painters
def findMinimumTime(boards, k):
    low = max(boards)
    high = sum(boards)
    # Initialize result to the maximum possible time
    result = high

    # Perform binary search to find the minimum time
    while low <= high:
        # Calculate mid point
        mid = low + (high - low) // 2

        # Check if it's possible to paint all boards within mid time
        if canPaint(boards, k, mid):
            # Update result with the current mid time
            result = mid
            # Try for a smaller time
            high = mid - 1
        else:
            # Increase time limit to try again
            low = mid + 1

    # Return the minimum time
    return result


boards = [10, 20, 30, 40]
k = 2
print("Minimum time to paint all boards:", findMinimumTime(boards, k))


'''
Time Complexity: O(n * log(sum - max))

Reason:
The answer is binary searched between max board length and total board
length. For every candidate time, canPaint scans all boards once.

Space Complexity: O(1)

Reason:
Only painter counters, current time, and binary-search variables are used.
'''
