def canPaint(boards, k, maxTime):
    painterCount = 1
    currentTime = 0

    for i in range(len(boards)):
        currentTime += boards[i]

        if currentTime > maxTime:
            painterCount += 1
            currentTime = boards[i]

            if painterCount > k:
                return False

    return True


def findMinimumTime(boards, k):
    low = max(boards)
    high = sum(boards)
    result = high

    while low <= high:
        mid = low + (high - low) // 2

        if canPaint(boards, k, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

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
