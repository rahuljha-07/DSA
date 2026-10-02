def canPlaceCows(stalls, numCows, minDist):
    countCows = 1
    lastPlaced = stalls[0]

    for i in range(1, len(stalls)):
        gap = stalls[i] - lastPlaced

        if gap >= minDist:
            countCows += 1
            lastPlaced = stalls[i]

            if countCows == numCows:
                return True

    return False


def largestMinDistance(stalls, numCows):
    stalls.sort()

    low = 1
    high = stalls[-1] - stalls[0]
    result = 0

    while low <= high:
        mid = low + (high - low) // 2

        if canPlaceCows(stalls, numCows, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result


stalls = [1, 2, 4, 8, 9]
numCows = 3
print(largestMinDistance(stalls, numCows))


'''
Time Complexity: O(n log n + n log R)

Reason:
Stalls are sorted first. Then binary search runs on the distance range R,
and each feasibility check scans all n stalls.

Space Complexity: O(1) auxiliary

Reason:
The placement check uses only counters and positions. Sorting is in place
from the algorithm point of view.
'''
